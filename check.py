## account.py
class Account:
    def __init__(self, acct_type, min_balance=500):
        self.acct_type = acct_type
        self.min_balance = min_balance
        self.current_balance = min_balance  # Initially set to min_balance

    def withdraw(self, amount):
        if self.current_balance - amount < -self.over_draft:
            print("Withdrawal denied: Exceeds overdraft limit!")
        else:
            self.current_balance -= amount
            print(f"Withdrawn: ${amount}. New balance: ${self.current_balance}")
            
            if self.current_balance < 0:
                self.over_draft += 200
                print("Warning: Account is in overdraft! Overdraft limit increased by $200.")

    def deposit(self, amount):
        self.current_balance += amount
        print(f"Deposited: ${amount}. New balance: ${self.current_balance}")

## checking.py
from account import Account

class Checking(Account):
    def __init__(self):
        super().__init__(acct_type="Checking")
        self.over_draft = 1000

## savings.py
from account import Account

class Savings(Account):
    def __init__(self):
        super().__init__(acct_type="Savings")
        self.over_draft = 1200
    
    def profit(self):
        profit_amount = self.current_balance * 0.15
        self.current_balance += profit_amount
        print(f"Profit of ${profit_amount} added. New balance: ${self.current_balance}")

## person.py
from checking import Checking
from savings import Savings

class Person:
    def __init__(self, name, account_type):
        self.name = name
          self.deposit_count = 0
        
        if account_type.lower() == "checking":
            self.account = Checking()
        elif account_type.lower() == "savings":
            self.account = Savings()
        else:
            raise ValueError("Invalid account type! Choose 'Checking' or 'Savings'.")

    def deposit(self, amount):
        self.account.deposit(amount)
        self.deposit_count += 1
        
        if isinstance(self.account, Savings) and self.deposit_count % 10 == 0:
            self.account.profit()

    def withdraw(self, amount):
        self.account.withdraw(amount)

## main.py
from person import Person

def main():
    name = input("Enter your name: ")
    account_type = input("Choose account type (Checking/Savings): ")
    user = Person(name, account_type)
    
    while True:
        action = input("Choose an action (deposit/withdraw/exit): ").lower()
        if action == "deposit":
            amount = float(input("Enter deposit amount: "))
            user.deposit(amount)
        elif action == "withdraw":
            amount = float(input("Enter withdrawal amount: "))
            user.withdraw(amount)
        elif action == "exit":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid action. Please choose again.")

if __name__ == "__main__":
    main()
