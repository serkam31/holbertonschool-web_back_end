# Cours complet — Pagination

---

# PARTIE 1 — THÉORIE

---

## 1. Qu'est-ce que la pagination ?

Quand une base de données contient des milliers d'entrées, il est impossible (et inutile) de tout envoyer d'un coup. La **pagination** divise les données en **pages**.

> Analogie : un livre. Tu ne lis pas tous les mots d'un coup — tu vas à la page 1, puis page 2, etc. La pagination de données fonctionne pareil.

---

## 2. Pagination simple — `page` et `page_size`

Le principe de base :

```python
page = 1        # numéro de page (commence à 1)
page_size = 10  # nombre d'éléments par page

# Calculer les indices de début et de fin
start = (page - 1) * page_size   # page 1 → index 0
end = page * page_size            # page 1 → index 10

data[start:end]  # éléments de l'index 0 à 9
```

| Page | start | end | Éléments |
|---|---|---|---|
| 1 | 0 | 10 | 0 à 9 |
| 2 | 10 | 20 | 10 à 19 |
| 3 | 20 | 30 | 20 à 29 |

---

## 3. Le slicing Python

```python
liste = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

liste[0:3]   # [0, 1, 2] — de l'index 0 à 2 (3 exclus)
liste[3:6]   # [3, 4, 5]
liste[100:]  # [] — au-delà de la liste : liste vide, pas d'erreur
```

Si `start` dépasse la taille de la liste, Python retourne une liste vide sans planter.

---

## 4. `assert` — validation des arguments

`assert condition` lance une `AssertionError` si la condition est fausse. Utile pour valider les paramètres.

```python
assert isinstance(page, int)  # doit être un entier
assert page > 0               # doit être positif
```

---

## 5. Lire un fichier CSV avec Python

```python
import csv

with open('fichier.csv') as f:
    reader = csv.reader(f)
    data = [row for row in reader]
# data[0] = les en-têtes
# data[1:] = les données
```

### Cache avec `__dataset`

Pour ne pas relire le fichier à chaque appel :

```python
def dataset(self):
    if self.__dataset is None:  # si pas encore chargé
        # charger le fichier
        self.__dataset = data[1:]  # stocker en cache
    return self.__dataset  # retourner le cache
```

---

## 6. `math.ceil()` — arrondi vers le haut

```python
import math
math.ceil(10 / 3)  # 4 (pas 3.33)
math.ceil(10 / 2)  # 5
math.ceil(11 / 2)  # 6 (pas 5.5)
```

Utilisé pour calculer le nombre total de pages :

```python
total_pages = math.ceil(total_items / page_size)
# 100 items, 10 par page → 10 pages
# 101 items, 10 par page → 11 pages (pas 10.1)
```

---

## 7. Pagination hypermedia

Au lieu de renvoyer seulement les données, on renvoie aussi des **métadonnées** qui permettent au client de naviguer :

```python
{
    'page': 2,
    'page_size': 10,
    'data': [...],
    'next_page': 3,      # None si dernière page
    'prev_page': 1,      # None si première page
    'total_pages': 15,
}
```

Le client n'a pas à calculer les indices — il reçoit directement quelle page est "suivante".

---

## 8. Pagination résiliente aux suppressions

**Problème :** Si un élément est supprimé pendant qu'un utilisateur navigue, les pages se décalent et l'utilisateur peut rater ou revoir des éléments.

**Solution :** Au lieu d'un numéro de page, on utilise un **index absolu** dans un dataset indexé. Même si des éléments sont supprimés, l'index reste stable.

```python
# Dataset indexé par position
{
    0: ['Alice', ...],
    1: ['Bob', ...],
    2: ['Clara', ...],
    # si l'index 1 est supprimé :
    0: ['Alice', ...],
    2: ['Clara', ...],  # l'index 2 est toujours là
}
```

La fonction avance l'index en **sautant les index manquants** :

```python
while len(data) < page_size:
    if current_index in indexed_dataset:  # si l'index existe
        data.append(indexed_dataset[current_index])
    current_index += 1  # avancer quoi qu'il arrive
```

---

---

# PARTIE 2 — WALKTHROUGH DES TÂCHES

---

## Tâche 0 — Fonction helper `index_range`

**Objectif :** Calculer les indices de début et de fin pour une page donnée.

### Code complet

```python
def index_range(page, page_size):
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)
```

### Explication

**`(page - 1) * page_size`** — page 1 → 0, page 2 → page_size, page 3 → 2*page_size, etc.
**`page * page_size`** — fin exclusive : les éléments `[start:end]` vont de `start` à `end-1`.
**`return (start, end)`** — retourne un tuple.

---

## Tâche 1 — Pagination simple avec une classe `Server`

**Objectif :** Créer une classe qui charge un CSV et retourne une page de données.

### Code complet

```python
import csv
import math
from typing import List

def index_range(page, page_size):
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)

class Server:
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # ignorer l'en-tête
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert (
            isinstance(page, int) and
            isinstance(page_size, int) and
            page > 0 and
            page_size > 0
        )
        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
```

### Explication

**`self.__dataset = None`** — le dataset n'est pas chargé au démarrage.
**`dataset()`** — charge le CSV une seule fois et le met en cache dans `__dataset`. Les appels suivants utilisent le cache.
**`assert ...`** — valide que `page` et `page_size` sont des entiers positifs.
**`self.dataset()[start:end]`** — retourne la tranche correspondant à la page.

---

## Tâche 2 — Pagination hypermedia

**Objectif :** Ajouter une méthode `get_hyper` qui retourne les données avec métadonnées de navigation.

### Code complet

```python
def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
    data = self.get_page(page, page_size)
    total_pages = math.ceil(len(self.dataset()) / page_size)
    next_page = page + 1 if page < total_pages else None
    prev_page = page - 1 if page > 1 else None
    return {
        'page_size': len(data),
        'page': page,
        'data': data,
        'next_page': next_page,
        'prev_page': prev_page,
        'total_pages': total_pages,
    }
```

### Explication

**`math.ceil(len(self.dataset()) / page_size)`** — nombre total de pages, arrondi vers le haut.
**`page + 1 if page < total_pages else None`** — si on n'est pas sur la dernière page, il y a une page suivante.
**`page - 1 if page > 1 else None`** — si on n'est pas sur la première page, il y a une page précédente.
**`'page_size': len(data)`** — la taille réelle de la page (peut être inférieure à `page_size` pour la dernière page).

---

## Tâche 3 — Pagination résiliente aux suppressions

**Objectif :** Paginer à partir d'un index absolu, résistant aux suppressions d'éléments.

### Code complet

```python
def indexed_dataset(self) -> Dict[int, List]:
    if self.__indexed_dataset is None:
        dataset = self.dataset()
        self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
    return self.__indexed_dataset

def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
    assert 0 <= index < len(self.indexed_dataset())

    data = []
    current_index = index

    while len(data) < page_size:
        if current_index in self.indexed_dataset():
            data.append(self.indexed_dataset()[current_index])
        current_index += 1

    return {
        'index': index,
        'next_index': current_index,
        'page_size': page_size,
        'data': data,
    }
```

### Explication

**`indexed_dataset()`** — crée un dictionnaire `{position: ligne}`. Contrairement à une liste, les suppressions ne font pas glisser les indices.

**`while len(data) < page_size`** — continue d'avancer jusqu'à avoir `page_size` éléments.
**`if current_index in self.indexed_dataset()`** — si l'index existe (n'a pas été supprimé), on prend l'élément.
**`current_index += 1`** — avance toujours, même si l'index était supprimé.
**`'next_index': current_index`** — retourne l'index de départ de la prochaine page.

---

---

# PARTIE 3 — TABLEAU RÉCAPITULATIF

| Tâche | Fichier | Concepts clés |
|---|---|---|
| 0 | `0-simple_helper_function.py` | Calcul `start`/`end`, tuple, formule de pagination |
| 1 | `1-simple_pagination.py` | Classe `Server`, cache `__dataset`, `csv.reader`, `assert`, slicing |
| 2 | `2-hypermedia_pagination.py` | `math.ceil`, `next_page`/`prev_page`, métadonnées de navigation |
| 3 | `3-hypermedia_del_pagination.py` | Dataset indexé, boucle avec sauts, résilience aux suppressions |
