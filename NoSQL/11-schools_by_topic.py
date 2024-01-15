#!/usr/bin/env python3
"""
returns the list of school having a specific topic
topics (list of string): will be the list of topic searched
mongo_collection will be the pymongo collection object
"""
import pymongo
from typing import List


def schools_by_topic(mongo_collection: pymongo.collection, topic: str) -> List:
    """
    returns the list of school having a specific topic
    topics (list of string): will be the list of topic searched
    mongo_collection will be the pymongo collection object
    """
    return mongo_collection.find({"topics": topic})
