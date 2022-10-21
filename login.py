

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
import sys
from PyQt5.uic import loadUi
from mongo_setup import *


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()

class Login(QMainWindow):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("finance_login.ui", self)

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
        loadUi('dashboard.ui', self) 
        self.savings_button.clicked.connect(self.click)
        
        

    def click(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

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
        loadUi("savings.ui", self)

        self.amount_label.hide()
        self.input_amount.hide()
        self.finish_button.hide()
        self.balance_modify()
        
        self.fund_add.clicked.connect(self.add_funds)   
        

    def balance_modify(self):
        for i in savings.find({}, {'Savings Balance': 1}):
            self.new_balance = str(i["Savings Balance"])
            self.balance.setText(self.new_balance)


    def add_funds(self):
        self.finish_button.clicked.connect(self.add_funds_db)
        return int

    def add_funds_db(self):
        increase = int(self.input_amount.text())
        savings.find_one_and_update({'_id': 1}, {'$inc':{'Savings Balance': + increase}})
        self.balance_modify()
          


saving = Savings()
widget.addWidget(saving)

sys.exit(app.exec_())



            


    

