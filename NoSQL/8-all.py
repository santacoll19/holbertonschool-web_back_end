#!/usr/bin/env python3
"""list all documents with python in documents collection"""
import pymongo


def list_all(mongo_collection):
    """"list all documents in a collection"""
    if mongo_collection is not None:
        document = mongo_collection.find()
        return list(document) if document else []
    return []
