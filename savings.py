from account import Account

class Savings(Account):
    def __init__(self):
        super().__init__(acct_type="Savings") 
        self.over_draft = -1200

    def profit(self):
        profit_amount = self.current_balance * 0.15
        self.current_balance += profit_amount
        print("Profit of", profit_amount, "was added. New balance is:", self.current_balance)
