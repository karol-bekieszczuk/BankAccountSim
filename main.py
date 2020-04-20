from menu import Menu, CreateAccountCommand, ExitCommand, ListAccountsCommand
from bank_account_int import BankAccountINT
from bank_account_covid19 import BankAccountCOVID19
from bank_account_covid19_firma import BankAccountCOVID19Firma
from file_manager import read_from_file

def main():
    accounts = []

    for acc_obj in read_from_file():
        acc = acc_obj.split(';')
        if acc[0] == "INT":
            BankAccountINT(accounts, acc[1], float(acc[2]))
        elif acc[0] == "PL":
            BankAccountCOVID19(accounts, acc[1], acc[2], acc[3], float(acc[4]))
        else:
            BankAccountCOVID19Firma(accounts, acc[1], acc[2], acc[3], float(acc[4]))


    menu = Menu()

    menu.add_command(CreateAccountCommand(accounts))
    menu.add_command(ListAccountsCommand(accounts))
    menu.add_command(ExitCommand(menu))

    menu.run()


main()
