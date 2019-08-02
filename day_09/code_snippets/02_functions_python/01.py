def ask_questions_get_user():
    user_details = {}

    user_details['name'] = input("Please enter your name.\n")
    print(f"Hi {user_details['name']}")
    user_details['age'] = input("Please enter your age.\n")
    user_details['city'] = input("Which city/town do you reside in?\n")
    
    return user_details


def print_user_details(user_details):
    print("...")
    print("...")
    print("Printing student details...")
    print("...")
    print("...")
    print(f"My name is {user_details['name']}. I am {user_details['age']} old and I reside in {user_details['city']}")
    
while True:
    more_names = input("Any more user names? Enter y or n.\n")

    if more_names == 'y':
        user_details = ask_questions_get_user()
        print_user_details(user_details)
    elif more_names == 'n':
        break
    else:
        print("Please enter y or n only.")
