#!/usr/bin/env python3
"""function that changes all topics of a school document based
on the name"""


def update_topics(mongo_collection, name, topics):
    """returns updated document"""
    result = mongo_collection.replace_one(
            {"name": name},
            {
                "name": name,
                "topics": topics,
            })
    return result
