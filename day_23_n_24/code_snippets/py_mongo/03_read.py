from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')


# same as the name of the database you make.
student_db = client['student_db']

# list all the collections
student_db.list_collection_names()

# we reference a collection in a Python variable
# this can be used to manipulate and make changes to the collection
student_collection = student_db['students']


# find the student with the name jagan
print("\n\nSingle Result\n\n")
result = student_collection.find_one({"name": "jagan"})
print(result)


print("\n\nMultiple Results\n\n")
# multiple results
results = student_collection.find({'name': 'Karthik Raja'})

for result in results:
    print(result)
