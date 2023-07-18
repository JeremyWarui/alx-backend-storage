#!/usr/bin/env python3
"""function that inserts a new document in a collection"""


def insert_school(mongo_collection, **kwargs):
    """returns a new id of the added items"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
