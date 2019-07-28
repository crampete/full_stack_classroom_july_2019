# desired sum starts with 0
desired_sum = 0

# a varible which helps keep track how far we've progressed
iterator = 1


while iterator < 21:
    desired_sum += iterator * iterator
    # we have to keep track and maintain iterator
    # had we used a for loop we wouldn't have to do this
    iterator += 1
