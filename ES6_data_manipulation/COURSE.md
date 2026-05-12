# Cours complet — ES6 Data Manipulation

---

# PARTIE 1 — THÉORIE

---

## 1. `map` — transformer chaque élément

`map` crée un **nouveau tableau** en appliquant une fonction à chaque élément.

```js
const numbers = [1, 2, 3];
const doubled = numbers.map(n => n * 2);
// [2, 4, 6]
```

> Analogie : tu as une liste de prix en euros. `map` applique un taux de conversion à chaque prix pour obtenir une liste en dollars.

### Piège courant

`map` **ne modifie pas** le tableau original. Il crée toujours un nouveau tableau.

```js
const arr = [1, 2, 3];
const result = arr.map(n => n * 2);
console.log(arr);    // [1, 2, 3] — inchangé
console.log(result); // [2, 4, 6] — nouveau tableau
```

---

## 2. `filter` — garder certains éléments

`filter` crée un **nouveau tableau** avec seulement les éléments pour lesquels la fonction retourne `true`.

```js
const students = [
  { name: 'Alice', city: 'Paris' },
  { name: 'Bob', city: 'Lyon' },
  { name: 'Clara', city: 'Paris' },
];

const parisStudents = students.filter(s => s.city === 'Paris');
// [{ name: 'Alice', ... }, { name: 'Clara', ... }]
```

---

## 3. `reduce` — calculer une valeur unique

`reduce` parcourt le tableau et **accumule** une valeur.

```js
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((accumulator, current) => accumulator + current, 0);
// 0 + 1 = 1 → 1 + 2 = 3 → 3 + 3 = 6 → 6 + 4 = 10
```

Le deuxième argument (`0`) est la valeur initiale de l'accumulateur.

> Analogie : tu comptes de l'argent. Tu pars de 0, et pour chaque billet tu l'ajoutes au total.

---

## 4. Combiner `filter` et `map`

On peut chaîner ces méthodes :

```js
// Filtrer les étudiants de Paris, puis extraire leurs noms
const names = students
  .filter(s => s.city === 'Paris')
  .map(s => s.name);
// ['Alice', 'Clara']
```

---

## 5. `find` — trouver un seul élément

`find` retourne le **premier élément** qui correspond à la condition, ou `undefined`.

```js
const grades = [{ studentId: 1, grade: 86 }, { studentId: 5, grade: 97 }];
const grade = grades.find(g => g.studentId === 5);
// { studentId: 5, grade: 97 }
```

---

## 6. `every` — vérifier que tous les éléments correspondent

`every` retourne `true` si **tous** les éléments passent la condition.

```js
const values = [2, 4, 6, 8];
values.every(n => n % 2 === 0); // true — tous sont pairs

const mixed = [2, 3, 6];
mixed.every(n => n % 2 === 0); // false — 3 n'est pas pair
```

---

## 7. `Set` — liste sans doublons

Un `Set` est une collection où **chaque valeur est unique**.

```js
const set = new Set([1, 2, 2, 3, 3, 3]);
console.log(set); // Set {1, 2, 3}
set.has(2);       // true
set.has(5);       // false
set.size;         // 3
```

### Créer un Set depuis un tableau

```js
const array = [1, 2, 2, 3];
const unique = new Set(array); // Set {1, 2, 3}
```

### Itérer sur un Set

```js
for (const item of set) {
  console.log(item);
}
```

---

## 8. `Map` — clé-valeur flexible

Un `Map` est comme un objet mais avec des **clés de n'importe quel type** (pas seulement des strings).

```js
const map = new Map();
map.set('name', 'Alice');
map.set(42, 'answer');
map.set(true, 'yes');

map.get('name'); // 'Alice'
map.get(42);     // 'answer'
map.size;        // 3
```

### Itérer sur un Map

```js
for (const [key, value] of map) {
  console.log(`${key} → ${value}`);
}
```

### Différence Map vs objet

| | Objet | Map |
|---|---|---|
| Clés | Seulement strings/symbols | N'importe quel type |
| Ordre | Non garanti | Insertion garantie |
| Taille | `Object.keys().length` | `.size` |

---

## 9. `WeakMap` — Map avec références faibles

Un `WeakMap` est comme un `Map` mais ses clés doivent être des **objets**, et les références sont "faibles" (le garbage collector peut les supprimer).

```js
const weakMap = new WeakMap();
const obj = {};
weakMap.set(obj, 'valeur');
weakMap.get(obj); // 'valeur'
```

Utilisation typique : stocker des données privées liées à un objet sans empêcher sa suppression mémoire.

---

## 10. `ArrayBuffer` et `DataView` — tableaux typés

Un `ArrayBuffer` est un bloc de mémoire binaire brute. Un `DataView` permet de lire/écrire dedans avec un type précis.

```js
const buffer = new ArrayBuffer(8); // 8 octets
const view = new DataView(buffer);
view.setInt8(0, 42); // écrit 42 à la position 0
view.getInt8(0);     // lit 42
```

Utilisé pour manipuler des données binaires précises (protocoles réseau, fichiers, etc.).

---

---

# PARTIE 2 — WALKTHROUGH DES TÂCHES

---

## Tâche 0 — Retourner une liste d'étudiants

**Objectif :** Créer une fonction qui retourne un tableau d'objets étudiants.

### Code complet

```js
export default function getListStudents() {
  return [
    { id: 1, firstName: 'Guillaume', location: 'San Francisco' },
    { id: 2, firstName: 'James', location: 'Columbia' },
    { id: 5, firstName: 'Serena', location: 'San Francisco' },
  ];
}
```

### Explication

La fonction retourne directement un tableau littéral d'objets. Chaque objet a 3 propriétés : `id`, `firstName`, `location`.

---

## Tâche 1 — Extraire les ids avec `map`

**Objectif :** Retourner un tableau des ids à partir d'une liste d'étudiants.

### Code complet

```js
export default function getListStudentIds(element) {
  if (Array.isArray(element)) {
    return element.map((select) => select.id);
  } else return [];
}
```

### Explication

**`Array.isArray(element)`** — vérifie que l'argument est bien un tableau. Si ce n'est pas le cas, on retourne `[]`.
**`.map((select) => select.id)`** — pour chaque étudiant, extrait uniquement la valeur `id`.

---

## Tâche 2 — Filtrer par ville avec `filter`

**Objectif :** Retourner les étudiants d'une ville donnée.

### Code complet

```js
export default function getStudentsByLocation(students, city) {
  return students.filter((student) => student.location === city);
}
```

### Explication

`filter` garde seulement les étudiants dont `location` est égale à `city`. Si aucun étudiant ne correspond, retourne `[]`.

---

## Tâche 3 — Sommer les ids avec `reduce`

**Objectif :** Calculer la somme de tous les ids.

### Code complet

```js
export default function getStudentIdsSum(students) {
  return students.reduce((acc, id) => acc + id.id, 0);
}
```

### Explication

**`reduce((acc, id) => acc + id.id, 0)`** — `acc` commence à `0`. Pour chaque étudiant `id`, on ajoute `id.id` à l'accumulateur. À la fin, `acc` contient la somme de tous les ids.

---

## Tâche 4 — Combiner `filter` et `map`

**Objectif :** Filtrer les étudiants par ville et y ajouter leur note.

### Code complet

```js
export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    .filter((student) => student.location === city)
    .map((student) => {
      const gradeObj = newGrades.find((g) => g.studentId === student.id);
      return { ...student, grade: gradeObj ? gradeObj.grade : 'N/A' };
    });
}
```

### Explication

**`.filter(...)`** — garde seulement les étudiants de la ville.
**`.map(...)`** — pour chaque étudiant, cherche sa note dans `newGrades` avec `find`.
**`gradeObj ? gradeObj.grade : 'N/A'`** — si une note est trouvée on la prend, sinon `'N/A'`.
**`{ ...student, grade: ... }`** — copie toutes les propriétés de l'étudiant et ajoute/remplace `grade`.

---

## Tâche 5 — `ArrayBuffer` et `DataView`

**Objectif :** Créer un buffer et écrire une valeur Int8 à une position donnée.

### Code complet

```js
export default function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }
  const buffer = new ArrayBuffer(length);
  const view = new DataView(buffer);
  view.setInt8(position, value);
  return view;
}
```

### Explication

**`new ArrayBuffer(length)`** — crée un bloc de mémoire de `length` octets.
**`new DataView(buffer)`** — crée une vue sur ce buffer pour lire/écrire.
**`view.setInt8(position, value)`** — écrit `value` à la position `position` sous forme d'entier 8 bits.

---

## Tâche 6 — Créer un Set depuis un tableau

**Objectif :** Retourner un `Set` créé à partir d'un tableau.

### Code complet

```js
export default function setFromArray(array) {
  return new Set(array);
}
```

### Explication

`new Set(array)` crée automatiquement un Set avec les valeurs uniques du tableau. Les doublons sont supprimés.

---

## Tâche 7 — Vérifier si un Set contient toutes les valeurs d'un tableau

**Objectif :** Retourner `true` si toutes les valeurs du tableau sont dans le Set.

### Code complet

```js
export default function hasValuesFromArray(set, array) {
  return array.every(value => set.has(value));
}
```

### Explication

**`array.every(...)`** — retourne `true` seulement si **tous** les éléments passent le test.
**`set.has(value)`** — vérifie si `value` est dans le Set.

---

## Tâche 8 — Nettoyer un Set

**Objectif :** Retourner les éléments du Set qui commencent par une string, sans ce préfixe.

### Code complet

```js
export default function cleanSet(set, startString) {
  if (typeof startString !== 'string' || startString.length === 0) {
    return '';
  }
  const result = [];
  for (const item of set) {
    if (item.startsWith(startString)) {
      result.push(item.slice(startString.length));
    }
  }
  return result.join('-');
}
```

### Explication

**`item.startsWith(startString)`** — vérifie si l'élément commence par le préfixe.
**`item.slice(startString.length)`** — enlève le préfixe en coupant les `n` premiers caractères.
**`result.join('-')`** — joint les résultats avec `-`.

---

## Tâche 9 — Créer un Map

**Objectif :** Retourner un Map avec des données de courses.

### Code complet

```js
export default function groceriesList() {
  const groceries = new Map();
  groceries.set('Apples', 10);
  groceries.set('Tomatoes', 10);
  groceries.set('Pasta', 1);
  groceries.set('Rice', 1);
  groceries.set('Banana', 5);
  return groceries;
}
```

### Explication

On crée un Map vide puis on y ajoute des paires clé-valeur avec `.set(clé, valeur)`. Les clés sont des strings (nom du produit), les valeurs des nombres (quantité).

---

## Tâche 10 — Modifier un Map

**Objectif :** Mettre à jour toutes les valeurs égales à `1` dans un Map.

### Code complet

```js
export default function updateUniqueItems(map) {
  if (typeof map !== 'object' || !(map instanceof Map)) {
    throw new Error('Cannot process');
  }
  for (const [key, value] of map) {
    if (value === 1) {
      map.set(key, 100);
    }
  }
  return map;
}
```

### Explication

**`map instanceof Map`** — vérifie que l'argument est bien un Map.
**`for (const [key, value] of map)`** — destructure chaque entrée en `[clé, valeur]`.
**`map.set(key, 100)`** — met à jour la valeur pour cette clé.

---

---

# PARTIE 3 — TABLEAU RÉCAPITULATIF

| Tâche | Fichier | Concepts clés |
|---|---|---|
| 0 | `0-get_list_students.js` | Tableau d'objets |
| 1 | `1-get_list_student_ids.js` | `map`, `Array.isArray` |
| 2 | `2-get_students_by_loc.js` | `filter` |
| 3 | `3-get_ids_sum.js` | `reduce`, accumulateur |
| 4 | `4-update_grade_by_city.js` | `filter` + `map` + `find`, spread `...` |
| 5 | `5-typed_arrays.js` | `ArrayBuffer`, `DataView`, `setInt8` |
| 6 | `6-set.js` | `Set`, déduplication |
| 7 | `7-has_array_values.js` | `every`, `Set.has()` |
| 8 | `8-clean_set.js` | `Set`, `startsWith`, `slice`, `join` |
| 9 | `9-groceries_list.js` | `Map`, `.set()` |
| 10 | `10-update_uniq_items.js` | `instanceof`, itération `Map`, `.set()` |
