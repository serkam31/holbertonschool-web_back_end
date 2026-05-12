# Cours complet — Python Variable Annotations

---

# PARTIE 1 — THÉORIE

---

## 1. Qu'est-ce que les annotations de types ?

Python est un langage à **typage dynamique** : une variable peut contenir n'importe quel type de valeur et ça peut changer. C'est flexible mais ça peut créer des bugs difficiles à trouver.

Les annotations de types ajoutent des **indications** sur le type attendu — sans forcer leur respect à l'exécution.

```python
# Sans annotation
def add(a, b):
    return a + b

# Avec annotation
def add(a: float, b: float) -> float:
    return a + b
```

> Analogie : annoter les types c'est comme mettre des étiquettes sur les boîtes de rangement. Python ne t'empêche pas de mettre des chaussures dans la boîte "livres", mais l'étiquette indique ce qui devrait s'y trouver.

---

## 2. Annoter une variable

```python
name: str = "Alice"
age: int = 20
score: float = 9.5
is_active: bool = True
```

Python **n'impose pas** ces types à l'exécution :

```python
age: int = "bonjour"  # Python ne plante pas, mais c'est incorrect
```

Les annotations servent à :
- Documenter le code
- Permettre aux outils comme `mypy` de détecter des erreurs

---

## 3. Annoter les paramètres et le retour d'une fonction

```python
def greet(name: str) -> str:
    return f"Bonjour {name}"

# Retour None
def log(message: str) -> None:
    print(message)
```

**`-> str`** = la fonction retourne une string
**`-> None`** = la fonction ne retourne rien (équivalent de `void` dans d'autres langages)

---

## 4. Le module `typing` — types complexes

Pour les types plus complexes, on importe depuis `typing`.

### `List`

```python
from typing import List

def get_names() -> List[str]:
    return ["Alice", "Bob"]
```

`List[str]` = une liste contenant des strings.

### `Tuple`

```python
from typing import Tuple

def get_coordinates() -> Tuple[float, float]:
    return (48.8566, 2.3522)
```

`Tuple[str, float]` = un tuple avec précisément une string et un float.

### `Union`

```python
from typing import Union

def process(value: Union[int, float]) -> float:
    return float(value)
```

`Union[int, float]` = soit un int soit un float.

### `Optional`

`Optional[str]` est un raccourci pour `Union[str, None]` — la valeur peut être une string ou `None`.

```python
from typing import Optional

def find_user(id: int) -> Optional[str]:
    if id == 1:
        return "Alice"
    return None
```

### `Callable`

```python
from typing import Callable

def apply(func: Callable[[float], float], value: float) -> float:
    return func(value)
```

`Callable[[float], float]` = une fonction qui prend un float et retourne un float.

### `Iterable` et `Sequence`

```python
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
```

---

## 5. `mypy` — vérifier les types statiquement

`mypy` est un outil qui analyse ton code et vérifie que les types sont cohérents **avant** l'exécution.

```bash
pip install mypy
mypy mon_fichier.py
```

```python
def add(a: int, b: int) -> int:
    return a + b

add("hello", 2)  # mypy détecte l'erreur !
```

---

## 6. Les fonctions comme valeurs (closures)

En Python, les fonctions sont des objets. On peut retourner une fonction depuis une autre fonction.

```python
def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(n: float) -> float:
        return n * multiplier  # capture multiplier du contexte parent
    return multiply

double = make_multiplier(2.0)
double(5.0)  # 10.0
```

La fonction `multiply` "capture" la variable `multiplier` de son contexte — c'est une **closure**.

---

---

# PARTIE 2 — WALKTHROUGH DES TÂCHES

---

## Tâche 0 — Annoter une addition de floats

**Objectif :** Écrire une fonction `add` avec annotations de types.

### Code complet

```python
def add(a: float, b: float) -> float:
    return a + b
```

### Explication

`a: float` et `b: float` indiquent que les deux paramètres doivent être des floats. `-> float` indique que la fonction retourne un float. La logique est simple : `a + b`.

---

## Tâche 1 — Annoter une concaténation de strings

**Objectif :** Écrire une fonction `concat` avec annotations de types.

### Code complet

```python
def concat(str1: str, str2: str) -> str:
    return str1 + str2
```

### Explication

`str1: str` et `str2: str` indiquent des strings en entrée. `-> str` indique une string en sortie. `+` concatène deux strings en Python.

---

## Tâche 2 — Annoter un floor (arrondi vers le bas)

**Objectif :** Retourner la partie entière d'un float.

### Code complet

```python
def floor(n: float) -> int:
    return int(n)
```

### Explication

`int(n)` en Python tronque vers zéro pour les positifs — ce qui est équivalent à `floor` pour les nombres positifs. Le type de retour est `int` car la partie entière est toujours un entier.

---

## Tâche 3 — Annoter une conversion en string

**Objectif :** Retourner la représentation string d'un float.

### Code complet

```python
def to_str(n: float) -> str:
    return str(n)
```

### Explication

`str(n)` convertit n'importe quelle valeur en sa représentation string. `3.14` → `'3.14'`.

---

## Tâche 4 — Annoter des variables directement

**Objectif :** Déclarer des variables avec annotations de types.

### Code complet

```python
a: int = 1
pi: float = 3.14
i_understand_annotations: bool = True
school: str = "Holberton"
```

### Explication

Les annotations peuvent s'appliquer directement aux variables, pas seulement aux fonctions. Chaque variable a son type annoté explicitement.

---

## Tâche 5 — Annoter avec `List`

**Objectif :** Sommer une liste de floats.

### Code complet

```python
from typing import List

def sum_list(input_list: List[float]) -> float:
    return sum(input_list)
```

### Explication

`List[float]` indique une liste de floats. `sum()` est une fonction built-in Python qui additionne tous les éléments d'un itérable.

---

## Tâche 6 — Annoter avec `Union`

**Objectif :** Sommer une liste qui peut contenir des ints et des floats.

### Code complet

```python
from typing import Union, List

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)
```

### Explication

`Union[int, float]` signifie que chaque élément peut être soit un `int` soit un `float`. Python additionne les deux types sans problème. Le retour est toujours `float` car la somme d'ints et floats est un float.

---

## Tâche 7 — Annoter avec `Tuple`

**Objectif :** Retourner un tuple contenant la clé et le carré de la valeur.

### Code complet

```python
from typing import Union, Tuple

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return (k, v ** 2)
```

### Explication

`Tuple[str, float]` spécifie précisément le type de chaque élément du tuple. `v ** 2` calcule le carré de `v`. Le type de retour est `float` même si `v` est un `int` — l'annotation est intentionnelle.

---

## Tâche 8 — Annoter avec `Callable`

**Objectif :** Retourner une fonction qui multiplie par un facteur.

### Code complet

```python
from typing import Callable

def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
```

### Explication

**`Callable[[float], float]`** = une fonction qui prend un float en argument et retourne un float.
**`multiply`** est une closure : elle "capture" `multiplier` depuis le scope de `make_multiplier`.
**`return multiply`** retourne la fonction elle-même (pas son résultat).

---

## Tâche 9 — Annoter avec `Iterable`, `Sequence`, `List`, `Tuple`

**Objectif :** Retourner chaque séquence et sa longueur.

### Code complet

```python
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
```

### Explication

**`Iterable[Sequence]`** = quelque chose sur lequel on peut itérer, dont chaque élément est une séquence (string, liste, etc.).
**`List[Tuple[Sequence, int]]`** = une liste de tuples où chaque tuple contient une séquence et un entier.
**`[(i, len(i)) for i in lst]`** = compréhension de liste qui crée un tuple `(séquence, longueur)` pour chaque élément.

---

---

# PARTIE 3 — TABLEAU RÉCAPITULATIF

| Tâche | Fichier | Concepts clés |
|---|---|---|
| 0 | `0-add.py` | `float`, annotations basiques, `->` |
| 1 | `1-concat.py` | `str`, concaténation |
| 2 | `2-floor.py` | `int(n)`, conversion de type |
| 3 | `3-to_str.py` | `str(n)`, conversion en string |
| 4 | `4-define_variables.py` | Annotations de variables, `bool` |
| 5 | `5-sum_list.py` | `List[float]`, `sum()` |
| 6 | `6-sum_mixed_list.py` | `Union[int, float]`, types mixtes |
| 7 | `7-to_kv.py` | `Tuple[str, float]`, `**` (puissance) |
| 8 | `8-make_multiplier.py` | `Callable`, closures, fonctions comme valeurs |
| 9 | `9-element_length.py` | `Iterable`, `Sequence`, compréhension de liste |
