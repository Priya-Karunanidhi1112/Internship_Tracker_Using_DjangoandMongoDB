from pymongo import MongoClient
con = MongoClient('mongodb://localhost:27017/')
db = con['crud'] # Connects to "crud" database
col = db['intern'] # Uses the "data" collection
print("connect") # Just confirms connection
#install - pymongo, pip install pymongo