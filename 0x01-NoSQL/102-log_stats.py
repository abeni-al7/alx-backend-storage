#!/usr/bin/env python3
'''Provides stats about Nginx Logs stored in mongoDB'''
from pymongo import MongoClient

if __name__ == '__main__':
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    collection = db.nginx

    nb_of_docs = collection.count_documents({})
    get_count = collection.count_documents({"method": "GET"})
    post_count = collection.count_documents({"method": "POST"})
    put_count = collection.count_documents({"method": "PUT"})
    patch_count = collection.count_documents({"method": "PATCH"})
    delete_count = collection.count_documents({"method": "DELETE"})
    status_count = collection.count_documents({"method": "GET", "path": "/status"})

    pipeline = [
        {
            '$group': {
                '_id': '$ip',
                'count': {'$sum': 1}
            }
        },
        {
            '$sort': {
                'count': -1
            }
        },
        {
            '$limit': 10
        }
    ]
    top_ips = list(collection.aggregate(pipeline))

    print(f"{nb_of_docs} logs")
    print("Methods:")
    print(f"\tmethod GET: {get_count}")
    print(f"\tmethod POST: {post_count}")
    print(f"\tmethod PUT: {put_count}")
    print(f"\tmethod PATCH: {patch_count}")
    print(f"\tmethod DELETE: {delete_count}")
    print(f"{status_count} status check")
    print("IPs:")
    for ip in top_ips:
        print('\t{}: {}'.format(ip.get('_id'), ip.get('count')))
