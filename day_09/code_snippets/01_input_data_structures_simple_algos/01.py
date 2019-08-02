# collect 10 integers from the user
# store them in a list
# create a new list with only the integers larger than 10


user_input_store = []
for iteration in range(10):
    number_by_user = int(input("Please enter a number.\n"))
    user_input_store.append(number_by_user)


new_list_filtered = []

for number in user_input_store:
    if number > 10:
        new_list_filtered.append(number)

print("List with all numbers larger than 10 :- ", new_list_filtered)