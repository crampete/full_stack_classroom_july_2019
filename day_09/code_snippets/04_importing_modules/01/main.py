from even import is_divisible_by_3_5_7, is_even

check_numbers = [45, 2345, 56, 105]

for number in check_numbers:
    result = is_even(number)
    if result == True:
        print(f"{number} is even.")
    else:
        print(f"{number} is ood.")

for number in check_numbers:
    result = is_divisible_by_3_5_7(number)

    if result:
        print(f"{number} is divisible by 3, 5 and 7.")
    else:
        print(f"{number} is NOT divisible by 3, 5 and 7.")
