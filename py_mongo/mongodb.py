import pymongo
from bson import ObjectId

client = pymongo.MongoClient("mongodb+srv://Ijass:1GJtifwT3dlOArP8@cluster0.u49gmjr.mongodb.net/?retryWrites=true&w=majority")
db = client["py"] #database

users = db["users"] #collection
candidates = db["candidates"] #collection


# data = [
#     {"name": "balaji"},
#     {"name": "xxx"},
#     {"name": "aaa"},
# ]

# insert_one

# users.insert_one({"id": "yudhg7456dh","name": "anbu"})


# insert_many

# candidates.insert_many(data)


#  find_one (read)

# print(users.find_one())

# print(users.find())


id = input("plaese enter your id and check your details => ")


for i in users.find():
    if(ObjectId(id) == i["_id"]):
        print(i)