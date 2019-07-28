# Just a plain if statement
bank_balance = 10000

# The amount the user wishes to spend
debit = int(input("How much should I debit the account by?\n"))

if bank_balance >= debit:
    print("Transaction taking place.")
    bank_balance -= debit

# We print the current balance just to check if the code worked as intended
print("Current bank balance is {}.".format(bank_balance))
