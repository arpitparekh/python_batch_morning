import pymongo as pm

client = pm.MongoClient("mongodb://localhost:27017/")

# database
db = client["bascom"]

# collection
collection = db["students"]

# fetch all data
data = collection.find()

for i in data:
  print(i)
