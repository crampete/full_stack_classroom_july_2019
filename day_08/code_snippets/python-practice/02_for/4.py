desired_sum = 0

for number_iter in range(501):
    if number_iter % 3 == 0 and number_iter % 5 != 0:
        desired_sum += number_iter

print(desired_sum)
