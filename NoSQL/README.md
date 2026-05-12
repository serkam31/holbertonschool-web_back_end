# NoSQL

## Introduction
**NoSQL** signifie "Not Only SQL". C'est une famille de bases de données qui ne stockent pas les données sous forme de tableaux comme SQL, mais sous d'autres formes (documents, clé-valeur, graphes, etc.).

**Pourquoi on l'apprend ?** Parce que des applications comme Instagram, Netflix ou MongoDB utilisent NoSQL pour sa flexibilité et ses performances.

---

## Concepts clés

### SQL vs NoSQL

| | SQL | NoSQL |
|---|---|---|
| Structure | Tableaux fixes | Flexible (JSON, etc.) |
| Schéma | Obligatoire | Optionnel |
| Exemple | MySQL, PostgreSQL | MongoDB, Redis |

### MongoDB — la base NoSQL la plus populaire
Les données sont stockées en **documents JSON** :
```json
{
  "_id": "123",
  "name": "Alice",
  "age": 20,
  "hobbies": ["code", "music"]
}
```

### Les opérations de base (CRUD)
```js
// Créer
db.students.insertOne({ name: "Alice", age: 20 });

// Lire
db.students.find({ age: 20 });

// Modifier
db.students.updateOne({ name: "Alice" }, { $set: { age: 21 } });

// Supprimer
db.students.deleteOne({ name: "Alice" });
```

---

## Résumé

| Concept | Utilité |
|---|---|
| NoSQL | Base de données flexible |
| Document | Unité de stockage (comme un objet JSON) |
| Collection | Groupe de documents (comme une table SQL) |
| CRUD | Créer, Lire, Modifier, Supprimer |
