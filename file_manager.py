def add_user_to_file(account):
    with open("/accounts.txt", "r") as f:
        for acc in f.readlines():
            if (acc.split(';')[0] == account.type) and (acc.split(';')[1] == account.owner):
                return False

    with open("/accounts.txt", 'a') as f:
        if account.type == "INT":
            f.write(f"{account.type};{account.owner};{account.balance}\n")
            return True
        else:
            f.write(f"{account.type};{account.owner};{account.last_withdraw_date};{account.daily_withdraw};{account.balance}\n")
            return True

def read_from_file():
    with open("/accounts.txt", "r") as f:
        return f.readlines()

def update_user_record(account, accounts):
    for i, acc in enumerate(accounts):
        if (account.type == acc.type) and (account.owner == acc.owner):
            accounts[i] = account

    update_file(accounts)

def delete_user_record(account, accounts):
    for i, acc in enumerate(accounts):
        if (account.type == acc.type) and (account.owner == acc.owner):
            del accounts[i]

    update_file(accounts)

def update_file(accounts):
    open("/accounts.txt", 'w').close()
    with open("/accounts.txt", 'a') as f:
        for account in accounts:
            if account.type == "INT":
                f.write(f"{account.type};{account.owner};{account.balance}\n")
            else:
                f.write(
                    f"{account.type};{account.owner};{account.last_withdraw_date};{account.daily_withdraw};{account.balance}\n")

