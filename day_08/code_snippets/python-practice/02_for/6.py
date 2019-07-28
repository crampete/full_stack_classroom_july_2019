laptop_ratings = {
    'tumshung': 4,
    'tenodo': 5,
    'lobiba': 4,
    'roni': 4,
    'maple': 5
}

for laptop in laptop_ratings.keys():
    print(f"{laptop} has a rating of {laptop_ratings[laptop]}")

print('----------Method 2----------')

for laptop, rating in laptop_ratings.items():
    print(f"{laptop} has a rating of {rating}")