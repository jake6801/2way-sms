from services.test_data import get_accounts, add_account, edit_account, delete_account, get_first_message, get_final_message, get_account, get_closing_message

def list_accounts():
    return get_accounts()

def list_account(symendID):
    return get_account(symendID)

def get_closer_message(account, indx):
    return get_closing_message(account, indx)

def add_accounts(account):
    return add_account(account)

def edit_accounts(account):
    return edit_account(account)

def delete_accounts(symendID):
    return delete_account(symendID)

def get_message1(account, indx):
    return get_first_message(account, indx)

def get_message2():
    return get_final_message()