desirable_numbers_seen_so_far = 0
iterator = 0
while desirable_numbers_seen_so_far < 20:
    if iterator % 2 == 1 and iterator % 3 == 0:
        print(f"Encountered {iterator}")
        print(iterator * iterator)
        desirable_numbers_seen_so_far += 1

    iterator += 1