#!/usr/bin/env python3
""" 9-insert_school """


def insert_school(mongo_collection, **kwargs):
    """ insert_school - inserts a new document in a collection
    Args:
        mongo_collection: the pymongo collection object
        kwargs: keyword arguments representing the document to insert
    Returns:
        the new _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
