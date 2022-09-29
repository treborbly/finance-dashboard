

from home import home_dashboard

accounts = ['Robert Bailey', 'Julianna Mercado']

acc_passes = ['robertsaccount', 'juliannasaccount']

def login_dashboard():
    passcode = ''
    while True:
        prompt = input('Which user will be continuing?: '.lower())

        if prompt == accounts[0].lower():
            passcode = input('Please enter your passcode: ')
            if passcode == acc_passes[0]:
                home_dashboard()
                break
            elif passcode != acc_passes[0]:
                error = print('Your passcode is incorrect, please try again.')
                continue
            
        if prompt == accounts[1].lower():
            passcode = input('Please enter your passcode: ')
            if passcode == acc_passes[1]:
                home_dashboard()
                break
            elif passcode != acc_passes[1]:
                error = print('Your passcode is incorrect, please try again.')
                continue
            





    

