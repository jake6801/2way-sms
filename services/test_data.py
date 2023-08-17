# test accounts 
data = {
    "accounts": [
      {
        "symendID": 1,
        "firstName": "Jake",
        "lastName": "Houston",
        "dueBalance": 150.00,
        "paymentExtension": False,
        "serviceCancellation": False
      },
      {
        "symendID": 2,
        "firstName": "Tim",
        "lastName": "Sanchez",
        "dueBalance": 200.00,
        "paymentExtension": False,
        "serviceCancellation": False
      },
      {
        "symendID": 3,
        "firstName": "Dean",
        "lastName": "Skelton",
        "dueBalance": 300.00,
        "paymentExtension": False,
        "serviceCancellation": False
      }
    ]
}

# introductory messages
firstMessages = {
    "messages": [
        {
            "message": "Hello {} {}, you have an overdue balance of ${}, reply 1 to request a payment extension or 2 to cancel your services."
        },
        {
            "message": "{} {} your balance of ${} is about to be overdue, please reply 1 to request a payment extension, or reply 2 to cancel your services."
        },
        {
            "message": "Hi {} {}, your services have an overdue balance of ${}, you can reply 1 to request a payment extension, or reply 2 to cancel your services."
        },
    ]
}

# not currently in use 
finalMessages = {
    "messages": [
        {
            "message1": "Thank you for your reply, your request is being processed."
        },
        {
            "message2": "Thank you for replying {}, your request will be processed."
        },
        {
            "message3": "Thank you for your reply, your request is being processed."
        }
    ]
}

# closing messages for paymentExtension request
extensionFinalMessage = {
    "messages": [
        {
            "message": "Thank you for replying {}, your payment extension request will be processed."
        },
        {
            "message": "Your payment extension request will be processed, thank you for replying {}."
        }
    ]
}

# closing messages for serviceCancellation request
cancellationFinalMessage = {
    "messages": [
        {
            "message": "Thank you for replying {}, your services will be cancelled."
        },
        {
            "message": "Thank you {}, your services will be cancelled. You will be missed."
        }
    ]
}

# endpoint that will get the first message
def get_first_message(account, indx):
    return firstMessages["messages"][indx]["message"].format(account["firstName"], account["lastName"], "{:.2f}".format(account["dueBalance"]))

# endpoint that will get the final message 
def get_final_message():
    return finalMessages["messages"][0]["message1"]

# endpoint that will get the extension final message 
def get_closing_message(account, indx):
    if account["paymentExtension"] == True:
      return extensionFinalMessage["messages"][indx]["message"].format(account["firstName"])
    else:
      return cancellationFinalMessage["messages"][indx]["message"].format(account["firstName"]) 

# endpoint that will get an account
def get_account(symendID):
    for i,account in enumerate(data["accounts"]):
        if account["symendID"] == symendID:
            return data["accounts"][i]

# endpoint that will list all accounts
def get_accounts():
    return data['accounts']

# endpoint that will add a new account
def add_account(account):
    account["symendID"] = len(data['accounts']) + 1
    data['accounts'].append(account)
    return {
      "message": "account added",
      "number of accounts": len(data['accounts'])
    }

# endpoint to update an account
def edit_account(updatedAccount):
    for i,account in enumerate(data["accounts"]):
        if account["symendID"] == updatedAccount["symendID"]:
           data["accounts"][i] = updatedAccount
    
    return {
      "message": "account edited",
      "number of accounts": len(data['accounts'])
    }

# endpoint to delete an account
def delete_account(account_id):
    item_to_remove = '';
    for account in data["accounts"]:
        if int(account_id) == account["symendID"]:
            item_to_remove = account
    if item_to_remove:
        data["accounts"].remove(item_to_remove)
    
    return {
      "message": "account deleted",
      "number of accounts": len(data['accounts'])
    }