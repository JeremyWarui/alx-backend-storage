#!/usr/bin/env python3
"""function that returrns the list of school having
specific topic"""


def schools_by_topic(mongo_collection, topic):
    """returns list of schools"""
    found_docs = mongo_collection.find({"topics": topic})
    list_docs = [i for i in found_docs]
    return list_docs
