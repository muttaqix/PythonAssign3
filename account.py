class Account:
    def __init__(self,acct_type,min_balance=500):
        self.acct_type = acct_type
        self.min_balance = min_balance
        self.current_balance = min_balance
    
    def withdraw(self,amount):
        pass

    def deposit(self,amount):
        pass 
        