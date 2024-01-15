#!/usr/bin/env python3
"""
Python script that provides some stats about Nginx logs stored in MongoDB
Database: logs, Collection: nginx
Display:
    first line: x logs where x is the number of documents in this collection
    second line: Methods:
        5 lines with the number of documents with the method = ["GET",
        "POST", "PUT", "PATCH", "DELETE"] in this order (see example below -
        warning: it’s a tabulation before each line)
    one line with the number of documents with:
        method=GET
        path=/status
"""
from pymongo import MongoClient


def log_stats():
    """ provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://localhost:27017')
    db = client.logs
    logs_collection = db.nginx
    total = logs_collection.count_documents({})
    print("{} logs".format(total))
    
    print('Methods:')
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = logs_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')
    count = logs_collection.count_documents({"method": "GET", "path": "/status"})
    print(f'{count} status check')
