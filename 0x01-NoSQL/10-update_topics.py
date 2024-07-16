#!/usr/bin/env python3
'''A module for updating documents in a collection'''


def update_topics(mongo_collection, name, topics):
    '''Updates a collection with topics querying by name'''
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
