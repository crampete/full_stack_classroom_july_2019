data = [
    ['character', 'strength', 'speed', 'overall'],
    ['naruto', '95', '95', '99'],
    ['itachi', '80', '85', '85'],
    ['kakashi', '80', '80', '75'],
    ['sakura', '90', '70', '75'],
]


superhero_csv = open("01.csv", 'w')


row_iter = 0
cell_iter = 0

while row_iter < len(data):
    cell_iter = 0
    while cell_iter < len(data[row_iter]):
        superhero_csv.write(data[row_iter][cell_iter])

        if cell_iter != len(data[row_iter]) - 1:
            superhero_csv.write(',')

        cell_iter += 1

    superhero_csv.write('\n')
    row_iter += 1


superhero_csv.close()
