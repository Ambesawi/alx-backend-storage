#!/usr/bin/env python3
"""
Defines a function that returns all students sorted by average score
"""
from typing import Iterator
from pymongo import MongoClient


def top_students(mongo_collection: MongoClient) -> Iterator:
    """
    A function that returns all students sorted by average score
    Args:
        mongo_collection : a collection object from a mongoDB database
    Returns:
        []: if there are no documents in the collection
        Iterator: contains documents in the collection
    """
    return mongo_collection.aggregate([
        {'$addFields': {'averageScore': {'$avg': "$topics.score"}}},
        {'$sort': {'averageScore': -1}}
    ])
