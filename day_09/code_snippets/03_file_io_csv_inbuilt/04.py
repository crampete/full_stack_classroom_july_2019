import csv

data = [
    ['character', 'strength', 'speed', 'overall'],
    ['naruto', '95', '95', '99'],
    ['itachi', '80', '85', '85'],
    ['kakashi', '80', '80', '75'],
    ['sakura', '90', '70', '75'],
]


# fp stands for file pointer
superhero_fp = open('04.csv', 'w')

writer = csv.writer(superhero_fp, delimiter=',')

# writerows can write a list of rows.
# i.e a lists of lists
writer.writerows(data)

superhero_fp.close()
