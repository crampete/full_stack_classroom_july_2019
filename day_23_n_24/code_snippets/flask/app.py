from flask import Flask, render_template, request, jsonify
# we're using pymongo instead of Flask-PyMongo
from pymongo import MongoClient
from bson.json_util import dumps
from bson import ObjectId

client = MongoClient('mongodb://localhost:27017/')
student_app_db = client['student_db']

# variable need not be the same as collection name
xyz_collection = student_app_db['students']


app = Flask(__name__)


@app.route('/student', methods=['POST'])
def new_student():
    # get JSON as POST
    new_student_details = request.json
    print(new_student_details)

    xyz_collection.insert(new_student_details)
    return jsonify({"status": "sucess"}), 200


@app.route('/student', methods=["GET"])
def all_students():
    # get all students
    results = xyz_collection.find({})
    result_as_json = dumps(results)
    return result_as_json

# get particular student
@app.route('/student/<doc_id>', methods=["GET"])
def student_info(doc_id):
    result = xyz_collection.find_one({"_id": ObjectId(doc_id)})
    
    # CONVERTING MONGO OBJ TO JSON
    result["_id"] = str(result["_id"])
    return jsonify(result)


@app.route('/student/<doc_id>', methods=["PUT"])
def update_student():
    return


@app.route("/student/<doc_id>", methods=["DELETE"])
def delete_student():
    # normally they don't delete such critical documents
    # they have to follow legal guidelines
    # deleting flow is similar to GET
    # try it yourself :)
    return

# normally would be a query string but let's keep things simple
@app.route("/students/male", methods=["GET"])
def male_students():
    return


if __name__ == "__main__":
    app.run(debug=True)
