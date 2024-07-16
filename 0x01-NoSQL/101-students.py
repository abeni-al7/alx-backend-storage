#!/usr/bin/env python3
'''A module for sorting students by their score from a collection'''


def top_students(mongo_collection):
    '''Returns the collection after sorting it by average score'''
    pipeline = [
        {
            '$addFields': {
                'averageScore': {
                    '$avg': '$topics.score'
                    }
                }
        },
        {
            '$sort': {
                'averageScore': -1
            }
        }]
    return list(mongo_collection.aggregate(pipeline))
