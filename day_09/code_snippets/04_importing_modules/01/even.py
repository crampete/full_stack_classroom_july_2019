def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def is_divisible_by_3_5_7(number):
    return (number % 3 == 0 and number % 5 == 0 and number % 7 == 0)
