#!/usr/bin/env python3
"""Function that lists all documents in mongo collection"""


def list_all(mongo_collection):
    """returns a list of all documents or empty list"""
    list = []
    if mongo_collection is not None:
        return mongo_collection.find()
    return list
