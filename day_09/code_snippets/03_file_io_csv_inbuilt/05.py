import csv

data = [
    ['character', 'strength', 'speed', 'overall'],
    ['naruto', '95', '95', '99'],
    ['itachi', '80', '85', '85'],
    ['kakashi', '80', '80', '75'],
    ['sakura', '90', '70', '75'],
]


def write_csv(file_name, data):
    fp = open(file_name, 'w')
    writer = csv.writer(fp, delimiter=',')
    writer.writerows(data)
    fp.close()


write_csv("05_01.csv", data)
write_csv("05_02.csv", data)
