import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client['admin_Id_Pass']

collection = db['admin']

idPass = json.load(open("idPass.json","r"))


collection.insert_many(idPass)

print(client.list_database_names())
print(db.list_collection_names())
