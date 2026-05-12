# Cours complet — ES6 Basic

---

# PARTIE 1 — THÉORIE

---

## 1. Pourquoi ES6 ?

Avant 2015, JavaScript avait beaucoup de limitations. ES6 (aussi appelé ES2015) est une mise à jour majeure qui a introduit une syntaxe plus moderne, plus lisible et plus fiable.

> Analogie : ES5 c'est un vieux téléphone à touches. ES6 c'est le même téléphone mais avec un écran tactile — mêmes fonctions de base, mais bien plus agréable à utiliser.

---

## 2. `const` et `let` — remplacer `var`

Avant ES6, on utilisait uniquement `var`. Le problème : `var` a des comportements surprenants liés à la **portée** (scope).

### `const` — valeur qui ne change jamais

```js
const age = 20;
age = 21; // ❌ TypeError : impossible de réassigner une const
```

Utilise `const` par défaut pour tout ce qui ne change pas.

### `let` — valeur qui peut changer

```js
let score = 0;
score = 10; // ✅ autorisé
```

### La portée de bloc

`const` et `let` sont **block-scoped** : ils n'existent qu'à l'intérieur du bloc `{}` où ils sont déclarés.

```js
if (true) {
  const x = 5;
  let y = 10;
}
console.log(x); // ❌ ReferenceError — x n'existe pas ici
console.log(y); // ❌ ReferenceError — y n'existe pas ici
```

`var` au contraire "fuit" hors du bloc :

```js
if (true) {
  var z = 5;
}
console.log(z); // ✅ 5 — var ignore les blocs !
```

### Piège courant

```js
// Dans un if, const redéclare une NOUVELLE variable locale
const task = false;
if (true) {
  const task = true; // nouvelle variable, n'affecte pas celle du dessus
}
console.log(task); // false — la variable d'origine est inchangée
```

---

## 3. Les arrow functions — fonctions fléchées

Une syntaxe plus courte pour écrire des fonctions anonymes.

```js
// Fonction classique
function addition(a, b) {
  return a + b;
}

// Arrow function équivalente
const addition = (a, b) => a + b;

// Avec un seul paramètre, pas besoin de parenthèses
const double = n => n * 2;

// Avec un corps multiligne
const greet = (name) => {
  const message = `Bonjour ${name}`;
  return message;
};
```

### `this` dans les arrow functions

C'est la différence principale avec les fonctions classiques. Une arrow function **hérite du `this`** du contexte où elle est définie.

```js
function getNeighborhoodsList() {
  this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];
  const self = this; // astuce classique avant ES6

  // Arrow function : this = le contexte parent (getNeighborhoodsList)
  this.addNeighborhood = (newNeighborhood) => {
    self.sanFranciscoNeighborhoods.push(newNeighborhood);
    return self.sanFranciscoNeighborhoods;
  };
}
```

---

## 4. Paramètres par défaut

Tu peux définir une valeur par défaut pour un paramètre si aucune valeur n'est passée.

```js
// Sans valeur par défaut
function greet(name) {
  return `Bonjour ${name}`; // "Bonjour undefined" si pas d'argument
}

// Avec valeur par défaut
function greet(name = 'inconnu') {
  return `Bonjour ${name}`; // "Bonjour inconnu" si pas d'argument
}

greet();          // "Bonjour inconnu"
greet('Alice');   // "Bonjour Alice"
```

---

## 5. Le rest parameter `...args`

Permet à une fonction de recevoir un **nombre illimité d'arguments** sous forme de tableau.

```js
function sum(...numbers) {
  return numbers.reduce((total, n) => total + n, 0);
}

sum(1, 2, 3);       // 6
sum(1, 2, 3, 4, 5); // 15
```

`...args` est toujours le **dernier** paramètre.

```js
function log(prefix, ...messages) {
  messages.forEach(msg => console.log(`${prefix}: ${msg}`));
}
log('INFO', 'démarrage', 'connexion', 'prêt');
```

---

## 6. Le spread operator `...`

Même syntaxe que le rest, mais usage inverse : **étaler** les éléments d'un tableau ou objet.

```js
// Fusionner deux tableaux
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combined = [...arr1, ...arr2]; // [1, 2, 3, 4, 5, 6]

// Étaler une string en tableau de caractères
const chars = [...'hello']; // ['h', 'e', 'l', 'l', 'o']

// Copier un tableau
const copy = [...arr1]; // [1, 2, 3] — copie indépendante
```

---

## 7. Template literals — chaînes de caractères améliorées

Utilise des backticks `` ` `` au lieu de guillemets. Permet d'insérer des variables directement avec `${}`.

```js
const name = 'Alice';
const age = 20;

// Avant ES6
console.log('Bonjour ' + name + ', tu as ' + age + ' ans');

// Avec ES6
console.log(`Bonjour ${name}, tu as ${age} ans`);

// On peut mettre n'importe quelle expression dans ${}
console.log(`2 + 2 = ${2 + 2}`); // "2 + 2 = 4"
console.log(`Majeur : ${age >= 18 ? 'oui' : 'non'}`);
```

---

## 8. Shorthand properties — propriétés raccourcies

Quand le nom de la variable et le nom de la propriété sont identiques, tu peux l'écrire une seule fois.

```js
const income = 50000;
const gdp = 100000;

// Avant ES6
const budget = { income: income, gdp: gdp };

// Avec ES6
const budget = { income, gdp }; // exactement pareil
```

---

## 9. Computed property names — clés dynamiques

Tu peux utiliser une expression comme clé d'objet en la mettant entre `[]`.

```js
const year = 2024;

// Clé dynamique
const budget = {
  [`income-${year}`]: 50000,
  [`gdp-${year}`]: 100000,
};

// Résultat : { 'income-2024': 50000, 'gdp-2024': 100000 }
```

---

## 10. Spread dans les objets

Le spread `...` fonctionne aussi avec les objets pour les fusionner ou copier.

```js
const base = { a: 1, b: 2 };
const extended = { ...base, c: 3 }; // { a: 1, b: 2, c: 3 }
```

---

## 11. Boucle `for...of`

Itère sur les **valeurs** d'un tableau (contrairement à `for...in` qui itère sur les indices).

```js
const fruits = ['pomme', 'banane', 'cerise'];

for (const fruit of fruits) {
  console.log(fruit); // 'pomme', 'banane', 'cerise'
}
```

---

## 12. ES6 modules — `import` / `export`

Dans ce projet, les fichiers utilisent la syntaxe ES6 modules.

```js
// Exporter une valeur par défaut
export default function maFonction() { ... }

// Exporter plusieurs valeurs nommées
export function funcA() { ... }
export function funcB() { ... }

// Importer la valeur par défaut
import maFonction from './mon-fichier.js';

// Importer des valeurs nommées
import { funcA, funcB } from './mon-fichier.js';
```

---

---

# PARTIE 2 — WALKTHROUGH DES TÂCHES

---

## Tâche 0 — `const` et `let`

**Objectif :** Utiliser `const` pour une valeur fixe et `let` pour une valeur modifiable.

### Code complet

```js
export function taskFirst() {
  const task = 'I prefer const when I can.';
  return task;
}

export function getLast() {
  return ' is okay';
}

export function taskNext() {
  let combination = 'But sometimes let';
  combination += getLast();
  return combination;
}
```

### Explication

**`const task`** — la valeur `'I prefer const when I can.'` ne change jamais dans cette fonction. `const` est le bon choix.

**`let combination`** — la valeur est d'abord `'But sometimes let'`, puis on lui concatène `getLast()`. Elle change, donc `let` est obligatoire.

**`combination += getLast()`** — équivalent à `combination = combination + getLast()`.

---

## Tâche 1 — Portée de bloc

**Objectif :** Montrer que `const` à l'intérieur d'un `if` crée une nouvelle variable locale.

### Code complet

```js
export default function taskBlock(trueOrFalse) {
  const task = false;
  const task2 = true;

  if (trueOrFalse) {
    const task = true;   // nouvelle variable, locale au bloc if
    const task2 = false; // nouvelle variable, locale au bloc if
  }

  return [task, task2]; // retourne les variables du scope externe : [false, true]
}
```

### Explication

Les deux `const task` et `const task2` à l'intérieur du `if` sont des **variables distinctes** des deux du dessus. Grâce à la portée de bloc de `const`, elles n'existent que dans le `{}` du `if`. La fonction retourne toujours `[false, true]` peu importe l'argument.

---

## Tâche 2 — Arrow function et `this`

**Objectif :** Remplacer une fonction classique par une arrow function pour hériter du contexte `this`.

### Code complet

```js
export default function getNeighborhoodsList() {
  this.sanFranciscoNeighborhoods = ['SOMA', 'Union Square'];

  const self = this;
  this.addNeighborhood = (newNeighborhood) => {
    self.sanFranciscoNeighborhoods.push(newNeighborhood);
    return self.sanFranciscoNeighborhoods;
  };
}
```

### Explication

**`this.sanFranciscoNeighborhoods`** — propriété attachée à l'instance créée avec `new getNeighborhoodsList()`.

**`const self = this`** — capture le `this` du contexte parent pour l'utiliser dans l'arrow function.

**Arrow function `(newNeighborhood) => { ... }`** — hérite du `this` de `getNeighborhoodsList`, donc `self` pointe bien vers l'instance.

---

## Tâche 3 — Paramètres par défaut

**Objectif :** Réécrire une fonction avec des valeurs par défaut pour ses paramètres.

### Code complet

```js
export default (initialNumber, expansion1989 = 89, expansion2019 = 19) =>
  initialNumber + expansion1989 + expansion2019;
```

### Explication

Si `expansion1989` ou `expansion2019` ne sont pas fournis, ils valent respectivement `89` et `19`. C'est une arrow function anonyme exportée directement — pas besoin de `function` ni de nom.

---

## Tâche 4 — Rest parameter

**Objectif :** Compter le nombre d'arguments passés à une fonction.

### Code complet

```js
export default function returnHowManyArguments(...args) {
  return args.length;
}
```

### Explication

`...args` capture tous les arguments dans un tableau. `args.length` est simplement la taille de ce tableau. Peu importe combien d'arguments tu passes, ils seront tous capturés.

---

## Tâche 5 — Spread operator

**Objectif :** Concaténer deux tableaux et les caractères d'une string.

### Code complet

```js
export default function concatArrays(array1, array2, string) {
  return [...array1, ...array2, ...string];
}
```

### Explication

`...array1` étale les éléments du premier tableau, `...array2` ceux du second, `...string` étale les caractères de la string (une string est itérable en JS). Le tout est assemblé dans un nouveau tableau.

---

## Tâche 6 — Template literals

**Objectif :** Réécrire une string avec des template literals.

### Code complet

```js
export default function getSanFranciscoDescription() {
  const year = 2017;
  const budget = {
    income: '$119,868',
    gdp: '$154.2 billion',
    capita: '$178,479',
  };

  return `As of ${year}, it was the seventh-highest income county in the United States, with a per capita personal income of ${budget.income}. As of 2015, San Francisco proper had a GDP of ${budget.gdp}, and a GDP per capita of ${budget.capita}.`;
}
```

### Explication

Les backticks permettent d'insérer directement `${year}`, `${budget.income}`, etc. sans concaténation. Le code est bien plus lisible qu'avec des `+`.

---

## Tâche 7 — Shorthand properties

**Objectif :** Créer un objet avec la syntaxe raccourcie.

### Code complet

```js
export default function getBudgetObject(income, gdp, capita) {
  const budget = { income, gdp, capita };
  return budget;
}
```

### Explication

Comme les paramètres et les clés ont le même nom, on peut écrire `{ income, gdp, capita }` au lieu de `{ income: income, gdp: gdp, capita: capita }`.

---

## Tâche 8 — Computed property names

**Objectif :** Créer un objet avec des clés dynamiques basées sur l'année courante.

### Code complet

```js
function getCurrentYear() {
  const date = new Date();
  return date.getFullYear();
}

export default function getBudgetForCurrentYear(income, gdp, capita) {
  const budget = {
    [`income-${getCurrentYear()}`]: income,
    [`gdp-${getCurrentYear()}`]: gdp,
    [`capita-${getCurrentYear()}`]: capita,
  };
  return budget;
}
```

### Explication

Les `[]` autour de la clé permettent d'utiliser une expression comme nom de propriété. `getCurrentYear()` retourne l'année courante, ce qui donne des clés comme `'income-2024'`.

---

## Tâche 9 — Spread dans les objets

**Objectif :** Étendre un objet existant avec de nouvelles propriétés.

### Code complet

```js
import getBudgetObject from './7-getBudgetObject.js';

export default function getFullBudgetObject(income, gdp, capita) {
  const budget = getBudgetObject(income, gdp, capita);
  const fullBudget = {
    ...budget,
    getIncomeInDollars(income) {
      return `$${income}`;
    },
    getIncomeInEuros(income) {
      return `${income} euros`;
    },
  };
  return fullBudget;
}
```

### Explication

`...budget` copie toutes les propriétés de `budget` dans le nouvel objet. Ensuite on ajoute deux méthodes. Le résultat est un objet qui contient à la fois les données de `budget` et les nouvelles méthodes.

---

## Tâche 10 — `for...of`

**Objectif :** Remplacer une boucle `for...in` par `for...of`.

### Code complet

```js
export default function appendToEachArrayValue(array, appendString) {
  const result = [];

  for (const value of array) {
    result.push(appendString + value);
  }

  return result;
}
```

### Explication

`for...of` itère sur les **valeurs** du tableau directement. On construit un nouveau tableau `result` avec chaque valeur préfixée par `appendString`.

---

## Tâche 11 — Computed property names avec paramètre

**Objectif :** Créer un objet avec une clé dynamique basée sur un paramètre.

### Code complet

```js
export default function createEmployeesObject(departmentName, employees) {
  const employeesObject = {
    [departmentName]: employees,
  };
  return employeesObject;
}
```

### Explication

`[departmentName]` utilise la valeur du paramètre comme clé. Si `departmentName = 'Engineering'` et `employees = ['Alice', 'Bob']`, le résultat est `{ Engineering: ['Alice', 'Bob'] }`.

---

## Tâche 12 — Méthode dans un objet

**Objectif :** Créer un objet avec une méthode qui compte ses propres clés.

### Code complet

```js
export default function createReportObject(employeesList) {
  const reportObject = {
    allEmployees: employeesList,
    getNumberOfDepartments(employees) {
      return Object.keys(employees).length;
    },
  };
  return reportObject;
}
```

### Explication

`getNumberOfDepartments` est une méthode de l'objet. `Object.keys(employees)` retourne un tableau des clés de l'objet `employees`, et `.length` donne le nombre de clés = nombre de départements.

---

---

# PARTIE 3 — TABLEAU RÉCAPITULATIF

| Tâche | Fichier | Concepts clés |
|---|---|---|
| 0 | `0-constants.js` | `const`, `let`, différence avec `var` |
| 1 | `1-block-scoped.js` | Portée de bloc avec `const`/`let` |
| 2 | `2-arrow.js` | Arrow functions, `this`, portée |
| 3 | `3-default-parameter.js` | Paramètres par défaut |
| 4 | `4-rest-parameter.js` | Rest parameter `...args` |
| 5 | `5-spread-operator.js` | Spread operator `...` sur tableaux et strings |
| 6 | `6-string-interpolation.js` | Template literals, `${}` |
| 7 | `7-getBudgetObject.js` | Shorthand properties |
| 8 | `8-getBudgetCurrentYear.js` | Computed property names `[expr]` |
| 9 | `9-getFullBudget.js` | Spread dans les objets, méthodes |
| 10 | `10-loops.js` | `for...of` |
| 11 | `11-createEmployeesObject.js` | Computed property names avec paramètre |
| 12 | `12-createReportObject.js` | `Object.keys()`, méthodes dans un objet |
