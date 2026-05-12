# Python Variable Annotations

## Introduction
Les **annotations de variables** permettent d'indiquer le **type** d'une variable en Python. Python reste flexible (pas d'erreur si tu mets le mauvais type), mais les annotations servent de **documentation** et permettent à des outils de détecter des erreurs.

**Pourquoi on l'apprend ?** Pour écrire du code plus lisible, maintenable, et détecter des bugs plus tôt.

---

## Concepts clés

### Annoter une variable
```python
name: str = "Alice"
age: int = 20
score: float = 9.5
is_active: bool = True
```

### Annoter les paramètres et retours d'une fonction
```python
def greet(name: str) -> str:
    return f"Bonjour {name}"
```

### Types complexes avec `typing`
```python
from typing import List, Dict, Tuple, Optional

def get_students() -> List[str]:
    return ["Alice", "Bob"]

def get_info() -> Dict[str, int]:
    return {"age": 20}

def find_user(id: int) -> Optional[str]:
    # peut retourner str ou None
    return None
```

### `mypy` — vérifier les types
```bash
pip install mypy
mypy mon_fichier.py
```

---

## Résumé

| Concept | Utilité |
|---|---|
| `variable: type` | Annoter une variable |
| `def f(x: int) -> str` | Annoter une fonction |
| `List`, `Dict`, `Optional` | Types complexes |
| `mypy` | Vérifier les types statiquement |
