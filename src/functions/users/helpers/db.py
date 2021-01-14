from pymongo import MongoClient, collection
import pymongo
import os


def db_connect():
    try:
        conn_string = os.environ['db_conn']
        db_conn = MongoClient(conn_string)
        return db_conn
    except pymongo.errors.ConnectionFailure as error:
        print("Failed to connect to server", error)
