

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from PyQt5.uic import loadUi
from mongo_setup import *
import constants as const


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()

class Login(QMainWindow):
    def __init__(self):
        super(Login,self).__init__()
        loadUi(const.LOGIN, self)

        self.accounts = ['robert bailey', 'julianna mercado']
        self.acc_passes = ['robertsaccount', 'juliannasaccount']

        self.enter_button.clicked.connect(self.submit)

    def submit(self):
        username = self.username_input.text()
        password = self.password_input.text()

        while True:
            if username == self.accounts[0] and password == self.acc_passes[0]:
                widget.setCurrentIndex(widget.currentIndex()+1)
                break
            if username == self.accounts[1] and password == self.acc_passes[1]:
                widget.setCurrentIndex(widget.currentIndex()+1)
                break

            if username != self.accounts[0] or password != self.acc_passes[0]:
                self.error()
                break
            if username != self.accounts[1] or password != self.acc_passes[1]:
                self.error()
                break
                   
    def error(self):
        error = QMessageBox()
        error.setWindowTitle('ERROR')
        error.setText('Error: No account under that credentials.')
        show_error = error.exec_()


login = Login()
widget.addWidget(login)

class Dashboard(QMainWindow):
    def __init__(self):
        super(Dashboard, self).__init__()
        loadUi(const.DASHBOARD, self) 
        self.savings_button.clicked.connect(self.savings_click)
        self.expendables_button.clicked.connect(self.expendables_click)
        self.phone_button.clicked.connect(self.phone_click)
        
    
    def savings_click(self):
        widget.setCurrentIndex(widget.currentIndex()+1)


    def expendables_click(self):
        widget.setCurrentIndex(widget.currentIndex()+2)

    
    def phone_click(self):
        widget.setCurrentIndex(widget.currentIndex()+3)

    def init():
        app = QApplication(sys.argv)
        init = Dashboard()
        init.show()
        sys.exit(app.exec_())

dashboard = Dashboard()
widget.addWidget(dashboard)


class Savings(QMainWindow):
    def __init__(self):
        super (Savings,self).__init__()
        loadUi(const.SAVINGS, self)
        self.back()
        self.balance_modify()
        
        self.fund_add.clicked.connect(self.add_funds)
        self.fund_remove.clicked.connect(self.remove_funds)   
        

    def balance_modify(self):
        for i in savings_db.find({}, {'Savings Balance': 1}):
            self.new_balance = str(i["Savings Balance"])
            self.balance.setText(self.new_balance)


    def add_funds(self):
        # Enter Amount
        self.amount_label = QtWidgets.QLabel(self.centralwidget)
        self.amount_label.setGeometry(QtCore.QRect(250, 450, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        font.setPointSize(18)
        self.amount_label.setFont(font)
        self.amount_label.setObjectName("amount_label")
        self.amount_label.setText("Enter Amount:")
        self.amount_label.show()

        # Input Amount
        self.input_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(400, 450, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        self.input_amount.setFont(font)
        self.input_amount.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.input_amount.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.input_amount.setObjectName("input_amount")
        self.input_amount.setText("0")
        self.input_amount.setPlaceholderText("Amount")
        self.input_amount.show()

        # Finish Button
        self.finish_button = QtWidgets.QPushButton(self.centralwidget)
        self.finish_button.setGeometry(QtCore.QRect(350, 490, 71, 32))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        self.finish_button.setFont(font)
        self.finish_button.setStyleSheet("background-color: rgba(79, 52, 0,179);\n"
"color: rgb(255, 255, 255);")
        self.finish_button.setObjectName("finish_button")
        self.finish_button.setText("Finish")
        self.finish_button.show()

        self.finish_button.clicked.connect(self.add_funds_db)


    def add_funds_db(self):
        savings_db.find_one_and_update({'_id': 1}, {'$inc':{'Savings Balance': + int(self.input_amount.text())}})
        self.balance_modify()
        self.close_objects()

    
    def remove_funds(self):
        # "Enter Amount"
        self.amount_label = QtWidgets.QLabel(self.centralwidget)
        self.amount_label.setGeometry(QtCore.QRect(250, 450, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        font.setPointSize(18)
        self.amount_label.setFont(font)
        self.amount_label.setObjectName("amount_label")
        self.amount_label.setText("Enter Amount:")
        self.amount_label.show()

        # Input Amount
        self.input_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(400, 450, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        self.input_amount.setFont(font)
        self.input_amount.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.input_amount.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.input_amount.setObjectName("input_amount")
        self.input_amount.setText("0")
        self.input_amount.setPlaceholderText("Amount")
        self.input_amount.show()

        # Finish Button
        self.finish_button = QtWidgets.QPushButton(self.centralwidget)
        self.finish_button.setGeometry(QtCore.QRect(350, 490, 71, 32))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        self.finish_button.setFont(font)
        self.finish_button.setStyleSheet("background-color: rgba(79, 52, 0,179);\n"
"color: rgb(255, 255, 255);")
        self.finish_button.setObjectName("finish_button")
        self.finish_button.setText("Finish")
        self.finish_button.show()

        self.finish_button.clicked.connect(self.remove_funds_db)

    
    def remove_funds_db(self):
        savings_db.find_one_and_update({'_id': 1}, {'$inc':{'Savings Balance': - int(self.input_amount.text())}})
        self.balance_modify()
        self.close_objects()

   
    def close_objects(self):
        self.amount_label.close()
        self.input_amount.close()
        self.finish_button.close()


    def back(self):
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(20, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(79, 52, 0,179);")
        self.back_button.setObjectName("back_button")
        self.back_button.setText("Back")
        self.back_button.show()

        self.back_button.clicked.connect(self.previous)

    
    def previous(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

savings = Savings()
widget.addWidget(savings)


class Expendables(QMainWindow):
    def __init__(self):
        super (Expendables, self).__init__()
        loadUi(const.EXPENDABLES, self)
        self.back()
        self.balance_modify()

        self.fund_add.clicked.connect(self.add_funds)
        self.fund_remove.clicked.connect(self.remove_funds)

    
    def balance_modify(self):
        for i in expendables_db.find({}, {'Expendable Balance': 1}):
            self.new_balance = str(i["Expendable Balance"])
            self.balance.setText(self.new_balance)

    
    def add_funds(self):
        # Enter Amount
        self.amount_label = QtWidgets.QLabel(self.centralwidget)
        self.amount_label.setGeometry(QtCore.QRect(250, 450, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        font.setPointSize(18)
        self.amount_label.setFont(font)
        self.amount_label.setObjectName("amount_label")
        self.amount_label.setText("Enter Amount:")
        self.amount_label.show()

        # Input Amount
        self.input_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(400, 450, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        self.input_amount.setFont(font)
        self.input_amount.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.input_amount.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.input_amount.setObjectName("input_amount")
        self.input_amount.setText("0")
        self.input_amount.setPlaceholderText("Amount")
        self.input_amount.show()

        # Finish Button
        self.finish_button = QtWidgets.QPushButton(self.centralwidget)
        self.finish_button.setGeometry(QtCore.QRect(350, 490, 71, 32))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        self.finish_button.setFont(font)
        self.finish_button.setStyleSheet("background-color: rgba(79, 52, 0,179);\n"
"color: rgb(255, 255, 255);")
        self.finish_button.setObjectName("finish_button")
        self.finish_button.setText("Finish")
        self.finish_button.show()

        self.finish_button.clicked.connect(self.add_funds_db)


    def add_funds_db(self):
        expendables_db.find_one_and_update({'_id': 1}, {'$inc':{'Expendable Balance': + int(self.input_amount.text())}})
        self.balance_modify()
        self.close_objects()

    
    def remove_funds(self):
        # "Enter Amount"
        self.amount_label = QtWidgets.QLabel(self.centralwidget)
        self.amount_label.setGeometry(QtCore.QRect(250, 450, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        font.setPointSize(18)
        self.amount_label.setFont(font)
        self.amount_label.setObjectName("amount_label")
        self.amount_label.setText("Enter Amount:")
        self.amount_label.show()

        # Input Amount
        self.input_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(400, 450, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        self.input_amount.setFont(font)
        self.input_amount.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.input_amount.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.input_amount.setObjectName("input_amount")
        self.input_amount.setText("0")
        self.input_amount.setPlaceholderText("Amount")
        self.input_amount.show()

        # Finish Button
        self.finish_button = QtWidgets.QPushButton(self.centralwidget)
        self.finish_button.setGeometry(QtCore.QRect(350, 490, 71, 32))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        self.finish_button.setFont(font)
        self.finish_button.setStyleSheet("background-color: rgba(79, 52, 0,179);\n"
"color: rgb(255, 255, 255);")
        self.finish_button.setObjectName("finish_button")
        self.finish_button.setText("Finish")
        self.finish_button.show()

        self.finish_button.clicked.connect(self.remove_funds_db)

    
    def remove_funds_db(self):
        expendables_db.find_one_and_update({'_id': 1}, {'$inc':{'Expendable Balance': - int(self.input_amount.text())}})
        self.balance_modify()
        self.close_objects()

   
    def close_objects(self):
        self.amount_label.close()
        self.input_amount.close()
        self.finish_button.close()

    
    def back(self):
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(20, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(79, 52, 0,179);")
        self.back_button.setObjectName("back_button")
        self.back_button.setText("Back")
        self.back_button.show()

        self.back_button.clicked.connect(self.previous)

    
    def previous(self):
        widget.setCurrentIndex(widget.currentIndex()-2)

expendables = Expendables()
widget.addWidget(expendables)


class Phone(QMainWindow):
    def __init__(self):
        super (Phone, self).__init__()
        loadUi(const.PHONE, self)

        self.back()
        self.balance_modify()

        self.fund_add.clicked.connect(self.add_funds)
        self.fund_remove.clicked.connect(self.remove_funds)

    
    def balance_modify(self):
        for i in phone_db.find({}, {'Phone Payment Balance': 1}):
            self.new_balance = str(i["Phone Payment Balance"])
            self.balance.setText(self.new_balance)

    
    def add_funds(self):
        # Enter Amount
        self.amount_label = QtWidgets.QLabel(self.centralwidget)
        self.amount_label.setGeometry(QtCore.QRect(250, 450, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        font.setPointSize(18)
        self.amount_label.setFont(font)
        self.amount_label.setObjectName("amount_label")
        self.amount_label.setText("Enter Amount:")
        self.amount_label.show()

        # Input Amount
        self.input_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(400, 450, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        self.input_amount.setFont(font)
        self.input_amount.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.input_amount.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.input_amount.setObjectName("input_amount")
        self.input_amount.setText("0")
        self.input_amount.setPlaceholderText("Amount")
        self.input_amount.show()

        # Finish Button
        self.finish_button = QtWidgets.QPushButton(self.centralwidget)
        self.finish_button.setGeometry(QtCore.QRect(350, 490, 71, 32))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        self.finish_button.setFont(font)
        self.finish_button.setStyleSheet("background-color: rgba(79, 52, 0,179);\n"
"color: rgb(255, 255, 255);")
        self.finish_button.setObjectName("finish_button")
        self.finish_button.setText("Finish")
        self.finish_button.show()

        self.finish_button.clicked.connect(self.add_funds_db)


    def add_funds_db(self):
        phone_db.find_one_and_update({'_id': 1}, {'$inc':{'Phone Payment Balance': + int(self.input_amount.text())}})
        self.balance_modify()
        self.close_objects()

    
    def remove_funds(self):
        # "Enter Amount"
        self.amount_label = QtWidgets.QLabel(self.centralwidget)
        self.amount_label.setGeometry(QtCore.QRect(250, 450, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        font.setPointSize(18)
        self.amount_label.setFont(font)
        self.amount_label.setObjectName("amount_label")
        self.amount_label.setText("Enter Amount:")
        self.amount_label.show()

        # Input Amount
        self.input_amount = QtWidgets.QLineEdit(self.centralwidget)
        self.input_amount.setGeometry(QtCore.QRect(400, 450, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        self.input_amount.setFont(font)
        self.input_amount.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.input_amount.setInputMethodHints(QtCore.Qt.ImhNone)
        self.input_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.input_amount.setObjectName("input_amount")
        self.input_amount.setText("0")
        self.input_amount.setPlaceholderText("Amount")
        self.input_amount.show()

        # Finish Button
        self.finish_button = QtWidgets.QPushButton(self.centralwidget)
        self.finish_button.setGeometry(QtCore.QRect(350, 490, 71, 32))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        self.finish_button.setFont(font)
        self.finish_button.setStyleSheet("background-color: rgba(79, 52, 0,179);\n"
"color: rgb(255, 255, 255);")
        self.finish_button.setObjectName("finish_button")
        self.finish_button.setText("Finish")
        self.finish_button.show()

        self.finish_button.clicked.connect(self.remove_funds_db)

    
    def remove_funds_db(self):
        phone_db.find_one_and_update({'_id': 1}, {'$inc':{'Phone Payment Balance': - int(self.input_amount.text())}})
        self.balance_modify()
        self.close_objects()

   
    def close_objects(self):
        self.amount_label.close()
        self.input_amount.close()
        self.finish_button.close()


    def back(self):
        self.back_button = QtWidgets.QPushButton(self.centralwidget)
        self.back_button.setGeometry(QtCore.QRect(20, 20, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Menlo")
        self.back_button.setFont(font)
        self.back_button.setStyleSheet("color: rgb(255, 255, 255);\n"
"background-color: rgba(79, 52, 0,179);")
        self.back_button.setObjectName("back_button")
        self.back_button.setText("Back")
        self.back_button.show()

        self.back_button.clicked.connect(self.previous)

    
    def previous(self):
        widget.setCurrentIndex(widget.currentIndex()-3)

phone = Phone()
widget.addWidget(phone)

sys.exit(app.exec_())



            


    

