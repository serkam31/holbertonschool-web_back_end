# Node JS Basic

Server-side JavaScript with Node.js: modules, file I/O, HTTP servers, Express routing, and MVC architecture.

## Requirements

- Node.js 20.x — Ubuntu 20.04 LTS
- ESLint with airbnb-base config
- Tests via Mocha (`npm run test`)

## Setup

```bash
npm install
```

## Provided files

- `database.csv` — student data used by tasks 2–8

## Tasks

| # | File | Description |
| --- | --- | --- |
| 0 | `0-console.js` | Export a function that prints to stdout |
| 1 | `1-stdin.js` | Read user input from stdin using `process` |
| 2 | `2-read_file.js` | Read and parse a CSV synchronously |
| 3 | `3-read_file_async.js` | Read and parse a CSV asynchronously with Promises |
| 4 | `4-http.js` | Basic HTTP server responding to all routes |
| 5 | `5-http.js` | HTTP server with route-based responses |
| 6 | `6-http_express.js` | Basic Express server |
| 7 | `7-http_express.js` | Express server with dynamic route |
| 8 | `full_server/` | MVC architecture with Express, Router, and controllers |

## Scripts

```bash
npm run test          # run all tests
npm run check-lint    # lint all numbered files
npm run dev           # start dev server with nodemon and babel-node
```

## Author

Holberton School — Web Back End
