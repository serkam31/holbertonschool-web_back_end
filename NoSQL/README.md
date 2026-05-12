# NoSQL

Introduction to MongoDB: shell commands, CRUD operations, and Python integration with PyMongo.

## Requirements

- MongoDB 4.4 — Ubuntu 20.04 LTS
- Python 3.9
- PyMongo 4.x (`pip install pymongo`)
- pycodestyle 2.5

## Setup

```bash
# Install MongoDB
sudo apt-get install -y mongodb

# Install PyMongo
pip install pymongo
```

## Tasks

| # | File | Description |
| --- | --- | --- |
| 0 | `0-list_databases` | List all databases |
| 1 | `1-use_or_create_database` | Create or select a database |
| 2 | `2-insert` | Insert a document into a collection |
| 3 | `3-all` | List all documents in a collection |
| 4 | `4-match` | Find documents matching a field |
| 5 | `5-count` | Count documents in a collection |
| 6 | `6-update` | Add a field to matching documents |
| 7 | `7-delete` | Delete matching documents |
| 8 | `8-all.py` | Python — list all documents |
| 9 | `9-insert_school.py` | Python — insert a document, return `_id` |
| 10 | `10-update_topics.py` | Python — update topics by school name |
| 11 | `11-schools_by_topic.py` | Python — find schools by topic |
| 12 | `12-log_stats.py` | Python — display Nginx log statistics |

## Usage

```bash
# Run a MongoDB script
mongo < 0-list_databases

# Run a Python script
python3 12-log_stats.py
```

## Author

Holberton School — Web Back End
