# Pagination

## Introduction
La **pagination** consiste à diviser une grande liste de données en **pages**. Comme dans un livre : au lieu d'afficher 10 000 résultats d'un coup, on en affiche 20 par page.

**Pourquoi on l'apprend ?** Pour des raisons de performance et d'expérience utilisateur. Charger 10 000 éléments d'un coup est trop lent.

---

## Concepts clés

### Pagination simple
```js
function paginate(data, page, pageSize) {
  const start = (page - 1) * pageSize;
  const end = start + pageSize;
  return data.slice(start, end);
}

const students = [/* 100 étudiants */];
const page1 = paginate(students, 1, 10); // étudiants 1 à 10
const page2 = paginate(students, 2, 10); // étudiants 11 à 20
```

### Hypermedia pagination — avec des métadonnées
Renvoyer non seulement les données, mais aussi des infos sur la pagination :
```json
{
  "page": 1,
  "page_size": 10,
  "total": 100,
  "next_page": 2,
  "prev_page": null,
  "data": []
}
```

### Cursor-based pagination — pour les grandes bases de données
Au lieu d'un numéro de page, on utilise un **curseur** (l'id du dernier élément vu) :
```json
{
  "next_cursor": "abc123",
  "data": []
}
```

---

## Résumé

| Type | Utilité |
|---|---|
| Simple | `page` + `page_size` |
| Hypermedia | Ajoute des métadonnées (next, prev) |
| Cursor-based | Plus performant pour les très grandes données |
