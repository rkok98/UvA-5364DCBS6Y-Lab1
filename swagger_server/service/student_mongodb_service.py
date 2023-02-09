import pymongo
from bson import ObjectId

conn_str = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn_str, serverSelectionTimeoutMS=5000)

student_db = client['student']
student_col = student_db["customers"]


def add(student=None):
    res = student_col.find_one({"first_name": student.first_name, "last_name": student.last_name})
    if res:
        return 'already exists', 409

    doc_id = student_col.insert_one(student.to_dict()).inserted_id
    return str(doc_id)


def get_by_id(student_id=None, subject=None):
    student = student_col.find_one({"_id": ObjectId(student_id)})
    if not student:
        return 'not found', 404
    student['student_id'] = student_id
    print(student)
    return student


def delete(student_id=None):
    student = student_col.find_one({"_id": ObjectId(student_id)})
    if not student:
        return 'not found', 404
    student_col.delete_one({"id": ObjectId(student_id)})
    return student_id
