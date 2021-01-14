from helpers.success_response import success_resp
from helpers.error_response import error_resp
from helpers.db import db_connect
from pymongo import ReturnDocument
from bson.objectid import ObjectId


def just_hello(request):
    my_text = {
        "message": "Hello"
    }
    return success_resp(my_text)


def create_user(request):
    try:
        db_conn = db_connect()
        db = db_conn['users']  # * Database Name
        user_instance = db['users']  # * Collection Name
        name = request['name']
        email = request['email']

        db_result = user_instance.insert_one({
            'name': name,
            'email': email
        })

        return success_resp('inserted successfully')

    except Exception as error:
        return error_resp(error)


def get_all(request):
    try:
        db_conn = db_connect()
        db = db_conn['users']
        user_instance = db['users']

        parsed_result = []

        db_result = user_instance.find({}, {'_id': False})

        for documents in db_result:
            parsed_result.append(documents)
        print(f'the output is {parsed_result}')
        return success_resp(parsed_result)
    except Exception as error:
        return error_resp(error)


def get_one(request):
    try:
        db_conn = db_connect()
        db = db_conn['users']
        user_instance = db['users']

        print(request)

        db_result = user_instance.find_one(
            {'_id': ObjectId(id)}, {'_id': False}
        )

        return success_resp(request)
    except Exception as error:
        return error_resp(error)


def edit_user(request):
    return 'hello'


def delete_user(request):
    return 'hello'
