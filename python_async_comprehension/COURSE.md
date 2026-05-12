# Cours complet — Python Async Comprehension

---

# PARTIE 1 — THÉORIE

---

## 1. Rappel : compréhensions de liste classiques

Une compréhension de liste crée une liste en une seule expression lisible.

```python
# Boucle classique
squares = []
for n in range(5):
    squares.append(n ** 2)

# Compréhension — même résultat en une ligne
squares = [n ** 2 for n in range(5)]
# [0, 1, 4, 9, 16]
```

---

## 2. Les générateurs (`yield`)

Un générateur est une fonction qui **produit des valeurs une par une** au lieu de tout calculer d'un coup.

```python
def count_up(n):
    for i in range(n):
        yield i  # produit une valeur et suspend

gen = count_up(3)
next(gen)  # 0
next(gen)  # 1
next(gen)  # 2
```

L'avantage : économise de la mémoire car les valeurs ne sont pas toutes calculées en même temps.

---

## 3. Générateurs asynchrones

Un générateur asynchrone combine `async def` et `yield`. Il produit des valeurs de façon asynchrone.

```python
import asyncio
import random

async def async_generator():
    for i in range(10):
        await asyncio.sleep(1)  # attend 1 seconde de façon asynchrone
        yield random.uniform(0, 10)  # produit une valeur
```

Il faut utiliser `async for` pour l'itérer :

```python
async def main():
    async for value in async_generator():
        print(value)
```

---

## 4. Async comprehension

Comme une compréhension de liste normale, mais avec `async for` :

```python
async def main():
    # Compréhension classique
    result = [n ** 2 for n in range(5)]

    # Async comprehension — itère sur un générateur asynchrone
    result = [value async for value in async_generator()]
```

---

## 5. `asyncio.gather()` — parallélisme

Rappel : `asyncio.gather()` lance plusieurs coroutines **en même temps**.

```python
async def main():
    # Séquentiel — chaque appel attend le précédent
    result1 = await async_comprehension()  # ~10 secondes
    result2 = await async_comprehension()  # ~10 secondes de plus
    # Total : ~20 secondes

    # Parallèle — tous les appels partent en même temps
    results = await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    )
    # Total : ~10 secondes (le temps du plus long)
```

---

## 6. Pourquoi 4 fois en parallèle prend ~10 secondes (et pas ~40) ?

Chaque appel à `async_comprehension()` prend ~10 secondes (10 itérations × 1 seconde). Si on les lance en **parallèle** avec `gather`, ils s'exécutent tous en même temps — le temps total est celui du plus long, soit ~10 secondes.

> Analogie : 4 ouvriers travaillent en parallèle sur 4 tâches identiques de 10 heures. Le chantier prend 10 heures, pas 40.

---

---

# PARTIE 2 — WALKTHROUGH DES TÂCHES

---

## Tâche 0 — Générateur asynchrone

**Objectif :** Créer une coroutine qui génère 10 nombres aléatoires avec délai.

### Code complet

```python
import asyncio
import random
import typing

async def async_generator() -> typing.Generator[float, None, None]:
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
```

### Explication

**`async def` + `yield`** — crée un générateur asynchrone.
**`for _ in range(10)`** — répète 10 fois. `_` est une convention pour une variable qu'on n'utilise pas.
**`await asyncio.sleep(1)`** — attend 1 seconde de façon asynchrone à chaque itération.
**`yield random.uniform(0, 10)`** — produit un float aléatoire entre 0 et 10, puis suspend.

**Type de retour `typing.Generator[float, None, None]`** :
- `float` = type des valeurs produites
- `None` = type de la valeur envoyée au générateur (on n'en envoie pas)
- `None` = type de la valeur de retour finale (il n'y en a pas)

---

## Tâche 1 — Async comprehension

**Objectif :** Collecter 10 nombres depuis `async_generator` avec une async comprehension.

### Code complet

```python
from typing import List
async_generator = __import__('0-async_generator').async_generator

async def async_comprehension() -> List[float]:
    return [i async for i in async_generator()]
```

### Explication

**`[i async for i in async_generator()]`** — itère sur le générateur asynchrone et collecte toutes les valeurs dans une liste. C'est l'équivalent async de `[i for i in generator()]`.

La fonction retourne la liste complète des 10 valeurs.

---

## Tâche 2 — Mesurer le runtime de 4 comprehensions en parallèle

**Objectif :** Lancer 4 fois `async_comprehension` en parallèle et mesurer le temps total.

### Code complet

```python
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    start_time = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time.time()
    return end_time - start_time
```

### Explication

**`[async_comprehension() for _ in range(4)]`** — crée une liste de 4 coroutines.
**`*[...]`** — dépaquette la liste pour passer les 4 coroutines à `gather`.
**`await asyncio.gather(...)`** — lance les 4 en parallèle et attend qu'elles soient toutes terminées.
**`time.time()`** — mesure le temps avant et après.

Le résultat sera ~10 secondes (et non ~40) car les 4 coroutines s'exécutent simultanément.

---

---

# PARTIE 3 — TABLEAU RÉCAPITULATIF

| Tâche | Fichier | Concepts clés |
|---|---|---|
| 0 | `0-async_generator.py` | Générateur asynchrone, `async def` + `yield`, `asyncio.sleep` |
| 1 | `1-async_comprehension.py` | Async comprehension, `async for`, `List[float]` |
| 2 | `2-measure_runtime.py` | `asyncio.gather`, parallélisme, `time.time()`, mesure de performance |
