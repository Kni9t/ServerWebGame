import pymongo

class db_controller:
    def __init__(self, address = "mongodb://192.168.1.13:27017/", dbname = "webgame"):
        self.client = pymongo.MongoClient(address)
        self.db = self.client[dbname]

    def write(self, collectionName, data):
        collection = self.db[collectionName]
        return collection.insert_one(data).inserted_id
    
    def find(self, collectionName, field, date):
        collection = self.db[collectionName]
        return collection.find_one({field: date})