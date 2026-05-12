# Python Async Comprehension

## Introduction
Les **async comprehensions** combinent deux concepts : les **compréhensions de liste** (une syntaxe Python pour créer des listes) et l'**asynchrone** (exécuter du code sans bloquer le programme).

**Pourquoi on l'apprend ?** Pour écrire du code asynchrone de façon concise et lisible.

---

## Concepts clés

### Rappel : compréhension de liste classique
```python
numbers = [1, 2, 3, 4, 5]
squares = [n ** 2 for n in numbers]
# [1, 4, 9, 16, 25]
```

### Générateur asynchrone
```python
import asyncio
import random

async def async_generator():
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
```

### Async comprehension
```python
async def main():
    results = [value async for value in async_generator()]
    print(results)
```

### `asyncio.gather` — exécuter plusieurs coroutines en parallèle
```python
async def main():
    results = await asyncio.gather(
        coroutine1(),
        coroutine2(),
        coroutine3()
    )
```

---

## Résumé

| Concept | Utilité |
|---|---|
| Compréhension de liste | Créer une liste en une ligne |
| `async for` | Itérer sur un générateur asynchrone |
| `async` comprehension | Compréhension avec `async for` |
| `asyncio.gather` | Lancer plusieurs tâches en parallèle |
