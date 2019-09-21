from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')


# same as the name of the database you make.
student_db = client['student_db']

# list all the collections
student_db.list_collection_names()

# we reference a collection in a Python variable
# this can be used to manipulate and make changes to the collection
student_collection = student_db['students']
