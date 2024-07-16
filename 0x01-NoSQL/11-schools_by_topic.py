#!/usr/bin/env python3
'''Query schools by topic'''


def schools_by_topic(mongo_collection, topic):
    '''Returns documents in the collection that have topics'''
    return mongo_collection.find({"topics": {"$in": [topic]}})
