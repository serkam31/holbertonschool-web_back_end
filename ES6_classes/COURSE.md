# Cours complet — ES6 Classes

---

# PARTIE 1 — THÉORIE

---

## 1. Qu'est-ce qu'une classe ?

Une classe est un **modèle** pour créer des objets. Tu la définis une fois, puis tu peux créer autant d'objets que tu veux à partir de ce modèle.

> Analogie : une classe c'est comme un moule à gâteau. Le moule définit la forme. Chaque gâteau que tu fais avec ce moule est une **instance** de ce moule.

```js
class Animal {
  constructor(name, sound) {
    this.name = name;   // propriété de l'instance
    this.sound = sound;
  }

  speak() { // méthode de la classe
    return `${this.name} fait ${this.sound}`;
  }
}

const cat = new Animal('Chat', 'miaou'); // instance
cat.speak(); // "Chat fait miaou"
```

---

## 2. Le `constructor`

C'est la méthode spéciale appelée automatiquement quand tu crées une instance avec `new`. Elle initialise les propriétés de l'objet.

```js
class ClassRoom {
  constructor(maxStudentsSize) {
    this._maxStudentsSize = maxStudentsSize; // _ = convention "propriété privée"
  }
}

const room = new ClassRoom(30);
// room._maxStudentsSize = 30
```

### La convention `_`

En JS, il n'existe pas de vraie propriété privée dans les classes ES6 classiques. La convention est de préfixer avec `_` pour signaler que la propriété ne doit pas être modifiée directement.

---

## 3. Getters et Setters

Ils permettent de **contrôler l'accès** aux propriétés d'une classe.

```js
class HolbertonCourse {
  constructor(name) {
    this._name = name;
  }

  get name() {          // appelé quand tu fais objet.name
    return this._name;
  }

  set name(value) {     // appelé quand tu fais objet.name = 'xxx'
    if (typeof value !== 'string') {
      throw new TypeError('Name must be a string');
    }
    this._name = value;
  }
}

const course = new HolbertonCourse('Math');
console.log(course.name); // appelle le getter → 'Math'
course.name = 42;         // appelle le setter → TypeError !
```

### Pourquoi utiliser des getters/setters ?

- **Validation** : vérifier le type ou la valeur avant d'assigner
- **Encapsulation** : cacher la propriété interne `_name` et n'exposer que l'interface publique

---

## 4. Les méthodes statiques

Une méthode `static` appartient à la **classe elle-même**, pas aux instances.

```js
class Pricing {
  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}

// Appel direct sur la classe, pas sur une instance
Pricing.convertPrice(100, 1.2); // 120

// ❌ Ne fonctionne pas sur une instance
const p = new Pricing();
p.convertPrice(100, 1.2); // TypeError
```

---

## 5. L'héritage — `extends` et `super`

Une classe peut **hériter** d'une autre pour réutiliser son code.

```js
class Building {
  constructor(sqft) {
    this._sqft = sqft;
  }
  get sqft() { return this._sqft; }
}

class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft); // appelle le constructor de Building
    this._floors = floors;
  }
  get floors() { return this._floors; }
}

const tower = new SkyHighBuilding(10000, 50);
tower.sqft;   // 10000 — hérité de Building
tower.floors; // 50 — propre à SkyHighBuilding
```

### `super` obligatoire

Dans le `constructor` d'une classe qui hérite, **`super()` doit être appelé avant d'utiliser `this`**. Sans ça, une erreur `ReferenceError` est lancée.

---

## 6. Les méthodes abstraites (pattern)

JavaScript n'a pas de méthodes abstraites natives, mais on peut simuler ce comportement en lançant une erreur dans la méthode parent.

```js
class Building {
  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}

class SkyHighBuilding extends Building {
  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`; // Override obligatoire
  }
}
```

Si une sous-classe ne redéfinit pas la méthode, l'erreur du parent est lancée.

---

## 7. `toString()` et `valueOf()`

Ces méthodes spéciales contrôlent comment un objet est converti en string ou en nombre.

```js
class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  valueOf() { return this._size; }     // appelé lors de conversions numériques
  toString() { return this._location; } // appelé lors de conversions en string
}

const hc = new HolbertonClass(12, 'Malibu');
Number(hc);  // 12  — appelle valueOf()
String(hc);  // 'Malibu' — appelle toString()
hc + 1;      // 13  — appelle valueOf()
```

---

## 8. Le hoisting des classes

Contrairement aux fonctions, les **classes ne sont pas hoistées**. Tu ne peux pas utiliser une classe avant de la déclarer.

```js
const obj = new MyClass(); // ❌ ReferenceError
class MyClass {}
```

C'est pourquoi dans `9-hoisting.js`, l'ordre de déclaration des classes est important.

---

## 9. `Symbol` pour le clonage

`Symbol` est un type primitif unique — chaque `Symbol()` crée une valeur garantie unique.

```js
const sym = Symbol('description');
// sym est unique — jamais égal à un autre Symbol
```

Utilisé comme clé de méthode, il crée une interface semi-privée :

```js
class Car {
  cloneCar() {
    return new this.constructor(this._brand, this._motor, this._color);
  }
}
```

`this.constructor` est une référence à la classe de l'instance courante, ce qui permet à une sous-classe de cloner ses propres instances.

---

---

# PARTIE 2 — WALKTHROUGH DES TÂCHES

---

## Tâche 0 — Créer une classe simple

**Objectif :** Créer une classe `ClassRoom` avec une propriété `_maxStudentsSize`.

### Code complet

```js
export default class ClassRoom {
  constructor(maxStudentsSize) {
    this._maxStudentsSize = maxStudentsSize;
  }
}
```

### Explication

**`constructor(maxStudentsSize)`** — reçoit la taille max en paramètre.
**`this._maxStudentsSize = maxStudentsSize`** — stocke la valeur sur l'instance. Le `_` signale que c'est une propriété "interne".

---

## Tâche 1 — Instancier une classe

**Objectif :** Créer une fonction qui retourne un tableau de 3 instances de `ClassRoom`.

### Code complet

```js
import ClassRoom from './0-classroom.js';

export default function initializeRooms() {
  const room1 = new ClassRoom(19);
  const room2 = new ClassRoom(20);
  const room3 = new ClassRoom(34);
  return [room1, room2, room3];
}
```

### Explication

`new ClassRoom(19)` crée une instance avec `_maxStudentsSize = 19`. On crée 3 instances avec des tailles différentes et on les retourne dans un tableau.

---

## Tâche 2 — Getters et setters avec validation

**Objectif :** Créer une classe `HolbertonCourse` avec validation des types.

### Code complet

```js
export default class HolbertonCourse {
  constructor(name = '', length = 0, students = ['']) {
    this._name = name;
    this._length = length;
    this._students = students;
  }

  get name() { return this._name; }
  set name(value) {
    if (typeof value !== 'string') throw new TypeError('Name must be a string');
    this._name = value;
  }

  get length() { return this._length; }
  set length(value) {
    if (typeof value !== 'number') throw new TypeError('Length must be a number');
    this._length = value;
  }

  get students() { return this._students; }
  set students(value) {
    if (!Array.isArray(value) || !value.every(s => typeof s === 'string')) {
      throw new TypeError('Students must be an array of strings');
    }
    this._students = value;
  }
}
```

### Explication

Chaque setter valide le type avant d'assigner. Si le type est incorrect, un `TypeError` est lancé. Les getters retournent simplement la valeur interne. Les valeurs par défaut dans le constructor évitent les `undefined`.

---

## Tâche 3 — Méthode d'affichage

**Objectif :** Créer une classe `Currency` avec une méthode qui formate l'affichage.

### Code complet

```js
export default class Currency {
  constructor(code, name) {
    this._code = code;
    this._name = name;
  }

  get code() { return this._code; }
  set code(value) {
    if (typeof value !== 'string') throw new TypeError('Code must be a string');
    this._code = value;
  }

  get name() { return this._name; }
  set name(value) {
    if (typeof value !== 'string') throw new TypeError('Name must be a string');
    this._name = value;
  }

  displayFullCurrency() {
    return `${this._name} (${this._code})`;
  }
}
```

### Explication

`displayFullCurrency()` est une méthode normale (ni getter ni setter). Elle formate et retourne une string lisible. Exemple : `new Currency('USD', 'Dollar').displayFullCurrency()` → `'Dollar (USD)'`.

---

## Tâche 4 — Classe qui utilise une autre classe + méthode statique

**Objectif :** Créer `Pricing` qui utilise `Currency` et expose une conversion statique.

### Code complet

```js
import Currency from './3-currency.js';

export default class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  get amount() { return this._amount; }
  set amount(value) {
    if (typeof value !== 'number') throw new TypeError('Amount must be a number');
    this._amount = value;
  }

  get currency() { return this._currency; }
  set currency(value) {
    if (!(value instanceof Currency)) throw new TypeError('Currency must be an instance of Currency class');
    this._currency = value;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.displayFullCurrency()}`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}
```

### Explication

**`value instanceof Currency`** — vérifie que la valeur est bien une instance de la classe `Currency`.
**`static convertPrice`** — accessible directement sur la classe : `Pricing.convertPrice(100, 1.2)`.
**`displayFullPrice`** — appelle `displayFullCurrency()` de l'instance `Currency` stockée.

---

## Tâche 5 — Classe abstraite simulée

**Objectif :** Forcer les sous-classes à implémenter `evacuationWarningMessage`.

### Code complet

```js
export default class Building {
  constructor(sqft) {
    this._sqft = sqft;
  }

  get sqft() { return this._sqft; }

  evacuationWarningMessage() {
    throw new Error('Class extending Building must override evacuationWarningMessage');
  }
}
```

### Explication

Si une sous-classe n'override pas `evacuationWarningMessage()` et que quelqu'un l'appelle, l'erreur du parent est lancée. C'est un pattern pour simuler une méthode abstraite.

---

## Tâche 6 — Héritage

**Objectif :** Créer `SkyHighBuilding` qui hérite de `Building` et override la méthode.

### Code complet

```js
import Building from './5-building.js';

export default class SkyHighBuilding extends Building {
  constructor(sqft, floors) {
    super(sqft);
    this._floors = floors;
  }

  get floors() { return this._floors; }

  evacuationWarningMessage() {
    return `Evacuate slowly the ${this.floors} floors`;
  }
}
```

### Explication

**`super(sqft)`** — appelle le constructor de `Building` pour initialiser `_sqft`.
**`evacuationWarningMessage()`** — override la méthode du parent avec une vraie implémentation.
**`this.floors`** — utilise le getter défini dans cette classe.

---

## Tâche 7 — `toString()` personnalisé

**Objectif :** Contrôler la conversion en string d'un objet `Airport`.

### Code complet

```js
export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  toString() {
    return `[object ${this._code}]`;
  }
}
```

### Explication

`toString()` est appelée automatiquement quand l'objet est utilisé dans un contexte de string. `new Airport('TAV', 'DAL').toString()` retourne `'[object DAL]'`.

---

## Tâche 8 — `valueOf()` et `toString()`

**Objectif :** Contrôler les conversions numériques et string.

### Code complet

```js
export default class HolbertonClass {
  constructor(size, location) {
    this._size = size;
    this._location = location;
  }

  valueOf() { return this._size; }
  toString() { return this._location; }
}
```

### Explication

`valueOf()` est appelée lors des opérations arithmétiques (`+`, `-`, etc.). `toString()` lors des conversions en string. Cela permet d'utiliser une instance de la classe comme si c'était un nombre ou une string selon le contexte.

---

## Tâche 9 — Hoisting et ordre de déclaration

**Objectif :** Corriger un problème de hoisting en déclarant les classes dans le bon ordre.

### Code complet

```js
export class HolbertonClass {
  constructor(year, location) {
    this._year = year;
    this._location = location;
  }
  get year() { return this._year; }
  get location() { return this._location; }
}

export class StudentHolberton {
  constructor(firstName, lastName, holbertonClass) {
    this._firstName = firstName;
    this._lastName = lastName;
    this._holbertonClass = holbertonClass;
  }
  get fullName() { return `${this._firstName} ${this._lastName}`; }
  get holbertonClass() { return this._holbertonClass; }
  get fullStudentDescription() {
    return `${this._firstName} ${this._lastName} - ${this._holbertonClass.year} - ${this._holbertonClass.location}`;
  }
}
```

### Explication

`HolbertonClass` doit être déclarée **avant** `StudentHolberton` car `StudentHolberton` l'utilise. Les classes ne sont pas hoistées donc l'ordre compte.

---

## Tâche 10 — Clonage avec `this.constructor`

**Objectif :** Créer une méthode `cloneCar` qui retourne une copie de l'instance.

### Code complet

```js
export default class Car {
  constructor(brand, motor, color) {
    this._brand = brand;
    this._motor = motor;
    this._color = color;
  }

  cloneCar() {
    return new this.constructor(this._brand, this._motor, this._color);
  }
}
```

### Explication

**`this.constructor`** — référence à la classe de l'instance courante. Si une sous-classe hérite de `Car` et appelle `cloneCar()`, elle obtiendra une instance de la sous-classe, pas de `Car`. C'est plus flexible que `new Car(...)`.

---

---

# PARTIE 3 — TABLEAU RÉCAPITULATIF

| Tâche | Fichier | Concepts clés |
|---|---|---|
| 0 | `0-classroom.js` | `class`, `constructor`, `this._prop` |
| 1 | `1-make_classrooms.js` | `new`, instanciation, `import` |
| 2 | `2-hbtn_course.js` | Getters, setters, validation de type, `TypeError` |
| 3 | `3-currency.js` | Méthode d'instance, template literal |
| 4 | `4-pricing.js` | `instanceof`, méthode `static`, composition de classes |
| 5 | `5-building.js` | Méthode abstraite simulée, `throw new Error` |
| 6 | `6-sky_high.js` | `extends`, `super()`, override de méthode |
| 7 | `7-airport.js` | `toString()` personnalisé |
| 8 | `8-hbtn_class.js` | `valueOf()`, conversions implicites |
| 9 | `9-hoisting.js` | Hoisting des classes, ordre de déclaration |
| 10 | `10-car.js` | `this.constructor`, clonage d'instance |
