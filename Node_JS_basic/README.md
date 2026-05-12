# Node JS Basic

## Introduction
**Node.js** permet d'exécuter du JavaScript **en dehors du navigateur**, directement sur ton ordinateur ou un serveur. Avant Node.js, JavaScript ne fonctionnait que dans les navigateurs.

**Pourquoi on l'apprend ?** Node.js est la base de tout le développement backend en JavaScript (APIs, serveurs web, etc.).

---

## Concepts clés

### Exécuter un fichier JS
```bash
node mon-fichier.js
```

### `console.log` — afficher dans le terminal
```js
console.log("Hello NodeJS!"); // affiche dans le terminal
```

### Les modules — `require` et `module.exports`
```js
// dans math.js
function addition(a, b) {
  return a + b;
}
module.exports = addition;

// dans main.js
const addition = require('./math');
console.log(addition(2, 3)); // 5
```

### Lire un fichier avec `fs`
```js
const fs = require('fs');
const content = fs.readFileSync('fichier.txt', 'utf8');
console.log(content);
```

### Créer un serveur HTTP
```js
const http = require('http');

const server = http.createServer((req, res) => {
  res.write("Hello World!");
  res.end();
});

server.listen(3000);
```

---

## Résumé

| Concept | Utilité |
|---|---|
| `node fichier.js` | Exécuter du JavaScript |
| `require` | Importer un module |
| `module.exports` | Exporter une fonction |
| `fs` | Lire/écrire des fichiers |
| `http` | Créer un serveur web |
