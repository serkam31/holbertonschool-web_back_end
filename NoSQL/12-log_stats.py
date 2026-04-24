#!/usr/bin/env python3
"""Provide some stats about Nginx logs stored in MongoDB."""

from pymongo import MongoClient


def log_stats(mongo_collection):
    """Print stats about Nginx logs stored in MongoDB."""
    total = mongo_collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print("{total} logs".format(total=total))
    print("Methods:")
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print("\tmethod {method}: {count}".format(method=method, count=count))

    status_check_count = mongo_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print("{count} status check".format(count=status_check_count))


if __name__ == "__main__":
    client = MongoClient("mongodb://127.0.0.1:27017")
    log_stats(client.logs.nginx)
