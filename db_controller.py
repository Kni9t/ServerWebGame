import pymongo
import sys

class DBController:
    def __init__(self, address = "mongodb://localhost:27017/", dbname = "webgame"):
        self.client = pymongo.MongoClient(address)
        self.db = self.client[dbname]
        
        if ('params' not in self.db.list_collection_names()):
            raise SystemError('Collection "params" with system settings not found')

    def write(self, collectionName, data):
        collection = self.db[collectionName]
        return collection.insert_one(data).inserted_id
    
    def find(self, collectionName, field = None, date = None):
        collection = self.db[collectionName]
        
        if (field is None or date is None ):
            return collection.find()
        else:
            return collection.find_one({field: date})