# Cours complet — Node JS Basics

---

# PARTIE 1 — THÉORIE

---

## 1. Qu'est-ce que Node.js ?

JavaScript a été inventé pour fonctionner dans le navigateur. Le navigateur contient un moteur qui lit et exécute le code JS — dans Chrome ce moteur s'appelle **V8**.

Node.js prend ce même moteur V8 et le fait tourner **en dehors du navigateur**, directement sur ta machine. Résultat : tu peux écrire du JavaScript qui lit des fichiers, ouvre des connexions réseau, répond à des requêtes HTTP, etc.

> Analogie : le navigateur est une voiture. V8 est le moteur. Node.js, c'est prendre ce moteur et le mettre dans un camion — même moteur, usage complètement différent.

Node.js n'est pas un langage. C'est un **environnement d'exécution** pour JavaScript côté serveur.

### Ce que tu peux faire avec Node.js que tu ne pouvais pas faire dans le navigateur

| Navigateur | Node.js |
|---|---|
| Manipuler le DOM | Lire/écrire des fichiers |
| Réagir aux clics | Écouter des connexions réseau |
| Faire des requêtes fetch | Créer un serveur HTTP |
| Pas d'accès au système | Accès complet au système |

---

## 2. La boucle d'événements (Event Loop)

C'est le concept le plus important de Node.js. Node tourne sur **un seul thread** (un seul fil d'exécution). Ça semble être une limitation, mais c'est en réalité une force.

### Comment ça marche

1. Node exécute ton code de haut en bas.
2. Quand il rencontre une opération lente (lire un fichier, attendre une requête réseau), il **ne bloque pas**. Il enregistre une fonction de rappel (callback) et passe à la suite.
3. Quand l'opération se termine, le callback est placé dans une file d'attente.
4. La boucle d'événements récupère ce callback et l'exécute.

> Analogie : tu es au restaurant. Tu passes ta commande (opération lente). Au lieu d'attendre debout à la cuisine, tu retournes t'asseoir et fais autre chose. Quand le plat est prêt, le serveur t'appelle (callback).

```
   ┌───────────────────────────┐
   │        Ton code           │
   └─────────────┬─────────────┘
                 │
   ┌─────────────▼─────────────┐
   │       Event Loop          │◄──── les callbacks s'accumulent ici
   └─────────────┬─────────────┘
                 │
   ┌─────────────▼─────────────┐
   │   Moteur V8 (exécution)   │
   └───────────────────────────┘
```

C'est pourquoi Node.js gère des milliers de connexions simultanées efficacement — il ne bloque jamais le thread en attendant une opération lente.

---

## 3. L'objet `process`

Quand Node.js démarre, il expose un objet global appelé `process`. Tu n'as pas besoin de l'importer — il est toujours disponible.

```js
// Pas besoin de require, process est global
console.log(process.version); // version de Node installée
```

### Les propriétés importantes

| Propriété | Description |
|---|---|
| `process.argv` | Tableau des arguments en ligne de commande |
| `process.stdin` | Flux d'entrée (ce que l'utilisateur tape) |
| `process.stdout` | Flux de sortie (ce qui s'affiche dans le terminal) |
| `process.stderr` | Flux d'erreur |
| `process.env` | Variables d'environnement |

### process.argv

Quand tu lances `node app.js database.csv` :

```js
console.log(process.argv);
// [ '/usr/bin/node', '/chemin/vers/app.js', 'database.csv' ]
//        index 0            index 1              index 2
```

Index 0 = le chemin vers node. Index 1 = le chemin vers ton script. Tes arguments commencent à l'**index 2**.

### process.stdout vs console.log

```js
console.log("Hello");           // affiche "Hello\n" — ajoute automatiquement un saut de ligne
process.stdout.write("Hello");  // affiche "Hello"   — aucun saut de ligne ajouté
```

Utilise `process.stdout.write` quand tu veux un contrôle exact sur ce qui est écrit, byte par byte. Le correcteur automatique de Holberton vérifie souvent la sortie caractère par caractère.

---

## 4. Les flux (Streams)

`process.stdin` et `process.stdout` sont des **streams** (flux). Un stream est un objet qui envoie ou reçoit des données par morceaux au fil du temps, plutôt qu'en une seule fois.

> Analogie : un stream c'est un tuyau d'eau. L'eau arrive progressivement, tu ne reçois pas toute l'eau d'un coup.

Un stream lisible (comme `stdin`) émet des événements :
- `'data'` — déclenché chaque fois qu'un morceau de données arrive
- `'end'` — déclenché quand le flux se ferme

Tu écoutes ces événements avec `.on(nomEvenement, callback)` :

```js
process.stdin.on('data', (data) => {
  // data contient ce qui a été tapé
  console.log(data.toString());
});

process.stdin.on('end', () => {
  console.log('Le flux est fermé');
});
```

### process.stdin.resume()

Par défaut, `process.stdin` est en mode **pause** — Node.js peut décider de fermer le programme s'il n'a rien d'autre à faire. `.resume()` force Node.js à rester en vie et à attendre des données.

```js
process.stdin.resume(); // "reste ouvert, il va arriver quelque chose"
```

Sans `.resume()`, le programme pourrait se fermer avant que l'utilisateur ait le temps de taper, surtout quand il est lancé via un child process.

---

## 5. Le système de modules (CommonJS)

Node.js utilise le système de modules **CommonJS** par défaut. Chaque fichier `.js` est son propre module avec sa propre portée — les variables définies dans un fichier ne sont pas visibles dans un autre, sauf si elles sont explicitement exportées.

### Exporter une fonction

```js
// dans math.js
function addition(a, b) {
  return a + b;
}
module.exports = addition; // rend la fonction disponible de l'extérieur
```

### Importer une fonction

```js
// dans main.js
const addition = require('./math'); // charge math.js et récupère ce qu'il exporte
console.log(addition(2, 3)); // 5
```

### Pourquoi mettre dans une variable ?

```js
require('fs');          // importé mais inutilisable — aucune référence
const fs = require('fs'); // stocké dans fs — tu peux utiliser fs.readFileSync(...)
```

### Importer un module natif vs un fichier local

```js
const fs = require('fs');        // module natif Node.js (pas de ./)
const fn = require('./0-console'); // fichier local (avec ./)
```

### Piège courant

```js
// FAUX — module.exports à l'intérieur de la fonction
function maFonction() {
  module.exports = maFonction; // ne s'exécute que si on appelle la fonction
}

// CORRECT — module.exports en dehors
function maFonction() { ... }
module.exports = maFonction; // s'exécute au chargement du fichier
```

---

## 6. Le module `fs` — Lire des fichiers

Le module `fs` (File System) est intégré à Node.js. Il fournit tous les outils pour interagir avec les fichiers.

```js
const fs = require('fs');
```

### Lecture synchrone — readFileSync

```js
const content = fs.readFileSync('fichier.txt', 'utf8');
// content est une string avec tout le contenu du fichier
```

- `'utf8'` convertit les données binaires en texte lisible. Sans ce paramètre, tu obtiens un Buffer (données brutes).
- **Synchrone** = le programme s'arrête et attend que la lecture soit terminée avant de continuer.

> Analogie : tu lis un livre. Tu ne fais rien d'autre tant que tu n'as pas fini.

### Gestion des erreurs avec try/catch

Si le fichier n'existe pas, `readFileSync` lance une erreur. Sans `try/catch`, le programme plante.

```js
try {
  const content = fs.readFileSync('nope.csv', 'utf8');
} catch (e) {
  // e contient l'erreur originale (ENOENT: no such file...)
  throw new Error('Cannot load the database'); // on relance une erreur personnalisée
}
```

**Pourquoi relancer une nouvelle erreur ?** Parce que le message d'erreur original de Node (`ENOENT: no such file or directory`) ne correspond pas au message attendu par le correcteur. On attrape l'erreur originale et on en lance une nouvelle avec le bon message.

---

## 7. Traitement d'un fichier CSV

Un fichier CSV est du texte brut où chaque ligne est un enregistrement et les valeurs sont séparées par des virgules.

```
firstname,lastname,age,field   ← ligne d'en-tête (à ignorer)
Johann,Kerbrou,30,CS           ← étudiant 1
Guillaume,Salou,30,SWE         ← étudiant 2
```

### Étape par étape

```js
// 1. Couper en lignes
const lignes = content.split('\n');
// ['firstname,lastname,age,field', 'Johann,Kerbrou,30,CS', '', ...]

// 2. Enlever les lignes vides (fin de fichier avec \n)
const sansVides = lignes.filter((ligne) => ligne.length > 0);

// 3. Enlever la première ligne (l'en-tête)
const etudiants = sansVides.slice(1);

// 4. Pour chaque étudiant, couper par virgule
const parties = 'Johann,Kerbrou,30,CS'.split(',');
// ['Johann', 'Kerbrou', '30', 'CS']
// index 0      index 1   index 2  index 3
```

### Grouper dans un objet

```js
const groupes = {};

groupes['CS'] = [];          // crée le tableau pour CS
groupes['CS'].push('Johann'); // ajoute Johann
groupes['CS'].push('Arielle'); // ajoute Arielle

// Résultat : { CS: ['Johann', 'Arielle', ...], SWE: ['Guillaume', ...] }
```

### Parcourir un objet

```js
Object.keys(groupes) // → ['CS', 'SWE']

Object.keys(groupes).forEach((field) => {
  console.log(field); // 'CS', puis 'SWE'
});
```

### Transformer un tableau en string

```js
['Johann', 'Arielle'].join(', ') // → "Johann, Arielle"
```

---

## 8. Lecture asynchrone — `fs.readFile` et Promises

La lecture **asynchrone** ne bloque pas le programme. Node.js lance la lecture et continue d'exécuter le reste du code. Quand la lecture est terminée, le callback est appelé.

```js
const fs = require('fs');

fs.readFile('fichier.txt', 'utf8', (err, data) => {
  if (err) {
    console.log('Erreur !');
    return;
  }
  console.log(data);
});

console.log('Ce message s'affiche AVANT le contenu du fichier');
```

### Envelopper dans une Promise

`fs.readFile` utilise un callback. Pour retourner une Promise, on l'enveloppe :

```js
function readFileAsync(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return; // IMPORTANT — stop ici, ne pas continuer
      }
      resolve(data);
    });
  });
}
```

**Pourquoi le `return` après `reject` ?** Sans lui, le code continuerait à s'exécuter après le `reject` et tenterait de traiter des données inexistantes, causant un crash.

### Synchrone vs Asynchrone — la différence clé

```
Synchrone (readFileSync)          Asynchrone (readFile + Promise)
────────────────────────          ──────────────────────────────
node 2-main_1.js                  node 3-main_1.js

Number of students: 10            After!        ← s'affiche en premier !
Number of students in CS: 6...    Number of students: 10
                                  Number of students in CS: 6...
                                  Done!
```

Avec l'asynchrone, `console.log("After!")` s'affiche **avant** les résultats car Node.js ne bloque pas sur la lecture.

---

## 9. Serveur HTTP avec le module `http`

Le module `http` est intégré à Node.js. Il permet de créer un serveur sans aucune dépendance externe.

```js
const http = require('http');

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello World');
});

app.listen(1245);
module.exports = app;
```

### L'objet `req` — la requête

| Propriété | Description |
| --- | --- |
| `req.url` | Le chemin de l'URL, ex: `/students` |
| `req.method` | Méthode HTTP : `GET`, `POST`, etc. |
| `req.headers` | En-têtes de la requête |

### L'objet `res` — la réponse

| Méthode | Description |
| --- | --- |
| `res.writeHead(code, headers)` | Définit le code HTTP et les en-têtes |
| `res.write(data)` | Envoie un morceau de réponse |
| `res.end(data)` | Envoie la réponse finale et ferme la connexion |

**`res.end()` est obligatoire.** Si tu ne l'appelles pas, le client attend indéfiniment.

### Routage manuel avec `req.url`

```js
const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/students') {
    res.end('Liste des étudiants');
  } else {
    res.end('Hello Holberton School!');
  }
});
```

### Pourquoi exporter `app` ?

```js
module.exports = app;
```

Les tests Mocha importent le serveur pour lancer des requêtes dessus sans avoir à `node` le fichier manuellement. Sans export, les tests ne peuvent pas accéder au serveur.

---

## 10. Express

Express est un framework web minimaliste construit par-dessus le module `http`. Il ajoute le routage, les middlewares et des méthodes pratiques.

```bash
# Déjà dans package.json, installé via :
npm install
```

### Différence avec `http` brut

```js
// http brut — verbeux
const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello');
});

// Express — concis
const express = require('express');
const app = express();
app.get('/', (req, res) => {
  res.send('Hello'); // gère writeHead + end automatiquement
});
```

### Définir des routes

```js
app.get('/', (req, res) => { ... });              // route /
app.get('/students', (req, res) => { ... });      // route /students
app.get('/students/:major', (req, res) => { ... }); // paramètre dynamique
```

### Paramètres de route

```js
app.get('/students/:major', (req, res) => {
  const { major } = req.params; // ex: 'CS' ou 'SWE'
  res.send(`Students in ${major}`);
});
```

`:major` capture la valeur dans l'URL. `req.params.major` y donne accès.

### `res.send()` vs `res.end()`

| | `res.end()` (http brut) | `res.send()` (Express) |
| --- | --- | --- |
| Content-Type | Manuel avec `writeHead` | Automatique |
| Status code | Manuel avec `writeHead` | 200 par défaut |
| Usage | Bas niveau | Haut niveau |

### `res.status(code).send(message)`

```js
res.status(500).send('Cannot load the database');
// équivalent à :
res.writeHead(500); res.end('Cannot load the database');
```

---

## 11. Architecture MVC avec Express

Quand le serveur grossit, tout mettre dans un fichier devient ingérable. L'architecture **MVC** (Model-View-Controller) sépare les responsabilités.

```
full_server/
├── server.js              ← point d'entrée, assemble tout
├── routes/
│   └── index.js           ← mappe les URLs aux controllers
├── controllers/
│   ├── AppController.js   ← logique de la route /
│   └── StudentsController.js ← logique des routes /students
└── utils.js               ← accès aux données (lit le CSV)
```

### Le rôle de chaque couche

**`utils.js`** — la couche données. Lit le fichier CSV et retourne les données. Ne sait rien des routes ni de HTTP.

**Controllers** — la couche logique. Reçoit `req`/`res`, appelle `utils`, envoie la réponse. Ne sait pas d'où vient la requête.

**Routes** — la couche mapping. Associe chaque URL à un controller. Ne contient aucune logique.

**`server.js`** — assemble tout. Crée l'app Express, monte les routes, écoute le port.

### ES6 modules dans `full_server`

Ce dossier utilise la syntaxe ES6 (`import`/`export`) au lieu de CommonJS (`require`/`module.exports`).

```js
// CommonJS (fichiers 0 à 7)
const fs = require('fs');
module.exports = myFunction;

// ES6 modules (full_server)
import fs from 'fs';
export default myFunction;
export { funcA, funcB };
```

Babel transpile cette syntaxe via `npm run dev`.

### Classes avec méthodes statiques

Les controllers utilisent des classes avec des méthodes `static` :

```js
export default class AppController {
  static getHomepage(req, res) {
    res.status(200).send('Hello Holberton School!');
  }
}
```

**`static`** = la méthode appartient à la classe, pas aux instances. On l'appelle directement : `AppController.getHomepage`. Pas besoin de `new AppController()`.

### Express Router

```js
import { Router } from 'express';
const router = Router();

router.get('/', AppController.getHomepage);
router.get('/students', StudentsController.getAllStudents);

export default router;
```

`router.get('/', AppController.getHomepage)` passe la **référence** à la fonction (pas son résultat). Express la stocke et l'appelle quand une requête arrive.

### `process.argv[2]` — le chemin de la base de données

```bash
node 5-http.js database.csv
```

```js
const database = process.argv[2]; // 'database.csv'
```

Le fichier CSV est passé comme argument en ligne de commande. `process.argv[2]` le récupère à l'exécution — indispensable pour que les tests puissent passer un chemin différent.

---

## 12. ESLint et la config airbnb

ESLint est un outil qui analyse ton code et signale les erreurs de style. Ce projet utilise la configuration **airbnb**, une des plus strictes.

### Règles importantes à retenir

| Règle | Mauvais | Bon |
|---|---|---|
| `semi` | `console.log("x")` | `console.log("x");` |
| `indent` | 4 espaces | 2 espaces |
| `space-before-blocks` | `function f(){` | `function f() {` |
| `prefer-template` | `'Bonjour ' + nom` | `` `Bonjour ${nom}` `` |
| `no-multiple-empty-lines` | 2 lignes vides à la fin | 0 lignes vides à la fin |

### Vérifier son code

```bash
./node_modules/.bin/eslint mon-fichier.js
```

### Corriger automatiquement

```bash
./node_modules/.bin/eslint --fix mon-fichier.js
```

---

## 9. Babel

Babel est un **transpileur** — il convertit du JavaScript moderne (ES6+) en JavaScript compatible avec des environnements plus anciens.

Dans ce projet, `babel-node` exécute ton code en le transpilant à la volée :

```bash
./node_modules/.bin/babel-node mon-fichier.js
```

La configuration dans `babel.config.js` dit à Babel de cibler la version de Node actuellement installée, donc il ne transpile que ce qui est réellement nécessaire.

---

---

# PARTIE 2 — WALKTHROUGH DES TÂCHES

---

## Tâche 0 — Exécuter du JavaScript avec Node.js

**Objectif :** Créer et exporter une fonction qui affiche un message dans le terminal.

### Code complet

```js
function displayMessage(message) {
  console.log(message);
}
module.exports = displayMessage;
```

### Explication ligne par ligne

**`function displayMessage(message) {`**
Déclare une fonction nommée `displayMessage` qui accepte un paramètre `message`. Le nom du paramètre est arbitraire — ce qui compte c'est qu'il soit utilisé de manière cohérente à l'intérieur.

**`console.log(message);`**
Affiche la valeur de `message` dans le terminal, suivi d'un saut de ligne automatique. Si `message` vaut `"Hello NodeJS!"`, ça affiche `Hello NodeJS!`.

**`module.exports = displayMessage;`**
Rend la fonction disponible pour tout fichier qui fait `require('./0-console')`. Sans cette ligne, `require` retournerait un objet vide `{}` et `displayMessage` serait `undefined`.

### Questions fréquentes

**Pourquoi `module.exports` et pas juste exporter ?**
En CommonJS, chaque fichier a son propre module. `module.exports` est l'interface publique de ce module — la seule chose que les autres fichiers peuvent voir.

**Pourquoi ne pas mettre `module.exports` à l'intérieur de la fonction ?**
Parce que `module.exports` à l'intérieur de la fonction ne s'exécuterait que si la fonction est appelée — mais `require` a besoin de l'export au moment du chargement du fichier, avant tout appel.

---

## Tâche 1 — Utiliser Process stdin

**Objectif :** Créer un programme interactif qui lit le nom de l'utilisateur et affiche un message de fermeture quand stdin se termine.

### Code complet

```js
process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.resume();
process.stdin.on('data', (data) => {
  process.stdout.write(`Your name is: ${data.toString()}`);
});
process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
```

### Explication ligne par ligne

**`process.stdout.write('Welcome to Holberton School, what is your name?\n');`**
Affiche le message de bienvenue au démarrage. On utilise `process.stdout.write` plutôt que `console.log` pour avoir un contrôle exact sur les caractères écrits. Le `\n` est le saut de ligne — on le met manuellement.

**`process.stdin.resume();`**
Passe stdin en mode actif. Sans cette ligne, Node.js peut fermer le programme immédiatement s'il détecte qu'il n'a rien d'autre à faire. C'est particulièrement important quand le programme est lancé via un child process.

**`process.stdin.on('data', (data) => { ... });`**
Enregistre un écouteur sur l'événement `data`. Cet événement se déclenche chaque fois que l'utilisateur tape quelque chose et appuie sur Entrée (ou quand un pipe envoie des données). `data` est un Buffer — un objet contenant les octets bruts.

**`` process.stdout.write(`Your name is: ${data.toString()}`); ``**
`.toString()` convertit le Buffer en texte lisible. On utilise un template literal (backticks + `${}`) plutôt que la concaténation `+` — c'est la règle `prefer-template` d'ESLint airbnb.

**`process.stdin.on('end', () => { ... });`**
L'événement `end` se déclenche quand stdin se ferme. Cela arrive quand un pipe se termine (`echo "John" | node 1-stdin.js`) ou quand l'utilisateur fait Ctrl+D.

### Questions fréquentes

**Pourquoi le message de fermeture n'apparaît pas en mode interactif ?**
En mode interactif, le terminal garde stdin ouvert — l'utilisateur peut continuer à taper. L'événement `end` ne se déclenche jamais. Avec un pipe, stdin se ferme automatiquement après l'envoi des données.

**Pourquoi `data.toString()` et pas juste `data` ?**
`data` est un Buffer (données binaires brutes). Afficher un Buffer directement donnerait quelque chose comme `<Buffer 42 6f 62 0a>`. `.toString()` le convertit en texte lisible `"Bob\n"`.

**Pourquoi ne pas utiliser `.trim()` ici ?**
L'énoncé ne demande pas de supprimer le saut de ligne. Le correcteur attend exactement `Your name is: Bob\n`, donc `data.toString()` est correct tel quel.

---

## Tâche 2 — Lire un fichier synchroniquement

**Objectif :** Lire le fichier CSV, compter les étudiants par filière et afficher les résultats.

### Code complet

```js
const fs = require('fs');

function countStudents(path) {
  try {
    const content = fs.readFileSync(path, 'utf8');
    const lines = content
      .split('\n')
      .filter((line) => line.length > 0)
      .slice(1);
    console.log(`Number of students: ${lines.length}`);
    const groups = {};
    lines.forEach((line) => {
      const fields = line.split(',');
      const firstname = fields[0];
      const field = fields[3];
      if (!groups[field]) groups[field] = [];
      groups[field].push(firstname);
    });
    Object.keys(groups).forEach((field) => {
      console.log(
        `Number of students in ${field}: ${groups[field].length}. List: ${groups[field].join(', ')}`,
      );
    });
  } catch (e) {
    throw new Error('Cannot load the database');
  }
}
module.exports = countStudents;
```

### Explication ligne par ligne

**`const fs = require('fs');`**
Importe le module File System de Node.js et le stocke dans `fs`. Sans cette variable, on ne peut pas utiliser `fs.readFileSync`.

**`function countStudents(path) {`**
Déclare la fonction avec `path` comme paramètre — le chemin vers le fichier CSV passé par l'appelant.

**`try { ... } catch (e) { ... }`**
Entoure le code risqué. Si `readFileSync` plante (fichier introuvable), on arrive dans le `catch`. On relance une nouvelle erreur avec le message exact attendu par le correcteur.

**`const content = fs.readFileSync(path, 'utf8');`**
Lit tout le contenu du fichier et le retourne sous forme de string. Le programme attend que la lecture soit terminée (synchrone). Sans `'utf8'`, on aurait un Buffer.

**`.split('\n')`**
Coupe la string à chaque saut de ligne. Transforme un long texte en tableau de lignes.

**`.filter((line) => line.length > 0)`**
Enlève les lignes vides. Les fichiers CSV se terminent souvent par un `\n` qui produit une chaîne vide après le split.

**`.slice(1)`**
Supprime le premier élément du tableau — la ligne d'en-tête (`firstname,lastname,age,field`). On ne veut compter que les vrais étudiants.

**`console.log(\`Number of students: ${lines.length}\`);`**
Affiche le total. `lines.length` est le nombre d'éléments dans le tableau = nombre d'étudiants.

**`const groups = {};`**
Crée un objet vide qui va servir de dictionnaire : clé = filière (CS, SWE), valeur = tableau des prénoms.

**`lines.forEach((line) => { ... });`**
Itère sur chaque ligne d'étudiant.

**`const fields = line.split(',');`**
Coupe la ligne à chaque virgule. `'Johann,Kerbrou,30,CS'` devient `['Johann', 'Kerbrou', '30', 'CS']`.

**`const firstname = fields[0];`**
Récupère le prénom (index 0).

**`const field = fields[3];`**
Récupère la filière (index 3).

**`if (!groups[field]) groups[field] = [];`**
Si la clé `field` n'existe pas encore dans `groups`, on crée un tableau vide. `!groups['CS']` est `true` si `groups['CS']` est `undefined`.

**`groups[field].push(firstname);`**
Ajoute le prénom dans le tableau de la filière correspondante.

**`Object.keys(groups).forEach((field) => { ... });`**
`Object.keys(groups)` retourne un tableau des clés de `groups` : `['CS', 'SWE']`. On itère dessus pour afficher chaque filière.

**`groups[field].join(', ')`**
Transforme le tableau de prénoms en string séparée par des virgules : `['Johann', 'Arielle']` → `"Johann, Arielle"`.

### Questions fréquentes

**Pourquoi `fields[3]` et pas `fields[2]` pour la filière ?**
Parce que le CSV a 4 colonnes dans cet ordre : `firstname(0), lastname(1), age(2), field(3)`. L'index commence à 0.

**Pourquoi `try/catch` et pas juste vérifier si le fichier existe ?**
`readFileSync` lance une exception si le fichier est inaccessible pour n'importe quelle raison (introuvable, permissions...). Le `try/catch` gère tous ces cas en une seule fois.

**Pourquoi relancer `new Error(...)` au lieu de juste `throw e` ?**
Parce que le message d'erreur original de Node est `ENOENT: no such file or directory, open 'nope.csv'`. L'énoncé exige exactement `Cannot load the database`.

---

## Tâche 3 — Lire un fichier asynchroniquement

**Objectif :** Même résultat que la tâche 2, mais sans bloquer le programme — la fonction retourne une Promise.

### Code complet

```js
const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = data
        .split('\n')
        .filter((line) => line.length > 0)
        .slice(1);
      console.log(`Number of students: ${lines.length}`);
      const groups = {};
      lines.forEach((line) => {
        const fields = line.split(',');
        const firstname = fields[0];
        const field = fields[3];
        if (!groups[field]) groups[field] = [];
        groups[field].push(firstname);
      });
      Object.keys(groups).forEach((field) => {
        console.log(
          `Number of students in ${field}: ${groups[field].length}. List: ${groups[field].join(', ')}`,
        );
      });
      resolve();
    });
  });
}
module.exports = countStudents;
```

### Explication ligne par ligne

**`return new Promise((resolve, reject) => { ... });`**
La fonction retourne immédiatement une Promise. Le code à l'intérieur s'exécutera plus tard, quand le fichier sera lu.

**`fs.readFile(path, 'utf8', (err, data) => { ... });`**
Lecture **asynchrone** — Node.js lit le fichier en arrière-plan et appelle le callback quand c'est terminé. Entre-temps, le reste du programme continue (c'est pourquoi `After!` s'affiche avant les résultats).

**`if (err) { reject(new Error('Cannot load the database')); return; }`**
Si le fichier n'existe pas, on rejette la Promise avec l'erreur attendue. Le `return` est **critique** : sans lui, le code continuerait à traiter `data` qui est `undefined`, causant un crash.

**`resolve();`**
À la fin du traitement, on résout la Promise sans valeur (`undefined`). Cela déclenche le `.then()` dans le code appelant.

### Questions fréquentes

**Pourquoi `After!` s'affiche avant les résultats ?**
`fs.readFile` est asynchrone. Node.js lance la lecture et **continue immédiatement** à la ligne suivante (`console.log("After!")`). Quand la lecture se termine, le callback est appelé et affiche les résultats.

**Quelle est la différence avec la tâche 2 ?**
Tâche 2 = synchrone, bloque le thread. Tâche 3 = asynchrone, libère le thread. Dans un serveur HTTP qui gère plusieurs requêtes en même temps, le synchrone bloquerait tout le monde. L'asynchrone est indispensable.

---

## Tâche 4 — Serveur HTTP simple

**Objectif :** Créer un serveur qui répond `Hello Holberton School!` à toutes les requêtes.

### Code complet

```js
const http = require('http');

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello Holberton School!');
});

app.listen(1245);
module.exports = app;
```

### Explication ligne par ligne

**`const http = require('http');`**
Importe le module HTTP natif de Node.js.

**`http.createServer((req, res) => { ... })`**
Crée un serveur. Le callback est appelé à chaque requête reçue, peu importe l'URL ou la méthode.

**`res.writeHead(200, { 'Content-Type': 'text/plain' });`**
Envoie les en-têtes HTTP. `200` = succès. `text/plain` = le corps est du texte brut.

**`res.end('Hello Holberton School!');`**
Envoie la réponse et ferme la connexion. Un seul appel suffit pour les réponses courtes.

**`app.listen(1245);`**
Le serveur écoute sur le port 1245. Toute requête vers `localhost:1245` sera traitée.

**`module.exports = app;`**
Exporte le serveur pour que les tests puissent y accéder.

### Questions fréquentes

**Pourquoi ce serveur répond à toutes les URLs ?**
On ne vérifie jamais `req.url`. Peu importe l'URL tapée, le même handler s'exécute et retourne toujours la même réponse.

**Pourquoi `res.end()` et pas juste `res.write()` ?**
`res.write()` envoie des données mais laisse la connexion ouverte. `res.end()` envoie les données finales et **ferme** la connexion. Sans `res.end()`, le navigateur attendrait indéfiniment la suite.

---

## Tâche 5 — Serveur HTTP avec routage

**Objectif :** Servir des réponses différentes selon l'URL — `/` ou `/students`.

### Code complet

```js
const http = require('http');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];

const app = http.createServer((req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });

  if (req.url === '/students') {
    const lines = ['This is the list of our students'];
    const originalLog = console.log;
    console.log = (msg) => lines.push(msg);

    countStudents(database)
      .then(() => {
        console.log = originalLog;
        res.end(lines.join('\n'));
      })
      .catch(() => {
        console.log = originalLog;
        res.end('Cannot load the database');
      });
  } else {
    res.end('Hello Holberton School!');
  }
});

app.listen(1245);
module.exports = app;
```

### Explication ligne par ligne

**`const database = process.argv[2];`**
Récupère le chemin du CSV passé en argument : `node 5-http.js database.csv`.

**`if (req.url === '/students') { ... } else { ... }`**
Routage manuel : on vérifie l'URL et on répond différemment.

**`const lines = ['This is the list of our students'];`**
Un tableau qui va accumuler toutes les lignes de la réponse. Commence avec la ligne d'introduction.

**`const originalLog = console.log; console.log = (msg) => lines.push(msg);`**
**Le pattern d'interception de `console.log`** : `countStudents` écrit directement dans `console.log`. On ne peut pas récupérer ces sorties normalement. L'astuce : remplacer temporairement `console.log` par une fonction qui, au lieu d'afficher dans le terminal, pousse les messages dans le tableau `lines`.

**`countStudents(database).then(() => { ... }).catch(() => { ... });`**
Appelle la fonction asynchrone. Dans `.then()` on restaure `console.log` original et on envoie `lines.join('\n')` comme réponse. Dans `.catch()` on gère l'erreur.

**`res.end(lines.join('\n'));`**
Joint toutes les lignes avec un saut de ligne et envoie la réponse complète.

### Questions fréquentes

**Pourquoi intercepter `console.log` ?**
`countStudents` a été écrite pour afficher dans le terminal. On ne peut pas la modifier (tâche 3 est figée). L'interception est un contournement pragmatique pour capturer sa sortie et l'envoyer comme réponse HTTP.

---

## Tâche 6 — Serveur Express simple

**Objectif :** Recréer la tâche 4 avec Express.

### Code complet

```js
const express = require('express');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.listen(1245);
module.exports = app;
```

### Explication ligne par ligne

**`const express = require('express');`**
Importe Express. Disponible car `npm install` l'a installé depuis `package.json`.

**`const app = express();`**
Crée une application Express. `app` est l'objet central qui gère routes et middlewares.

**`app.get('/', (req, res) => { ... });`**
Enregistre un handler pour les requêtes `GET` sur `/`. Contrairement à `http.createServer`, cette route ne répond **que** sur `/`.

**`res.send('Hello Holberton School!');`**
Express gère automatiquement `writeHead(200)` et `res.end()`. Plus simple que le module `http` brut.

### Questions fréquentes

**Pourquoi les autres URLs retournent une page 404 HTML ?**
Express génère automatiquement une page 404 pour les routes non définies. Avec `http` brut (tâche 4), on ne vérifiait pas l'URL donc tout retournait 200.

---

## Tâche 7 — Serveur Express avec routage

**Objectif :** Recréer la tâche 5 avec Express.

### Code complet

```js
const express = require('express');
const countStudents = require('./3-read_file_async');

const database = process.argv[2];
const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const lines = ['This is the list of our students'];
  const originalLog = console.log;
  console.log = (msg) => lines.push(msg);

  countStudents(database)
    .then(() => {
      console.log = originalLog;
      res.send(lines.join('\n'));
    })
    .catch(() => {
      console.log = originalLog;
      res.send('Cannot load the database');
    });
});

app.listen(1245);
module.exports = app;
```

### Explication

La logique est identique à la tâche 5. Les différences sont syntaxiques :
- `app.get('/students', ...)` au lieu de `if (req.url === '/students')`
- `res.send(...)` au lieu de `res.end(...)`

Express rend le routage **déclaratif** et lisible plutôt qu'une chaîne de `if`.

---

## Tâche 8 — Architecture MVC complète

**Objectif :** Reorganiser le serveur en plusieurs fichiers avec une séparation claire des responsabilités.

---

### 8.1 — `full_server/utils.js`

**Objectif :** Fonction utilitaire qui lit le CSV et retourne les données — sans logger, sans HTTP.

```js
import fs from 'fs';

export function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }
      const lines = data
        .split('\n')
        .filter((line) => line.trim() !== '')
        .slice(1);
      const fields = {};
      lines.forEach((line) => {
        const parts = line.split(',');
        if (!fields[parts[3]]) fields[parts[3]] = [];
        fields[parts[3]].push(parts[0]);
      });
      resolve(fields);
    });
  });
}
```

**Différence clé avec les tâches 2 et 3 :** Au lieu de `console.log`, `readDatabase` **resolve avec les données** — un objet `{ CS: ['Johann', ...], SWE: [...] }`. Les controllers décident ensuite quoi faire avec ces données. C'est ça la séparation des responsabilités.

---

### 8.2 — `full_server/controllers/AppController.js`

**Objectif :** Gérer la route `/`.

```js
export default class AppController {
  static getHomepage(req, res) {
    res.status(200).send('Hello Holberton School!');
  }
}
```

**`static`** — méthode de classe, appelée directement : `AppController.getHomepage`. Pas besoin de `new`.

---

### 8.3 — `full_server/controllers/StudentsController.js`

**Objectif :** Gérer les routes `/students` et `/students/:major`.

```js
import { readDatabase } from '../utils';

export default class StudentsController {
  static getAllStudents(req, res) {
    readDatabase(process.argv[2])
      .then((fields) => {
        const lines = ['This is the list of our students'];
        const sortedFields = Object.keys(fields).sort((a, b) =>
          a.toLowerCase().localeCompare(b.toLowerCase())
        );
        sortedFields.forEach((field) => {
          lines.push(
            `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`
          );
        });
        res.status(200).send(lines.join('\n'));
      })
      .catch(() => res.status(500).send('Cannot load the database'));
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;
    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
      return;
    }
    readDatabase(process.argv[2])
      .then((fields) => {
        res.status(200).send(`List: ${fields[major].join(', ')}`);
      })
      .catch(() => res.status(500).send('Cannot load the database'));
  }
}
```

**`.sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()))`** — tri alphabétique insensible à la casse. `localeCompare` compare des strings selon les règles linguistiques.

**`return;` après `res.status(500).send(...)`** — sans ce `return`, la fonction continuerait à appeler `readDatabase` après avoir déjà envoyé une réponse. Envoyer deux réponses sur la même requête cause une erreur Node.

**`process.argv[2]`** — récupéré à l'appel de la fonction (pas au chargement du module) pour que les tests puissent passer un chemin différent.

---

### 8.4 — `full_server/routes/index.js`

**Objectif :** Mapper les URLs aux controllers.

```js
import { Router } from 'express';
import AppController from '../controllers/AppController';
import StudentsController from '../controllers/StudentsController';

const router = Router();

router.get('/', AppController.getHomepage);
router.get('/students', StudentsController.getAllStudents);
router.get('/students/:major', StudentsController.getAllStudentsByMajor);

export default router;
```

**Ce fichier ne contient aucune logique** — seulement des associations URL → handler. C'est sa seule responsabilité.

**On passe `AppController.getHomepage` (référence)** et non `AppController.getHomepage()` (appel). Express stocke la référence et l'appelle quand une requête arrive.

---

### 8.5 — `full_server/server.js`

**Objectif :** Point d'entrée — assemble tout et lance le serveur.

```js
import express from 'express';
import router from './routes/index';

const app = express();
app.use('/', router);
app.listen(1245);

export default app;
```

**`app.use('/', router)`** — monte le router sur la racine. Toutes les routes définies dans `routes/index.js` deviennent actives.

**`export default app;`** — exporte le serveur pour les tests.

---

---

# PARTIE 3 — TABLEAU RÉCAPITULATIF

| Tâche | Fichier | Concepts clés |
|---|---|---|
| 0 | `0-console.js` | `module.exports`, `console.log`, paramètres de fonction |
| 1 | `1-stdin.js` | `process.stdin/stdout`, streams, événements `data`/`end`, `.resume()` |
| 2 | `2-read_file.js` | `require('fs')`, `readFileSync`, `try/catch`, parsing CSV, objets, `forEach` |
| 3 | `3-read_file_async.js` | `fs.readFile`, Promises, `resolve`/`reject`, callbacks asynchrones |
| 4 | `4-http.js` | `http.createServer`, `req`, `res`, `writeHead`, `res.end`, `listen` |
| 5 | `5-http.js` | Routage dans http brut (`req.url`), Promise dans un handler HTTP |
| 6 | `6-http_express.js` | Express, `app.get`, `res.send`, routes déclaratives |
| 7 | `7-http_express.js` | Express + async, handler avec Promise, `res.status` |
| 8 | `full_server/` | ES6 modules (`import/export`), Babel, architecture MVC, `Router`, classes |

---

## Commandes utiles

```bash
# Exécuter un fichier
node mon-fichier.js

# Vérifier le style avec ESLint
./node_modules/.bin/eslint mon-fichier.js

# Corriger automatiquement le style
./node_modules/.bin/eslint --fix mon-fichier.js

# Exécuter avec Babel (pour ES6 import/export)
./node_modules/.bin/babel-node mon-fichier.js

# Lancer les tests
npm test

# Vérifier le lint sur tous les fichiers numérotés
npm run check-lint
```
