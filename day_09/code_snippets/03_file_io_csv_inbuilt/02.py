data = [
    ['character', 'strength', 'speed', 'overall'],
    ['naruto', '95', '95', '99'],
    ['itachi', '80', '85', '85'],
    ['kakashi', '80', '80', '75'],
    ['sakura', '90', '70', '75'],
]


superhero_csv = open("02.csv", 'w')


row_iter = 0
cell_iter = 0

while row_iter < len(data):

    row_data = ",".join(data[row_iter])
    superhero_csv.write(row_data)
    superhero_csv.write('\n')
    row_iter += 1


superhero_csv.close()
