from datetime import datetime, timedelta
from bank_account_int import BankAccountINT
from bank_account_covid19 import BankAccountCOVID19
from bank_account_covid19_firma import BankAccountCOVID19Firma

class MenuCommand:
    def description(self):
        raise NotImplementedError

    def execute(self):
        raise NotImplementedError


class ExitCommand(MenuCommand):
    def __init__(self, menu):
        super().__init__()
        self._menu = menu

    def description(self):
        return "Exit"

    def execute(self):
        self._menu.stop()


class AddINTAccount(MenuCommand):
    def __init__(self, accounts):
        super().__init__()
        self._accounts = accounts

    def description(self):
        return "Create INT account"

    def execute(self):
        BankAccountINT(self._accounts, input("Owner name: "), 0)

class AddCOVID19Account(MenuCommand):
    def __init__(self, accounts):
        super().__init__()
        self._accounts = accounts

    def description(self):
        return "Create PL Account"

    def execute(self):
        BankAccountCOVID19(self._accounts, input("Owner name: "), datetime.today() - timedelta(days=1), 0, 0)

class AddCOVID19FirmaAccount(MenuCommand):
    def __init__(self, accounts):
        super().__init__()
        self._accounts = accounts

    def description(self):
        return "Create Firma Account"

    def execute(self):
        BankAccountCOVID19Firma(self._accounts, input("Owner name: "), datetime.today() - timedelta(days=1), 0, 5000)

class CreateAccountCommand(MenuCommand):
    def __init__(self, accounts):
        self._accounts = accounts

    def description(self):
        return "Add new account"

    def execute(self):
        menu = Menu()
        menu.add_command(AddINTAccount(self._accounts))
        menu.add_command(AddCOVID19Account(self._accounts))
        menu.add_command(AddCOVID19FirmaAccount(self._accounts))
        menu.add_command(ExitCommand(menu))

        menu.run()

class ChooseAccount(MenuCommand):
    def __init__(self, account):
        self._account = account

    def description(self):
        return f"{self._account.type} - {self._account.owner}, {self._account.balance}"

    def execute(self):
        menu = Menu()
        menu.add_command(DepositToAccount(self._account))
        menu.add_command(WithdrawFromAccount(self._account))
        menu.add_command(CloseAccount(self._account, menu))
        menu.add_command(ExitCommand(menu))

        menu.run()

class DepositToAccount(MenuCommand):
    def __init__(self, account):
        self._account = account
        # self._amount = amount

    def description(self):
        return "Deposit to account"

    def execute(self):
        print(self._account.deposit(float(input("Enter the amount to deposit: "))))

class WithdrawFromAccount(MenuCommand):
    def __init__(self, account):
        self._account = account

    def description(self):
        return "Withdraw from account"

    def execute(self):
        print(self._account.withdraw(float(input("Enter the amount to withdraw: "))))

class CloseAccount(MenuCommand):
    def __init__(self, account, menu):
        self._account = account
        self._menu = menu

    def description(self):
        return "Close the account"

    def execute(self):
        print(self._account.close())

        self._menu.stop()

class ListAccountsCommand(MenuCommand):
    def __init__(self, accounts):
        self._accounts = accounts

    def description(self):
        return "List all accounts"

    def execute(self):
        if len(self._accounts) is not 0:
            print("Choose account to deposit, withdraw or close")
            menu = Menu()
            for account in self._accounts:
                menu.add_command(ChooseAccount(account))
            menu.add_command(ExitCommand(menu))

            menu.run()

class Menu:
    def __init__(self):
        self._commands = []
        self._should_running = True

    def add_command(self, cmd):
        self._commands.append(cmd)

    def run(self):
        while self._should_running:
            self._display_menu()
            self._execute_selected_command()

    def stop(self):
        self._should_running = False

    def _display_menu(self):
        for i, cmd in enumerate(self._commands):
            print("{}. {}".format(i + 1, cmd.description()))

    def _execute_selected_command(self):
        try:
            cmd_num = int(input("Select menu item (1-{}): ".format(len(self._commands))))
            cmd = self._commands[cmd_num - 1]
            cmd.execute()
        except:
            print("Invalid input")
