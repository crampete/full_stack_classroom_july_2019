# if else

# let's assume the password is imbatman
super_secret_password = "imbatman"
user_entered_password = input("Please enter the super secret password.\n")

# string comparison to check if they match
if user_entered_password == super_secret_password:
    # the passwords match
    print("You are now logged in.")
else:
    # user entered password doesn't match the secret password.
    print("Oops. Wrong password.")
