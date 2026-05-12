# Cours complet — NoSQL

---

# PARTIE 1 — THÉORIE

---

## 1. SQL vs NoSQL

### SQL — bases de données relationnelles

Les données sont organisées en **tableaux** avec des colonnes fixes (schéma rigide).

```
Table "students"
+----+-------+-----+
| id | name  | age |
+----+-------+-----+
|  1 | Alice |  20 |
|  2 | Bob   |  22 |
+----+-------+-----+
```

### NoSQL — bases de données non relationnelles

Les données sont stockées sous d'autres formes. MongoDB utilise des **documents JSON**.

```json
{
  "_id": "abc123",
  "name": "Alice",
  "age": 20,
  "hobbies": ["code", "music"],
  "address": { "city": "Paris", "zip": "75001" }
}
```

### Tableau comparatif

| | SQL | NoSQL (MongoDB) |
|---|---|---|
| Structure | Tableaux fixes | Documents JSON flexibles |
| Schéma | Obligatoire | Optionnel |
| Relations | Jointures entre tables | Données imbriquées |
| Exemple | MySQL, PostgreSQL | MongoDB, Redis |

> Analogie : SQL c'est un classeur avec des feuilles bien structurées. NoSQL c'est une boîte où tu mets des post-its — chaque post-it peut avoir une forme différente.

---

## 2. Terminologie MongoDB

| MongoDB | SQL équivalent | Description |
|---|---|---|
| Database | Database | Conteneur principal |
| Collection | Table | Groupe de documents |
| Document | Row (ligne) | Un enregistrement JSON |
| Field | Column (colonne) | Une propriété du document |
| `_id` | Primary key | Identifiant unique automatique |

---

## 3. Les commandes MongoDB (shell)

### Naviguer

```javascript
show dbs            // liste toutes les bases de données
use ma_db           // sélectionner (ou créer) une base
show collections    // liste les collections de la base courante
```

### CRUD — les 4 opérations de base

**Create — insérer un document**

```javascript
db.school.insert({ name: "Holberton school" })
db.school.insertOne({ name: "Alice", age: 20 })
db.school.insertMany([{ name: "Bob" }, { name: "Clara" }])
```

**Read — lire des documents**

```javascript
db.school.find()                     // tous les documents
db.school.find({ name: "Alice" })    // filtre par champ
db.school.findOne({ name: "Alice" }) // premier résultat seulement
db.school.count()                    // nombre de documents
```

**Update — modifier des documents**

```javascript
// $set : modifier un champ existant ou en ajouter un
db.school.update(
  { name: "Holberton school" },      // filtre (qui modifier)
  { $set: { address: "972 Mission" } }, // modification
  { multi: true }                    // modifier tous les matchs
)
```

**Delete — supprimer des documents**

```javascript
db.school.deleteMany({ name: "Holberton school" }) // supprime tous les matchs
db.school.deleteOne({ name: "Alice" })             // supprime le premier match
```

---

## 4. Les opérateurs de requête

```javascript
db.collection.find({ age: { $gt: 18 } })   // age > 18
db.collection.find({ age: { $gte: 18 } })  // age >= 18
db.collection.find({ age: { $lt: 18 } })   // age < 18
db.collection.find({ age: { $ne: 18 } })   // age != 18
db.collection.find({ topics: "MongoDB" })  // tableau contient "MongoDB"
```

---

## 5. PyMongo — utiliser MongoDB avec Python

PyMongo est le driver Python officiel pour MongoDB.

```python
from pymongo import MongoClient

client = MongoClient('mongodb://127.0.0.1:27017')  # connexion
db = client.ma_database                             # sélectionner la base
collection = db.ma_collection                       # sélectionner la collection
```

### Les opérations CRUD en Python

```python
# Insert
collection.insert_one({"name": "Alice"})

# Find
collection.find()             # tous les documents (curseur)
collection.find({"age": 20})  # avec filtre
list(collection.find())       # convertir en liste Python

# Update
collection.update_many(
    {"name": "Alice"},
    {"$set": {"age": 21}}
)

# Delete
collection.delete_many({"name": "Alice"})
```

### `**kwargs` — arguments nommés dynamiques

```python
def insert_school(mongo_collection, **kwargs):
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
```

`**kwargs` capture tous les arguments nommés passés à la fonction dans un dictionnaire. `insert_school(col, name="Alice", age=20)` → `kwargs = {"name": "Alice", "age": 20}`.

---

## 6. Compter les documents

```python
collection.count_documents({})              # tous
collection.count_documents({"age": 20})     # avec filtre
collection.count_documents({"method": "GET", "path": "/status"})  # plusieurs conditions
```

---

---

# PARTIE 2 — WALKTHROUGH DES TÂCHES

---

## Tâche 0 — Lister les bases de données

**Objectif :** Afficher toutes les bases de données disponibles.

### Code complet

```javascript
show dbs
```

### Explication

`show dbs` est une commande du shell MongoDB. Elle liste toutes les bases de données avec leur taille.

---

## Tâche 1 — Créer ou utiliser une base de données

**Objectif :** Se connecter à une base (ou la créer si elle n'existe pas).

### Code complet

```javascript
use my_db
```

### Explication

`use my_db` sélectionne la base `my_db`. Si elle n'existe pas, MongoDB la crée automatiquement dès que tu y insères un document.

---

## Tâche 2 — Insérer un document

**Objectif :** Ajouter un document dans la collection `school`.

### Code complet

```javascript
db.school.insert({ name: "Holberton school" })
```

### Explication

`db.school` accède à la collection `school` (créée automatiquement). `.insert({ ... })` insère le document JSON. MongoDB ajoute automatiquement un champ `_id` unique.

---

## Tâche 3 — Lister tous les documents

**Objectif :** Afficher tous les documents d'une collection.

### Code complet

```javascript
db.school.find()
```

### Explication

`.find()` sans argument retourne tous les documents. Le shell affiche les résultats formatés avec leur `_id`.

---

## Tâche 4 — Filtrer par champ

**Objectif :** Afficher les documents avec un nom spécifique.

### Code complet

```javascript
db.school.find({ name: "Holberton school" })
```

### Explication

L'objet `{ name: "Holberton school" }` est le **filtre**. Seuls les documents dont `name` correspond sont retournés.

---

## Tâche 5 — Compter les documents

**Objectif :** Afficher le nombre de documents dans la collection.

### Code complet

```javascript
db.school.count()
```

### Explication

`.count()` retourne le nombre total de documents dans la collection.

---

## Tâche 6 — Mettre à jour un document

**Objectif :** Ajouter un champ `address` à tous les documents avec un nom spécifique.

### Code complet

```javascript
db.school.update(
  { name: "Holberton school" },
  { $set: { address: "972 Mission street" } },
  { multi: true }
)
```

### Explication

**Premier argument** = filtre : quels documents modifier.
**`$set`** = opérateur qui ajoute ou modifie des champs sans toucher aux autres.
**`{ multi: true }`** = modifier tous les documents qui correspondent (pas seulement le premier).

---

## Tâche 7 — Supprimer des documents

**Objectif :** Supprimer tous les documents avec un nom spécifique.

### Code complet

```javascript
db.school.deleteMany({ name: "Holberton school" })
```

### Explication

`.deleteMany({ ... })` supprime **tous** les documents qui correspondent au filtre. `.deleteOne({ ... })` n'en supprimerait qu'un.

---

## Tâche 8 — Lister tous les documents (Python)

**Objectif :** Créer une fonction Python qui retourne tous les documents d'une collection.

### Code complet

```python
def list_all(mongo_collection):
    return mongo_collection.find()
```

### Explication

`.find()` sans argument retourne un **curseur** — un objet itérable sur tous les documents. On retourne le curseur directement (pas besoin de le convertir en liste).

---

## Tâche 9 — Insérer un document (Python)

**Objectif :** Insérer un document et retourner son `_id`.

### Code complet

```python
def insert_school(mongo_collection, **kwargs):
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
```

### Explication

**`**kwargs`** — capture tous les arguments nommés dans un dictionnaire. L'appelant peut passer n'importe quels champs.
**`insert_one(kwargs)`** — insère le dictionnaire comme document.
**`result.inserted_id`** — retourne l'`_id` généré automatiquement par MongoDB.

---

## Tâche 10 — Mettre à jour les topics (Python)

**Objectif :** Modifier les topics d'une école par son nom.

### Code complet

```python
def update_topics(mongo_collection, name, topics):
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result.modified_count
```

### Explication

**`update_many({ "name": name }, { "$set": { "topics": topics } })`** — met à jour le champ `topics` de tous les documents dont `name` correspond.
**`result.modified_count`** — nombre de documents modifiés.

---

## Tâche 11 — Rechercher par topic (Python)

**Objectif :** Retourner toutes les écoles qui enseignent un topic donné.

### Code complet

```python
def schools_by_topic(mongo_collection, topic):
    return mongo_collection.find({"topics": topic})
```

### Explication

`{"topics": topic}` — MongoDB comprend automatiquement ce filtre sur un tableau : il retourne tous les documents où le champ `topics` **contient** la valeur `topic`.

---

## Tâche 12 — Statistiques des logs Nginx (Python)

**Objectif :** Afficher des statistiques sur des logs Nginx stockés dans MongoDB.

### Code complet

```python
from pymongo import MongoClient

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    total = collection.count_documents({})
    print("{} logs".format(total))

    print("Methods:")
    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status = collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status))
```

### Explication

**`client.logs.nginx`** — accède à la collection `nginx` dans la base `logs`.
**`count_documents({})`** — compte tous les documents.
**`count_documents({"method": method})`** — compte les documents filtrés par méthode HTTP.
**`count_documents({"method": "GET", "path": "/status"})`** — filtre sur deux champs simultanément.

---

---

# PARTIE 3 — TABLEAU RÉCAPITULATIF

| Tâche | Fichier | Concepts clés |
|---|---|---|
| 0 | `0-list_databases` | `show dbs` |
| 1 | `1-use_or_create_database` | `use db` |
| 2 | `2-insert` | `db.col.insert()` |
| 3 | `3-all` | `db.col.find()` |
| 4 | `4-match` | `find({ filtre })` |
| 5 | `5-count` | `db.col.count()` |
| 6 | `6-update` | `update`, `$set`, `multi: true` |
| 7 | `7-delete` | `deleteMany` |
| 8 | `8-all.py` | PyMongo, `.find()`, curseur |
| 9 | `9-insert_school.py` | `insert_one`, `**kwargs`, `inserted_id` |
| 10 | `10-update_topics.py` | `update_many`, `$set`, `modified_count` |
| 11 | `11-schools_by_topic.py` | `find` sur tableau, filtre MongoDB |
| 12 | `12-log_stats.py` | `count_documents`, filtres multiples, stats |
