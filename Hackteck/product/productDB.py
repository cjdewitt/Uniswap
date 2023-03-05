import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://cjdewitt:d8ZpfzggeDVYvHMO@uni-swap.hy9bzs8.mongodb.net/?retryWrites=true&w=majority")
db = cluster["uni-swap"]
collection = db["Products"]

post = {"_id": 1, "name": "Nike Air Max Penney", "price": 125, "Decription": "Size: 9.5 Premium basketball sneakers"}

collection.insert_one(post)

