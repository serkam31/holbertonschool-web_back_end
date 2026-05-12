# Pagination

Dataset pagination in Python: simple index-based pagination, hypermedia pagination with metadata, and deletion-resilient cursor pagination.

## Requirements

- Python 3.9 — Ubuntu 20.04 LTS
- pycodestyle 2.5
- Dataset: `Popular_Baby_Names.csv`

## Tasks

| # | File | Description |
| --- | --- | --- |
| 0 | `0-simple_helper_function.py` | `index_range` helper returning start/end tuple |
| 1 | `1-simple_pagination.py` | `Server` class with basic `get_page` method |
| 2 | `2-hypermedia_pagination.py` | `get_hyper` returning page data with navigation metadata |
| 3 | `3-hypermedia_del_pagination.py` | `get_hyper_index` resilient to row deletions |

## Usage

```bash
python3 0-main.py
python3 1-main.py
python3 2-main.py
python3 3-main.py
```

## Author

Holberton School — Web Back End
