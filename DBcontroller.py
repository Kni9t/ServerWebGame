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
        return collection.insert_one(data)
    
    def read(self, collectionName, id = None):
        collection = self.db[collectionName]
        bufList = []
        for item in collection.find():
            bufList.append(item)
        return bufList