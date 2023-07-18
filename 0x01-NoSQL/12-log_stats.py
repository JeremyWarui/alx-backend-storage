#!/usr/bin/env python3
"""python script that provides some stats on nginx
logs stored in mongodb"""


from pymongo import MongoClient


if __name__ == "__main__":
    """database: logs, collection: nginx"""

    client = MongoClient(host="localhost", port=27017)
    nginx_coll = client.logs.nginx

    num_logs = nginx_coll.count_documents({})
    print("{} logs".format(num_logs))

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_coll.count_documents({"method": method})
        print("\tmethod {}:{}".format(method, count))

    status = nginx_coll.count_documents(
            {"method": "GET", "path": "/status"})
    print("{} status check".format(status))
