# remove vowels from a string

arbitrary_string = "Laptops and mobile phones have changed the world."

new_string = ""
for char in arbitrary_string:
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        continue
    else:
        new_string += char


print(new_string)
