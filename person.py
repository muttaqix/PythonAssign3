from chequing import Chequing
from savings import Savings

class Person:
    def __init__(self, name, acct_type):
        self.name = name
        self.deposit_count = 0

        if acct_type == "Chequing":
            self.account = Chequing()
        elif acct_type == "Savings":
            self.account = Savings()
        else:
            print("Please choose either a Chequing or Savings account")

    def deposit(self,amount):
        self.account.deposit(amount)
        self.deposit_count +=1

    def withdraw(self,amount):
        self.account.withdraw(amount)
        