#!/usr/bin/env python3
""" 
list all documents in a collection
mongo_collection will be the pymongo collection object
return empty list if no document
"""
import pymongo
from typing import List


def list_all(mongo_collection: pymongo.collection) -> List:
    """ 
    list all documents in a collection
    return empty list if no document
    """
    return mongo_collection.find()

