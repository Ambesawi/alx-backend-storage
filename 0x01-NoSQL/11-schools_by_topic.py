#!/usr/bin/env python3
"""
Defines a function that returns the list of school having a specific topic
"""
from typing import List
from pymongo import MongoClient


def schools_by_topic(mongo_collection: MongoClient,
                     topic: str) -> List[object]:
    """
    Llist of school having a specific topic
    Args:
        mongo_collection: a collection object from a mongoDB database
        topic (str): topic to be searched
    Returns:
        List of documents or an empty list
    """
    return mongo_collection.find({"topics": topic})
