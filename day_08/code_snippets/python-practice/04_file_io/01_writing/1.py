# List of students line by line
students_list = ['aadithya', 'abhirath', 'david', 'franklin', 'ganesh']


# Open a file and explicitly specify that we intend to write
# fp stands for file pointer and it's a common convention to name fp
# even though the file doesn't exist it creates it for us.
fp = open('1.student_list.txt', 'w')

for student in students_list:
    fp.write(student+"\n")

# Be responsible
# Don't forget to close the file
fp.close()
