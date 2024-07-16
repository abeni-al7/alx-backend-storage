#!/usr/bin/env python3
'''Provides stats about Nginx Logs stored in mongoDB'''
from pymongo import MongoClient


# connect to the database
client = MongoClient('mongodb://127.0.0.1:27017')

# get the database
db = client.logs

#get the collection
collection = db.nginx
# get the number of documents
nb_of_docs = collection.count_documents({})
get_count = collection.count_documents({"method": "GET"})
post_count = collection.count_documents({"method": "POST"})
put_count = collection.count_documents({"method": "PUT"})
patch_count = collection.count_documents({"method": "PATCH"})
delete_count = collection.count_documents({"method": "DELETE"})
get_and_status_count = collection.count_documents({"method": "GET", "path": "/status"})

print(f"{nb_of_docs} logs")
print("Methods:")
print(f"\tmethod GET: {get_count}")
print(f"\tmethod POST: {post_count}")
print(f"\tmethod PUT: {put_count}")
print(f"\tmethod PATCH: {patch_count}")
print(f"\tmethod DELETE: {delete_count}")
print(f"{get_and_status_count} status check")
