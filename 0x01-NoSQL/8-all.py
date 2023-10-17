#!/usr/bin/env python3
"""
Defines a function that lists all documents in a collection
"""
from pymongo import MongoClient
from typing import Iterator


def list_all(mongo_collection: MongoClient) -> Iterator:
    """
    Lists all documents in a collection
    Args:
        mongo_collection: a collection object from a mongoDB database
    Returns:
        []: if there are no documents in the collection
        Iterator: contains documents in the collection
    """
    if mongo_collection.count() == 0:
        return []
    return mongo_collection.find()
