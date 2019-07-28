first_names = [
    'Raghu',
    'Vikram',
    'John',
    'Priya',
    'Kannan'
]

last_names = [
    'Srinivasan',
    'Johnson'
]

for f_name in first_names:
    for l_name in last_names:
        print(f"{f_name} {l_name}")

print('===== Method 2 =====')

for l_name in last_names:
    for f_name in first_names:
        print(f"{f_name} {l_name}")