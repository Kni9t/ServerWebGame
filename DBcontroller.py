import pymongo

DBNAME = "webgame"
USERCOLLECTION = "users"

#collection = db["users"]

class db_controller:
    def __init__(self, address = "mongodb://192.168.1.13:27017/"):
        self.client = pymongo.MongoClient(address)
        self.db = self.client[DBNAME]

    def write(self, collectionName, data):
        collection = self.db[collectionName]
        return collection.insert_one(data).inserted_id
    
    def read(self, collectionName, id = None):
        collection = self.db[collectionName]
        collection.find_one({"_id": id})
        return collection.find_one({"_id": id})