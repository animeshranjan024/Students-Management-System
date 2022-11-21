import pymongo
import json

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client["Students_2018"]

collection1 = db['CSE']

collection2 = db['EEE']

collection3 = db["ME"]

collection4 = db["CE"]

showdbs = client.list_database_names()

print(showdbs)

cse = json.load(open("CSE.json","r"))

eee = json.load(open("EEE.json","r"))

me = json.load(open("Mech.json","r"))

ce = json.load(open("Civil.json","r"))


collection1.insert_many(cse)

collection2.insert_many(eee)

collection3.insert_many(me)

collection4.insert_many(ce)

showcollections = db.list_collection_names()

print(showcollections)