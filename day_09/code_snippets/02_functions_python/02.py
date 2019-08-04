# write a function that takes a list and filters
# out all the odd numbers from it


def filter_even(list_of_numbers):
    new_list = []

    for number in list_of_numbers:
        if number % 2 == 0:
            new_list.append(number)

    return new_list


even_numbers = filter_even([1, 2, 3, 100, 243, 567])
print(even_numbers)

print(
    f"[2,3,7,10,15,8] filtering only the even numbers gives us {filter_even([2,3,7,10,15,8])}")
