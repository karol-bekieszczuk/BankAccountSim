from main_template import BankAccount
from file_manager import add_user_to_file, update_user_record, delete_user_record
from datetime import datetime, timedelta

class BankAccountCOVID19(BankAccount):
    def __init__(self, accounts, owner, last_withdraw_date, daily_withdraw, balance):
        self.type = "PL"
        self.owner = owner
        self.last_withdraw_date = last_withdraw_date
        self.daily_withdraw = daily_withdraw
        self.daily_withdraw_limit = 1000
        self.balance = balance
        self._accounts = accounts
        self.check_if_exists(accounts)

    def deposit(self, amount):
        self.balance += amount
        update_user_record(self, self._accounts)
        return f"Deposited {amount}, balance is {self.balance}"

    def withdraw(self, amount):
        if self.check_if_daily_limit_reached(amount):
            return f"Daily limit reached, limit is {self.daily_withdraw_limit}"
        if (self.balance - amount) >= 0:
            self.balance -= amount
            self.last_withdraw_date = datetime.today()
            update_user_record(self, self._accounts)
            return f"Withdrawed {amount}, left {self.balance}"
        else:
            return "Cant withdraw, not enought funds"

    def close(self):
        self.withdraw(self.balance)
        delete_user_record(self, self._accounts)
        del self

    def check_if_exists(self, accounts):
        for acc in accounts:
            if self.owner == acc.owner:
                print(self.owner)
                print(acc.owner)
                return "User already exists"
        accounts.append(self)
        add_user_to_file(self)
        return "User Created"

    def check_if_daily_limit_reached(self, amount):
        if datetime.today() > datetime(2020, 4, 1):
            return False
        if (self.last_withdraw_date is datetime.today()) and ((amount + self.daily_withdraw) > self.daily_withdraw_limit):
            self.daily_withdraw += amount
            return True
        else:
            return False
