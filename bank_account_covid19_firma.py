from bank_account_covid19 import BankAccountCOVID19

class BankAccountCOVID19Firma(BankAccountCOVID19):
    def __init__(self, accounts, owner, last_withdraw_date, daily_withdraw, balance):
        self.type = "Firma"
        self.owner = owner
        self.last_withdraw_date = last_withdraw_date
        self.daily_withdraw = daily_withdraw
        self.daily_withdraw_limit = 1000
        self.balance = balance
        self._accounts = accounts
        self.check_if_exists(accounts)
