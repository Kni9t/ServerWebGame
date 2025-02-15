import pymongo
import json
import DBcontroller as DBcontroller

bufJson = {
    'name': "1234656",
    'email': "123@mail.ru",
    'password': "11111"
    }

#myclient = pymongo.MongoClient("mongodb://192.168.1.13:27017/")
#db = myclient["webgame"]
#collection = db["users"]

DBC = DBcontroller.db_controller()

#x = collection.insert_one(bufJson)
print (DBC.read("users"))
#print(x)

exit(0)