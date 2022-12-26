import os
import pymongo
import certifi

from Automl.Logging.logs import logging

db_url = os.environ['MONGO_DB_URL']


class Mongo:
    DEFAULT_CONNECTION_URL = db_url
    """
    Mongo class is for storing csv files.
    """
    def __init__(self, db_name: str, collection_name: str):
        """
        intializing the database
        Args:
            db_name: name of the database
            collection_name: name of collection in database
        """
        self.database_name = db_name
        self.collection = collection_name

    def connect_database(self):
        """
        establish the connection with database
        Returns:
            collections
        """
        try:
            mongo_cloud = pymongo.MongoClient(Mongo.DEFAULT_CONNECTION_URL, tlsCAFile=certifi.where())
            mongo_db = mongo_cloud[self.database_name]
            collection = mongo_db[self.collection]
            return collection
        except Exception as e:
            print(e)

    def insert_many(self, records):
        """
        inserts many documents
        Args:
            records: files or documents to insert

        Returns: str

        """
        try:
            collection = self.connect_database()
            collection.insert_many(records)
            return True
        except Exception as e:
            print(e)

    def delete_all(self):
        """
        deletes all the records present in the collections
        Returns:
            str
        """
        try:
            collection = self.connect_database()
            collection.delete_many({})
            return "Deleted documents"
        except Exception as e:
            print(e)
