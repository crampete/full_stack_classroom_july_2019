side = int(input(
    "How long should the square be? Please enter a number between 2 and 10.\n"))


for row in range(side):
    for column in range(side):
        print("*", end='')

    print('')
