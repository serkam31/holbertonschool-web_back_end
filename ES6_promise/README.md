# ES6 Promise

## Introduction
Une **Promise** représente une valeur qui sera disponible **dans le futur**. C'est la solution JavaScript pour gérer les opérations asynchrones (appels API, lecture de fichiers, etc.).

**Analogie :** C'est comme commander un café. Le serveur te donne un ticket (la Promise). Tu ne l'as pas encore, mais tu sais qu'il arrivera (ou pas, si la machine est en panne).

---

## Concepts clés

### Créer une Promise
```js
const promise = new Promise((resolve, reject) => {
  const success = true;

  if (success) {
    resolve("Café prêt !");
  } else {
    reject("Machine en panne !");
  }
});
```

### `.then()` et `.catch()`
```js
promise
  .then(result => console.log(result))   // "Café prêt !"
  .catch(error => console.log(error));   // "Machine en panne !"
```

### `async` / `await` — syntaxe plus lisible
```js
async function getCoffee() {
  try {
    const result = await promise;
    console.log(result);
  } catch (error) {
    console.log(error);
  }
}
```

### `Promise.all` — attendre plusieurs promesses
```js
const p1 = fetch('/api/users');
const p2 = fetch('/api/posts');

Promise.all([p1, p2]).then(([users, posts]) => {
  console.log(users, posts);
});
```

---

## Résumé

| Concept | Utilité |
|---|---|
| `Promise` | Représente une valeur future |
| `.then()` | Que faire si ça réussit |
| `.catch()` | Que faire si ça échoue |
| `async/await` | Syntaxe plus lisible pour les promesses |
| `Promise.all` | Attendre plusieurs promesses en parallèle |
