# Cours complet — Python Async Function

---

# PARTIE 1 — THÉORIE

---

## 1. Programmation synchrone vs asynchrone

### Synchrone — bloquant

```python
import time

def get_data():
    time.sleep(3)  # le programme s'arrête 3 secondes
    return "données"

get_data()  # 3 secondes d'attente
print("suite")  # s'exécute seulement après
```

> Analogie synchrone : tu appelles un ami, tu attends qu'il réponde avant de faire autre chose. Tu es bloqué pendant ce temps.

### Asynchrone — non bloquant

```python
import asyncio

async def get_data():
    await asyncio.sleep(3)  # cède le contrôle pendant 3 secondes
    return "données"
```

> Analogie asynchrone : tu envoies un message à ton ami et tu continues ta journée. Quand il répond, tu t'en occupes.

---

## 2. `async def` — déclarer une coroutine

Une fonction précédée de `async def` est une **coroutine**. Elle ne s'exécute pas directement — elle retourne un objet coroutine qu'il faut `await`.

```python
async def ma_coroutine():
    return 42

# ❌ Ne fonctionne pas comme ça
result = ma_coroutine()  # retourne <coroutine object>, pas 42

# ✅ Il faut await
result = await ma_coroutine()  # retourne 42
```

---

## 3. `await` — attendre sans bloquer

`await` suspend la coroutine courante et rend le contrôle à la boucle d'événements. Pendant ce temps, d'autres tâches peuvent s'exécuter.

```python
async def example():
    print("Avant")
    await asyncio.sleep(1)  # suspend 1 seconde sans bloquer
    print("Après")
```

`await` ne peut être utilisé **que dans** une fonction `async def`.

---

## 4. `asyncio.run()` — lancer le programme asynchrone

Pour exécuter une coroutine depuis du code synchrone (comme le point d'entrée du programme) :

```python
async def main():
    await ma_coroutine()

asyncio.run(main())  # lance la boucle d'événements
```

---

## 5. `random.uniform()` — nombre aléatoire décimal

```python
import random

random.uniform(0, 10)  # float aléatoire entre 0 et 10
```

---

## 6. `asyncio.gather()` — lancer plusieurs coroutines en parallèle

`asyncio.gather()` lance plusieurs coroutines **en même temps** et attend qu'elles soient toutes terminées.

```python
async def main():
    results = await asyncio.gather(
        wait_random(5),
        wait_random(5),
        wait_random(5),
    )
    # results est une liste des retours de chaque coroutine
```

> Analogie : envoyer 3 lettres à la poste en même temps. Elles partent simultanément, et tu récupères les réponses au fur et à mesure.

### Avec `*` pour dépaqueter une liste

```python
tasks = [wait_random(max_delay) for _ in range(n)]
results = await asyncio.gather(*tasks)  # * dépaquete la liste
```

---

## 7. `asyncio.create_task()` — créer une tâche planifiée

`create_task()` planifie une coroutine pour qu'elle s'exécute "en arrière-plan" sans attendre immédiatement.

```python
async def main():
    task = asyncio.create_task(wait_random(5))
    # on peut faire autre chose ici
    result = await task  # on attend le résultat quand on en a besoin
```

**Différence avec `await` direct :**

```python
# Séquentiel — l'un après l'autre
result1 = await wait_random(5)  # attend la fin
result2 = await wait_random(5)  # commence seulement après

# Parallèle avec create_task
task1 = asyncio.create_task(wait_random(5))  # démarre immédiatement
task2 = asyncio.create_task(wait_random(5))  # démarre immédiatement
result1 = await task1
result2 = await task2
```

---

## 8. Mesurer le temps d'exécution

```python
import time

start = time.perf_counter()
# ... code à mesurer ...
end = time.perf_counter()
elapsed = end - start
```

`time.perf_counter()` est plus précis que `time.time()` pour mesurer des durées courtes.

---

## 9. `__import__()` — importation dynamique

Dans ce projet, les fichiers importent les uns des autres avec `__import__` :

```python
wait_random = __import__('0-basic_async_syntax').wait_random
```

C'est équivalent à `from 0-basic_async_syntax import wait_random` mais fonctionne quand le nom du fichier commence par un chiffre (qui n'est pas un identifiant Python valide).

---

---

# PARTIE 2 — WALKTHROUGH DES TÂCHES

---

## Tâche 0 — Coroutine simple avec délai aléatoire

**Objectif :** Créer une coroutine qui attend un délai aléatoire et le retourne.

### Code complet

```python
import random
import asyncio

async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
```

### Explication

**`async def`** — déclare une coroutine.
**`random.uniform(0, max_delay)`** — génère un float aléatoire entre 0 et `max_delay`.
**`await asyncio.sleep(delay)`** — attend `delay` secondes sans bloquer le thread.
**`return delay`** — retourne la durée attendue.

---

## Tâche 1 — Lancer plusieurs coroutines en parallèle

**Objectif :** Lancer `n` fois `wait_random` et retourner les délais triés.

### Code complet

```python
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
```

### Explication

**`[wait_random(max_delay) for _ in range(n)]`** — crée une liste de `n` coroutines (non encore exécutées).
**`await asyncio.gather(*tasks)`** — lance toutes les coroutines en parallèle et attend leurs résultats. `*tasks` dépaquette la liste.
**`sorted(delays)`** — retourne la liste triée du plus petit au plus grand.

---

## Tâche 2 — Mesurer le temps d'exécution

**Objectif :** Mesurer le temps total pris par `wait_n`.

### Code complet

```python
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.perf_counter()
    return end_time - start_time
```

### Explication

**`time.perf_counter()`** — chronomètre précis.
**`asyncio.run(wait_n(n, max_delay))`** — lance la boucle d'événements depuis une fonction synchrone.
**`end_time - start_time`** — durée totale en secondes.

Note : `measure_time` est une fonction **synchrone** (pas `async`). Elle utilise `asyncio.run()` pour lancer la coroutine.

---

## Tâche 3 — Retourner une `asyncio.Task`

**Objectif :** Créer une fonction qui retourne une Task à partir de `wait_random`.

### Code complet

```python
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    return asyncio.create_task(wait_random(max_delay))
```

### Explication

**`asyncio.create_task()`** — planifie la coroutine pour exécution et retourne un objet `Task`. La Task commence à s'exécuter dès qu'une boucle d'événements est active.

Cette fonction est **synchrone** (pas `async`) — elle ne fait que créer et retourner la Task, pas l'attendre.

---

## Tâche 4 — Utiliser les Tasks dans `wait_n`

**Objectif :** Reproduire `wait_n` mais avec `task_wait_random`.

### Code complet

```python
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    tasks = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    return sorted(await asyncio.gather(*tasks))
```

### Explication

La logique est identique à `wait_n` de la tâche 1. La seule différence : on appelle `task_wait_random(max_delay)` (qui retourne une Task) au lieu de `wait_random(max_delay)` (qui retourne une coroutine). `asyncio.gather()` accepte les deux.

---

---

# PARTIE 3 — TABLEAU RÉCAPITULATIF

| Tâche | Fichier | Concepts clés |
|---|---|---|
| 0 | `0-basic_async_syntax.py` | `async def`, `await`, `asyncio.sleep`, `random.uniform` |
| 1 | `1-concurrent_coroutines.py` | `asyncio.gather`, `*tasks`, `sorted`, parallélisme |
| 2 | `2-measure_runtime.py` | `time.perf_counter`, `asyncio.run`, fonction synchrone |
| 3 | `3-tasks.py` | `asyncio.create_task`, `asyncio.Task` |
| 4 | `4-tasks.py` | Task vs coroutine, `asyncio.gather` avec Tasks |
