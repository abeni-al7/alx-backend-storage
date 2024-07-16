#!/usr/bin/env python3
'''A module for inserting a new document into a collection'''


def insert_school(mongo_collection, **kwargs):
    '''Inserts a document into database and returns the id'''
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
    