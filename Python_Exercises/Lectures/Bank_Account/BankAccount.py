from datetime import date

class BankAccount():
    account_number: None
    account_holder: None
    balance: None
    opening_date: None

    def __init__(self, account_holder, account_number):
        self.account_holder = account_holder
        self.account_number = account_number
        self.balance = 0.00
        self.opening_date = date.today()

    def display_info(self):
        print("**** BANK ACCOUNT ****")
        print("Account Number:", self.account_number)
        print("Account Holder:", self.account_holder)
        print("Account Balance:", self.balance)
        print("Opening Date:", self.opening_date)

#deposit money onto bank acc
# parameter: sum - to deposit
    def deposit(self, sum):
        self.balance += sum

#withdraw money onto bank acc
# parameter: sum to deposit    
    def withdraw(self, sum):
        if sum > self.balance:
            print("Insufficient Balance")
            return
        self.balance -= sum


bankacc1 = BankAccount("Lyle Jose", "02-1234-009500-00")
bankacc1.deposit(2000.00)
bankacc1.withdraw(500.00)
bankacc1.display_info()