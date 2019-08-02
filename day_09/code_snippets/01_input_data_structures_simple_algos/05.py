laptop_mapping = {
    'boobalan': 'hp',
    'sadam': 'lenovo',
    'siraj': 'sony',
    'mohan': 'toshiba'
}


for key, value in laptop_mapping.items():
    print(f"{key} uses a {value} laptop.")


print("\n\nMethod 2\n\n")
    
for key in laptop_mapping.keys():
    print(f"{key} uses a {laptop_mapping[key]} laptop.")