import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://cjdewitt:d8ZpfzggeDVYvHMO@uni-swap.hy9bzs8.mongodb.net/?retryWrites=true&w=majority")
db = cluster["uni-swap"]
collection = db["users"]


post = {"_id": 1, "name": "Cory", "email": "cjdewitt@usc.edu"} 



collection.insert_one(post)


