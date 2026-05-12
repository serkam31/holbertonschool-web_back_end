# Python Async Function

## Introduction
La programmation **asynchrone** permet d'exécuter plusieurs tâches "en même temps" sans bloquer le programme. En Python, ça se fait avec `async` et `await`.

**Analogie :** Au restaurant, le serveur ne reste pas figé devant le four en attendant que ta pizza cuise. Il va prendre d'autres commandes pendant ce temps. C'est ça l'asynchrone.

---

## Concepts clés

### Fonction synchrone vs asynchrone
```python
import asyncio

# Synchrone — bloque tout pendant 3 secondes
import time
def wait():
    time.sleep(3)
    print("Terminé")

# Asynchrone — ne bloque pas
async def wait():
    await asyncio.sleep(3)
    print("Terminé")
```

### `async def` et `await`
```python
async def fetch_data():
    await asyncio.sleep(1)  # simule une attente
    return "données reçues"

async def main():
    result = await fetch_data()
    print(result)

asyncio.run(main())
```

### Lancer plusieurs tâches en parallèle
```python
async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(fetch_data())

    result1 = await task1
    result2 = await task2
```

---

## Résumé

| Concept | Utilité |
|---|---|
| `async def` | Déclarer une fonction asynchrone |
| `await` | Attendre le résultat sans bloquer |
| `asyncio.run()` | Lancer le programme asynchrone |
| `asyncio.create_task()` | Lancer une tâche en parallèle |
