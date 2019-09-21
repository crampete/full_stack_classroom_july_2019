from db import student_collection
from bson.objectid import ObjectId


# print(student_collection.find_one({'name': "Karthik Raja"}))


# update one using unique id

student_collection.update(

    {
        '_id': ObjectId('5d847060f1eead571ae0e7bb')
    },
    {
        "$set": {
            'place': 'bangalore'
        }
    },
    upsert=False)

# update many using a filter

student_collection.update(
    {
        "place": "Chennai"
    },
    {
        "$set": {
            'place': "Karur"
        }
    },
    upsert=False,
    multi=True
)
