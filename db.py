
from pymongo import MongoClient

mongo_client = MongoClient("mongodb+srv://task_manager:task_manager@cluster0.hnlcf87.mongodb.net/")

# Access database
task_manager_db = mongo_client["task_manager_db"]

# Pick a collection to operate on
tasks = task_manager_db["tasks"]