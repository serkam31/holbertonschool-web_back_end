# Python Variable Annotations

Type annotations in Python using built-in types and the `typing` module, with static type checking via `mypy`.

## Requirements

- Python 3.9 — Ubuntu 20.04 LTS
- pycodestyle 2.5
- mypy (`pip install mypy`)

## Tasks

| # | File | Description |
| --- | --- | --- |
| 0 | `0-add.py` | Annotate a function that adds two floats |
| 1 | `1-concat.py` | Annotate a string concatenation function |
| 2 | `2-floor.py` | Annotate a floor function returning `int` |
| 3 | `3-to_str.py` | Annotate a float-to-string conversion |
| 4 | `4-define_variables.py` | Annotate module-level variables |
| 5 | `5-sum_list.py` | Annotate a function using `List[float]` |
| 6 | `6-sum_mixed_list.py` | Annotate with `Union[int, float]` |
| 7 | `7-to_kv.py` | Annotate with `Tuple[str, float]` |
| 8 | `8-make_multiplier.py` | Annotate a higher-order function with `Callable` |
| 9 | `9-element_length.py` | Annotate with `Iterable`, `Sequence`, `List`, `Tuple` |

## Usage

```bash
# Run a task
python3 0-add.py

# Type check with mypy
mypy 0-add.py
```

## Author

Holberton School — Web Back End
