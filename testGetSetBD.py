import pymongo
import json

bufJson = {
    '2name': "1234656",
    'email': "123@mail.ru",
    'password': "11111"
    }

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
db = myclient["webgame"]
collection = db["users"]

x = collection.insert_one(bufJson)
#print (collection.find_one())

exit(0)