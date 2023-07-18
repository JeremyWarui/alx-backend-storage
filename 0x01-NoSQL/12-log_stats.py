#!/usr/bin/env python3
"""python script that provides some stats on nginx
logs stored in mongodb"""


from pymongo import MongoClient


def count_logs(a: dict) -> int:
    """returns number of logs"""
    client = MongoClient("mongodb://127.0.0.1:27017")
    logs = client.logs.nginx
    return logs.count_documents(a)

if __name__ == "__main__":
    """database: logs, collection: nginx"""

    print(f"{count_logs({})} logs")
    print("Methods:")
    print(f"\tmethod GET: {count_logs({'method': 'GET'})}")
    print(f"\tmethod POST: {count_logs({'method': 'POST'})}")
    print(f"\tmethod PUT: {count_logs({'method': 'PUT'})}")
    print(f"\tmethod PATCH: {count_logs({'method': 'PATCH'})}")
    print(f"\tmethod DELETE: {count_logs({'method': 'DELETE'})}")
    print(f"{count_logs({'method': 'GET', 'path': '/status'})} status check")
