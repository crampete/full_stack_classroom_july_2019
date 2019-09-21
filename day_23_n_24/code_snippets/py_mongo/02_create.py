from pymongo import MongoClient
import datetime

client = MongoClient('mongodb://localhost:27017/')


# same as the name of the database you make.
student_db = client['student_db']

# list all the collections
student_db.list_collection_names()

# we reference a collection in a Python variable
# this can be used to manipulate and make changes to the collection
student_collection = student_db['students']

# inserting one student
student_collection.insert({
    'name': "Karthik Raja",
    'place': "Chennai",
    'pincode': "600040",
    "phone_number": "9999999999"
})


# inserting many students using a list
students_to_be_inserted = [
    {'name': 'sachin', 'place': 'Chennai', 'pincode': '600040'},
    {'name': 'rupesh', 'place': "Chennai", 'pincode': '600101'},
    {'name': 'jagan', 'place': 'Chennai', 'pincode': '600050'}
]
student_collection.insert(students_to_be_inserted)
