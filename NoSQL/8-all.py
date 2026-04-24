#!/usr/bin/env python3
"""Lists all documents in a collection"""


def list_all(mongo_collection):
    """ list_all - lists all documents in a collection
    Args:
        mongo_collection: the pymongo collection object
    Returns:
        list of all documents in the collection
    """
    return mongo_collection.find()
