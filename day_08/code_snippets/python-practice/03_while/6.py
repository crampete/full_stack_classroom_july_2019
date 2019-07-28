# how many odd numbers are required to reach a particular sum

required_sum = int(input("Enter your desired sum.\n"))


accumulated_sum = 0
number_iterator = 1
odd_number_count = 0

while accumulated_sum < required_sum:
    # if it is an odd number
    if number_iterator % 2 == 1:
        accumulated_sum += number_iterator
        odd_number_count += 1

    number_iterator += 1


print(f"The required number of odd number are {odd_number_count}")
