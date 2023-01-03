import pymongo
from bson import ObjectId
from data import data

client = pymongo.MongoClient(
    "mongodb+srv://Ijass:1GJtifwT3dlOArP8@cluster0.u49gmjr.mongodb.net/?retryWrites=true&w=majority")
db = client["py"]  # database

users = db["users"]  # collection
candidates = db["candidates"]  # collection
comments = db["comments"]  # collection

# l = [
#     {"name": "balaji", "address": "pondy"},
#     {"name": "monika", "address": "london"},
#     {"name": "anbarasan", "address": "australia"},
#     {"name": "santhosh", "address": "london"},
#     {"name": "bharath", "address": "pondy"},
#     {"name": "ijass", "address": "pondy"},
#     {"name": "ragavan", "address": "australia"}
# ]

# users.insert_many(l)

# query = {"_id": ObjectId("63a07eb0ee99f1d1797d081b")}
# ftr = {"name": 0, "email": 0}
# ftr = {"name": 1}

# print(comments.find_one(query))
# comments.drop()

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


# id = input("plaese enter your id and check your details => ")


# query = {"_id" : ObjectId(id)}
# query = {"_id" : ObjectId("63a077f194b94248a0c6c0e6")}
query = {"address": "australia"}


for i in users.find(query):
    print(i)
# print(users.find(query))

# for i in users.find(query):
#     print(i)


# for i in users.find():
#     if(ObjectId(id) == i["_id"]):
#         print(i)
