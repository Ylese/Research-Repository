from BankAccount import BankAccount

if __name__ == "__main__":
      
    bankacc1 = BankAccount("Lyle Jose", "02-1234-009500-00")
    bankacc1.deposit(2000.00)
    bankacc1.withdraw(500.00)
    bankacc1.display_info()

