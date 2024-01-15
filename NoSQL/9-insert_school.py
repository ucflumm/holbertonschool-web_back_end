#!/usr/bin/env python3
"""
insert a document in a collection based on kwargs
mongo_collection will be the pymongo collection object
returns the new _id
"""
import pymongo
from typing import List


def insert_school(mongo_collection: pymongo.collection, **kwargs) -> str:
    """
    insert a document in a collection based on kwargs
    returns the new _id
    """
    return mongo_collection.insert_one(kwargs).inserted_id
