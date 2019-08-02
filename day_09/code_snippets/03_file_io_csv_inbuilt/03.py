import csv

data = [
    ['character', 'strength', 'speed', 'overall'],
    ['naruto', '95', '95', '99'],
    ['itachi', '80', '85', '85'],
    ['kakashi', '80', '80', '75'],
    ['sakura', '90', '70', '75'],
]


# fp stands for file pointer
superhero_fp = open('03.csv', 'w')

writer = csv.writer(superhero_fp, delimiter=',')

for row in data:
    writer.writerow(row)

superhero_fp.close()
