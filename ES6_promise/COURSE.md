# Cours complet — ES6 Promise

---

# PARTIE 1 — THÉORIE

---

## 1. Pourquoi les Promises ?

En JavaScript, certaines opérations prennent du temps : appels API, lecture de fichiers, temporisations. Sans Promises, on utilisait des **callbacks** — des fonctions passées en argument et appelées plus tard.

```js
// Callbacks — devient vite illisible ("callback hell")
fetchUser(id, (user) => {
  fetchPosts(user.id, (posts) => {
    fetchComments(posts[0].id, (comments) => {
      // ...
    });
  });
});
```

Les Promises permettent d'écrire ce même code de façon linéaire et lisible.

---

## 2. Qu'est-ce qu'une Promise ?

Une Promise représente une **valeur future**. Elle peut être dans 3 états :

| État | Signification |
|---|---|
| **Pending** | En attente — l'opération n'est pas encore terminée |
| **Fulfilled** | Réussie — la valeur est disponible |
| **Rejected** | Échouée — une erreur s'est produite |

> Analogie : tu commandes un colis en ligne. Tu as un numéro de suivi (la Promise). Le colis est soit en transit (pending), soit livré (fulfilled), soit perdu (rejected).

---

## 3. Créer une Promise

```js
const promise = new Promise((resolve, reject) => {
  const success = true;

  if (success) {
    resolve('Opération réussie !'); // passe en fulfilled
  } else {
    reject(new Error('Quelque chose a raté')); // passe en rejected
  }
});
```

`resolve` et `reject` sont des fonctions fournies par JS. Tu appelles l'une ou l'autre selon le résultat.

---

## 4. Consommer une Promise — `.then()` et `.catch()`

```js
promise
  .then((result) => {
    console.log(result); // "Opération réussie !"
  })
  .catch((error) => {
    console.log(error.message); // "Quelque chose a raté"
  });
```

- `.then()` reçoit la valeur de `resolve`
- `.catch()` reçoit l'erreur de `reject`
- Les deux retournent de nouvelles Promises, donc on peut les **chaîner**

---

## 5. `.finally()` — toujours exécuté

`.finally()` s'exécute après la Promise, qu'elle réussisse ou échoue.

```js
promise
  .then(result => console.log(result))
  .catch(err => console.log(err))
  .finally(() => console.log('Toujours exécuté'));
```

---

## 6. `Promise.resolve()` et `Promise.reject()`

Créer une Promise déjà résolue ou rejetée immédiatement :

```js
Promise.resolve({ firstName: 'Alice', lastName: 'Doe' });
// Équivalent à new Promise((resolve) => resolve({ firstName: 'Alice', ... }))

Promise.reject(new Error('Erreur immédiate'));
```

Utile pour retourner une Promise uniforme depuis une fonction.

---

## 7. `Promise.all()` — attendre toutes les Promises

`Promise.all()` attend que **toutes** les Promises réussissent. Si une seule échoue, tout échoue.

```js
Promise.all([promise1, promise2, promise3])
  .then(([result1, result2, result3]) => {
    // toutes ont réussi
  })
  .catch((error) => {
    // au moins une a échoué
  });
```

---

## 8. `Promise.allSettled()` — attendre toutes, sans échouer

`Promise.allSettled()` attend que **toutes** les Promises se terminent, qu'elles réussissent ou échouent. Elle ne rejette jamais.

```js
Promise.allSettled([promise1, promise2])
  .then((results) => {
    results.forEach((result) => {
      if (result.status === 'fulfilled') {
        console.log(result.value);
      } else {
        console.log(result.reason);
      }
    });
  });
```

Chaque résultat a un `status` (`'fulfilled'` ou `'rejected'`) et soit `value` soit `reason`.

---

## 9. `Promise.race()` — la plus rapide gagne

`Promise.race()` résout ou rejette avec la **première Promise terminée**.

```js
Promise.race([slowDownload, fastDownload])
  .then((result) => {
    // result vient du téléchargement le plus rapide
  });
```

---

## 10. `async` / `await`

Syntaxe plus lisible pour travailler avec les Promises.

```js
// Avec .then()
fetchUser().then(user => fetchPosts(user.id)).then(posts => console.log(posts));

// Avec async/await — plus lisible
async function main() {
  const user = await fetchUser();
  const posts = await fetchPosts(user.id);
  console.log(posts);
}
```

**`async`** devant une fonction la fait toujours retourner une Promise.
**`await`** attend qu'une Promise se résolve avant de continuer.

---

## 11. `try/catch/finally` avec les Promises

```js
function divideFunction(numerator, denominator) {
  if (denominator === 0) {
    throw new Error('cannot divide by 0');
  }
  return numerator / denominator;
}
```

```js
function guardrail(mathFunction) {
  const queue = [];
  try {
    queue.push(mathFunction()); // si ça lance une erreur → catch
  } catch (err) {
    queue.push(String(err));   // capture l'erreur comme string
  } finally {
    queue.push('Guardrail was processed'); // toujours exécuté
    return queue;
  }
}
```

---

---

# PARTIE 2 — WALKTHROUGH DES TÂCHES

---

## Tâche 0 — Retourner une Promise simple

**Objectif :** Créer une fonction qui retourne une Promise résolue à `true`.

### Code complet

```js
export default function getResponseFromAPI() {
  const promise = new Promise((resolve) => {
    resolve(true);
  });
  return promise;
}
```

### Explication

On crée une Promise avec `new Promise(...)`. Le `resolve(true)` la met immédiatement en état `fulfilled` avec la valeur `true`. La fonction retourne cette Promise.

---

## Tâche 1 — Promise conditionnelle

**Objectif :** Résoudre ou rejeter selon un paramètre booléen.

### Code complet

```js
export default function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success) {
      resolve({ status: 200, body: 'Success' });
    } else {
      reject(new Error('The fake API is not working currently'));
    }
  });
}
```

### Explication

Si `success` est `true`, on résout avec un objet `{ status, body }`. Sinon, on rejette avec un objet `Error`. `new Error(...)` crée un objet erreur avec un message — c'est mieux que de rejeter une simple string.

---

## Tâche 2 — Gérer `.then()` et `.catch()`

**Objectif :** Ajouter des handlers à une Promise reçue en paramètre.

### Code complet

```js
export default function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      console.log('Got a response from the API');
      return { status: 200, body: 'success' };
    })
    .catch(() => {
      console.log('Got a response from the API');
      return new Error();
    });
}
```

### Explication

La fonction reçoit une Promise existante et y attache des handlers. Dans les deux cas (succès ou échec), on affiche le même message mais on retourne des valeurs différentes. `.then()` et `.catch()` retournent tous les deux de nouvelles Promises, ce qui permet de chaîner.

---

## Tâche 3 — `Promise.all()`

**Objectif :** Lancer deux Promises en parallèle et afficher les résultats combinés.

### Code complet

```js
import { uploadPhoto, createUser } from './utils.js';

export default async function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then((response) => {
      const [photo, user] = response;
      console.log(`${photo.body} ${user.firstName} ${user.lastName}`);
    })
    .catch(() => {
      console.log('Signup system offline');
    });
}
```

### Explication

`Promise.all([...])` lance les deux Promises **en parallèle** et attend qu'elles soient toutes les deux terminées. La destructuration `const [photo, user] = response` extrait les deux résultats dans l'ordre. Si une seule échoue, `.catch()` est déclenché.

---

## Tâche 4 — `Promise.resolve()`

**Objectif :** Retourner une Promise immédiatement résolue avec un objet.

### Code complet

```js
export default function signUpUser(firstName, lastName) {
  return Promise.resolve({ firstName, lastName });
}
```

### Explication

`Promise.resolve(valeur)` crée une Promise déjà résolue. C'est un raccourci pour `new Promise((resolve) => resolve(valeur))`. La shorthand property `{ firstName, lastName }` crée l'objet directement.

---

## Tâche 5 — `Promise.reject()`

**Objectif :** Retourner une Promise immédiatement rejetée.

### Code complet

```js
export default function uploadPhoto(filename) {
  return Promise.reject(new Error(`${filename} cannot be processed`));
}
```

### Explication

`Promise.reject(erreur)` crée une Promise immédiatement rejetée. Le message d'erreur utilise le `filename` passé en paramètre.

---

## Tâche 6 — `Promise.allSettled()`

**Objectif :** Gérer plusieurs Promises même si certaines échouent.

### Code complet

```js
import signUpUser from './4-user-promise.js';
import uploadPhoto from './5-photo-reject.js';

export default function handleProfileSignup(firstName, lastName, filename) {
  return Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(filename)])
    .then((results) =>
      results.map((res) => ({
        status: res.status,
        value: res.status === 'fulfilled' ? res.value : res.reason.toString(),
      }))
    );
}
```

### Explication

`signUpUser` réussit toujours, `uploadPhoto` échoue toujours. `Promise.allSettled` attend les deux et ne rejette pas. Chaque résultat a un `status`. Si `'fulfilled'`, on prend `.value`. Si `'rejected'`, on prend `.reason` et on le convertit en string.

---

## Tâche 7 — `Promise.race()`

**Objectif :** Retourner la première Promise qui se termine.

### Code complet

```js
export default function loadBalancer(chinaDownload, USDownload) {
  return Promise.race([chinaDownload, USDownload]);
}
```

### Explication

`Promise.race()` retourne une nouvelle Promise qui se résout ou se rejette avec la **première** des deux à se terminer. C'est utile pour choisir le serveur le plus rapide.

---

## Tâche 8 — `throw` dans une fonction

**Objectif :** Lancer une erreur si le dénominateur est zéro.

### Code complet

```js
export default function divideFunction(numerator, denominator) {
  if (denominator === 0) {
    throw new Error('cannot divide by 0');
  }
  return numerator / denominator;
}
```

### Explication

`throw new Error(...)` interrompt l'exécution de la fonction et propage une erreur. Si le dénominateur est zéro, la division est impossible et on lance une erreur explicite plutôt que de retourner `Infinity`.

---

## Tâche 9 — `try/catch/finally`

**Objectif :** Exécuter une fonction, capturer les erreurs, et toujours ajouter un message final.

### Code complet

```js
export default function guardrail(mathFunction) {
  const queue = [];
  try {
    queue.push(mathFunction());
  } catch (err) {
    queue.push(String(err));
  } finally {
    queue.push('Guardrail was processed');
    return queue;
  }
}
```

### Explication

**`try`** — appelle `mathFunction()`. Si elle réussit, le résultat est ajouté à `queue`.
**`catch (err)`** — si `mathFunction()` lance une erreur, on la capture et on l'ajoute à `queue` sous forme de string.
**`finally`** — toujours exécuté, qu'il y ait eu erreur ou non. Ajoute le message de fin et retourne `queue`.

**`String(err)`** — convertit l'objet Error en string : `'Error: cannot divide by 0'`.

---

---

# PARTIE 3 — TABLEAU RÉCAPITULATIF

| Tâche | Fichier | Concepts clés |
|---|---|---|
| 0 | `0-promise.js` | `new Promise`, `resolve` |
| 1 | `1-promise.js` | `resolve` vs `reject`, `new Error` |
| 2 | `2-then.js` | `.then()`, `.catch()`, chaining |
| 3 | `3-all.js` | `Promise.all()`, destructuring, `async` |
| 4 | `4-user-promise.js` | `Promise.resolve()`, shorthand properties |
| 5 | `5-photo-reject.js` | `Promise.reject()`, template literal |
| 6 | `6-final-user.js` | `Promise.allSettled()`, `status`, `reason` |
| 7 | `7-load_balancer.js` | `Promise.race()` |
| 8 | `8-try.js` | `throw new Error` |
| 9 | `9-try.js` | `try/catch/finally`, `String(err)` |
