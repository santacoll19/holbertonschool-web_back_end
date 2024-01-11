#!/usr/bin/env python3
"""insert a document in Python"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """insert a document in Python"""
    if mongo_collection is not None:
        return mongo_collection.insert_one(kwargs).inserted_id
    return None
