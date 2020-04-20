from main_template import BankAccount
from file_manager import add_user_to_file, update_user_record, delete_user_record

class BankAccountINT(BankAccount):
    def __init__(self, accounts, owner, balance):
        self.type = "INT"
        self.owner = owner
        self.balance = balance
        self._accounts = accounts
        print(self.check_if_exists(accounts))

    def deposit(self, amount):
        self.balance += amount
        update_user_record(self, self._accounts)
        return f"Deposited {amount}, balance is {self.balance}"

    def withdraw(self, amount):
        if (self.balance - amount) >= 0:
            self.balance -= amount
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
                return "User already exists"
        accounts.append(self)
        add_user_to_file(self)
        return "User Created"
