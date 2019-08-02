def filter_even(list_of_numbers):
    new_list = []

    for number in list_of_numbers:
        if number % 2 == 0:
            new_list.append(number)

    return new_list


print(
    f"[2,3,7,10,15,8] filtering only the even numbers gives us {filter_even([2,3,7,10,15,8])}")
