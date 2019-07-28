# if else

dividend = int(input("Please enter a number between 1 and 1000.\n"))
check_divisibility_by = int(input("Please enter a number between 1 and 10.\n"))

# check if the remainder is 0 or not
if dividend % check_divisibility_by == 0:
    # remainder is 0, therefore it is divisible
    print(f"{dividend} is divisible by {check_divisibility_by}.")
else:
    # remainder isn't zero, therefore it isn't divisible
    print(f"{dividend} is not divisible by {check_divisibility_by}.")
