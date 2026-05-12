# ES6 Classes

## Introduction
Les classes permettent de créer des **modèles d'objets**. C'est comme un moule : tu définis une fois la forme, et tu peux créer autant d'objets que tu veux à partir de ce moule.

**Pourquoi on l'apprend ?** La programmation orientée objet (POO) est un paradigme fondamental utilisé dans presque tous les langages.

---

## Concepts clés

### Créer une classe
```js
class Animal {
  constructor(name, sound) {
    this.name = name;
    this.sound = sound;
  }

  speak() {
    console.log(`${this.name} fait ${this.sound}`);
  }
}

const cat = new Animal("Chat", "miaou");
cat.speak(); // Chat fait miaou
```

---

### L'héritage — `extends`
Une classe peut **hériter** d'une autre et réutiliser ses propriétés.

```js
class Dog extends Animal {
  constructor(name) {
    super(name, "wouf"); // appelle le constructor du parent
  }

  fetch() {
    console.log(`${this.name} rapporte la balle !`);
  }
}

const dog = new Dog("Rex");
dog.speak();  // Rex fait wouf
dog.fetch();  // Rex rapporte la balle !
```

---

### Getters et Setters
Contrôler l'accès aux propriétés d'une classe.

```js
class Student {
  constructor(name) {
    this._name = name;
  }

  get name() {
    return this._name.toUpperCase();
  }

  set name(value) {
    this._name = value;
  }
}

const s = new Student("alice");
console.log(s.name); // ALICE
```

---

## Résumé

| Concept | Utilité |
|---|---|
| `class` | Créer un modèle d'objet |
| `constructor` | Initialiser les propriétés |
| `extends` | Hériter d'une autre classe |
| `super` | Appeler le parent |
| `get` / `set` | Contrôler l'accès aux propriétés |
