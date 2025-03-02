from account import Account
class Chequing(Account):
    def __init__(self):
        super().__init__(acct_type="Chequing")
        self.over_draft = 1000