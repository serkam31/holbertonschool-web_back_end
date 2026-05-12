# ES6 Basic

## Introduction
ES6 (aussi appelé ES2015) est une mise à jour majeure de JavaScript sortie en 2015. Avant ES6, JavaScript avait beaucoup de limitations qui rendaient le code difficile à lire et à maintenir. ES6 apporte une syntaxe plus moderne, plus claire et plus puissante.

**Pourquoi on l'apprend ?** Parce que tout le JavaScript moderne (React, Node.js, etc.) utilise cette syntaxe. C'est la base indispensable.

---

## Concepts clés

### `const` et `let` — remplaçants de `var`
Avant ES6, on utilisait `var` pour déclarer des variables. Le problème : `var` est capricieux et peut créer des bugs.

```js
// Avant ES6
var age = 20;

// Avec ES6
const age = 20;  // valeur qui ne change jamais
let score = 0;   // valeur qui peut changer
score = 10;      // ✅ autorisé
age = 21;        // ❌ erreur, const ne peut pas changer
```

---

### Les arrow functions — fonctions fléchées
Une syntaxe plus courte pour écrire des fonctions.

```js
// Fonction classique
function addition(a, b) {
  return a + b;
}

// Arrow function
const addition = (a, b) => a + b;
```

---

### Template literals — les chaînes de caractères améliorées
Plus besoin de concaténer avec `+`.

```js
const name = "Alice";

// Avant
console.log("Bonjour " + name + " !");

// Avec ES6
console.log(`Bonjour ${name} !`);
```

---

### Destructuring — décomposer un objet ou tableau
```js
const student = { name: "Alice", age: 20 };

// Avant
const name = student.name;
const age = student.age;

// Avec ES6
const { name, age } = student;
```

---

### Spread operator `...`
```js
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];

const combined = [...arr1, ...arr2]; // [1, 2, 3, 4, 5, 6]
```

---

## Résumé

| Concept | Utilité |
|---|---|
| `const` / `let` | Remplace `var`, plus fiable |
| Arrow functions | Syntaxe courte pour les fonctions |
| Template literals | Chaînes de caractères dynamiques |
| Destructuring | Extraire des valeurs facilement |
| Spread `...` | Fusionner ou copier des tableaux/objets |
