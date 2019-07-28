arbitrary_string = "python"

iterator = 0  # string indices start from 0


new_reversed_string = ''
while iterator < len(arbitrary_string):
    new_reversed_string = arbitrary_string[iterator] + new_reversed_string
    iterator += 1

print(new_reversed_string)
