import pymongo as pm

# mongo client
client = pm.MongoClient("mongodb+srv://arpitparekh9:TSBJ021KM8KG0Teu@googleclundcluster.2kkxh.mongodb.net/")

# database
db = client["bascom"]

# collection
collection = db["students"]

# fetch all data
data = collection.find()

for i in data:
  print(i)
