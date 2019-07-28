# declare a list of arbitrary students against which we check
students_in_my_class = ["kishore", "balaji", "modi", "obama"]

# prompt the user for his name
user_entered_name = input("Please enter your name\n")

if user_entered_name not in students_in_my_class:
    print(f"Please leave the class. {user_entered_name} is not my student.")
else:
    print(f"{user_entered_name} is my student. Marking your attendance.")
