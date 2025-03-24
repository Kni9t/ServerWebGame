import pymongo

class db_controller:
    def __init__(self, address = "mongodb://192.168.1.13:27017/", dbname = "webgame"):
        self.client = pymongo.MongoClient(address)
        self.db = self.client[dbname]

    def write(self, collectionName, data):
        collection = self.db[collectionName]
        return collection.insert_one(data).inserted_id
    
    def find(self, collectionName, field = None, date = None):
        collection = self.db[collectionName]
        
        if (field is None or date is None ):
            return collection.find()
        else:
            return collection.find_one({field: date})