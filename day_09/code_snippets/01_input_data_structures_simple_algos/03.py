rows_of_students = [
    ['alan', 'joshiba', 'ramya', 'sangeetha'], 
    ['kishore', 'arivuselvan', 'jegan', 'syed', 'anand', 'ashwin', 'sachin', 'edwin'], 
    ['sumaya', 'likitha', 'meena', 'abirami', 'kokila']
]

for row in rows_of_students:
    for student in row:
        print(student, end=" ")

    print("")