# reading billing entry line by line
fp = open('2.billing_entry.txt', 'r')


# keep doing it until we break
while True:

    # To hold each bill until we process them
    four_lines = []

    # read 4 lines everytime
    for i in range(4):
        line = fp.readline()

        # reached the end of file
        # break
        if line == '':
            break

        # line has a newline character at the end
        # so we get rid of it before appending
        # it to our temporary list
        four_lines.append(line.rstrip())

    if len(four_lines) == 4:
        print(f"Customer Name:- {four_lines[0]}")
        print(f"Amount Spent:- {four_lines[1]}")
        print(f"Cart:- {four_lines[2]}")
        print(f"Date:- {four_lines[3]}\n")
    else:
        # encountered missing entry or we're at the end
        break


fp.close()
