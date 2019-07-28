# no variable, forever running, exiting based on certain input


from pprint import pprint

student_list = []


while 1:
    user_input = input(
        "Do you want to enter any more student names?\nPlease input y or n.\n")

    if user_input == 'y':
        student_name = input("Please enter the student's name.\n")
        student_list.append(student_name)
    elif user_input == 'n':
        break
    else:
        print("Invalid. Please enter y or n only.")


print("The final list of students is as follows")
pprint(student_list)
