class Account:
    def __init__(self,acct_type,min_balance=500):
        self.acct_type = acct_type
        self.min_balance = min_balance
        self.current_balance = min_balance
    
    def withdraw(self,amount):
        if self.current_balance - amount < self.over_draft:
            print("You have exceeded the overdraft limit")
        else:
            self.current_balance -= amount
            print("You withdrew:", amount,"New balance is:", self.current_balance)

            if self.current_balance < 0:
                self.over_draft +=200
                print("Overdraft limit increased by 200")
    def deposit(self,amount):
        self.current_balance +=amount
        print("You deposited", amount, "Updated balance is:", self.current_balance)
        
        