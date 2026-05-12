# ES6 Data Manipulation

## Introduction
Ce projet porte sur la manipulation de données avec les outils modernes de JavaScript : `map`, `filter`, `reduce`, et les nouvelles structures `Set`, `Map`, et `WeakMap`.

**Pourquoi on l'apprend ?** Manipuler des listes de données est une tâche quotidienne en développement. Ces outils remplacent les boucles `for` classiques par du code plus lisible.

---

## Concepts clés

### `map` — transformer chaque élément
```js
const numbers = [1, 2, 3];
const doubled = numbers.map(n => n * 2);
// [2, 4, 6]
```

### `filter` — garder seulement certains éléments
```js
const numbers = [1, 2, 3, 4, 5];
const evens = numbers.filter(n => n % 2 === 0);
// [2, 4]
```

### `reduce` — réduire un tableau à une seule valeur
```js
const numbers = [1, 2, 3, 4];
const sum = numbers.reduce((total, n) => total + n, 0);
// 10
```

### `Set` — une liste sans doublons
```js
const set = new Set([1, 2, 2, 3, 3]);
console.log(set); // Set {1, 2, 3}
```

### `Map` — comme un objet mais plus puissant
```js
const map = new Map();
map.set("name", "Alice");
map.set("age", 20);
console.log(map.get("name")); // Alice
```

---

## Résumé

| Méthode | Utilité |
|---|---|
| `map` | Transformer chaque élément |
| `filter` | Filtrer selon une condition |
| `reduce` | Calculer une valeur unique |
| `Set` | Liste sans doublons |
| `Map` | Clé-valeur flexible |
