#!/usr/bin/env python3
"""
Defines a function that changes
all topics of a school document based on the name
"""
from pymongo import MongoClient
from typing import List


def update_topics(mongo_collection: MongoClient,
                  name: str, topics: List[str]) -> str:
    """
    Updates all topics of a school document based on the name
    Args:
        mongo_collection: a collection object from a mongoDB database
        name (str): school name to update
        topics (List(str)): list of topics approached in the school
    Returns:
        None
    """
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
