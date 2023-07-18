#!/usr/bin/env python3
"""python script that provides some stats on nginx
logs stored in mongodb"""


from pymongo import MongoClient


if __name__ == "__main__":
    """database: logs, collection: nginx"""

    client = MongoClient("mongodb://127.0.0.1:27017")
    logs = client.logs.nginx

    num_logs = logs.count_documents({})
    print(f'{num_logs} logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = logs.count_documents({"method": method})
        print(f'\tmethod {method}:{count}')

    status = logs.count_documents(
            {"method": "GET", "path": "/status"})
    print(f'{status} status check')
