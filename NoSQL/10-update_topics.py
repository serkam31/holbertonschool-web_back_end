#!/usr/bin/env python3
""" 10-update_topics """


def update_topics(mongo_collection, name, topics):
    """ update_topics - changes all topics of a school document based on the name
    Args:
        mongo_collection: the pymongo collection object
        name: the name of the school to update
        topics: the list of topics approached in the school
    Returns:
        the number of documents updated
    """
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result.modified_count
