from datetime import datetime
class Transaction:

    def withdraw(self,balance):
        amount = input("Enter amount to withdraw: ")
        withdrawal_amount = int(amount)
        balance = balance - withdrawal_amount
        today = datetime.today()
        today = today.strftime("%d/%m/%Y %H:%M:%S")
        with open('bank_statement.py', 'w') as file:
            file.write(f"{today}\tAmount withdrawn: {withdrawal_amount} \n{today}\tAccount Balance:{balance}")
        return balance   

    def deposit(self,balance):
        amount = input("Enter amount to deposit: ")
        deposit_amount = int(amount)
        balance = balance + deposit_amount
        today = datetime.today()
        today = today.strftime("%d/%m/%Y %H:%M:%S")
        with open('bank_statement.py', 'a') as file:
            file.write(f"\n{today}\tAmount deposited: {deposit_amount} \n{today}\tAccount Balance:{balance}")
        return balance

transaction = Transaction()

while (True):
    message = input("""Welcome! What would you like to do;
                ..................
                 1. Depposit
                 2. Check Balance
                 3. Withdraw
                 4. Exit
                 : """)
    message = int(message)
    if (message == 1):
        output = transaction.deposit(151515)
        print(f"Your account balance is {output}")
        break
    
    if (message == 3):
        output = transaction.withdraw(11223)
        print(f"Your account balance is {output}")
        break
    if (message == 4):
        print(f"Thank you for being a valued customer!")
        break
