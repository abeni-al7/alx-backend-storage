#!/usr/bin/env python3
'''A module for listing all documents in a collection'''


def list_all(mongo_collection):
    '''Returns a list of all documents from mongo_collection'''
    documents = list(mongo_collection.find())
    return documents
