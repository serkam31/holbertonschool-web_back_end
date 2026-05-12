# ES6 Promise

Asynchronous JavaScript using Promises: creation, chaining, error handling, and async/await syntax.

## Requirements

- Node.js 20.x — Ubuntu 20.04 LTS
- ESLint with airbnb-base config
- Tests via Jest (`npm run test`)

## Setup

```bash
npm install
```

## Tasks

| # | File | Description |
| --- | --- | --- |
| 0 | `0-promise.js` | Return a basic resolved Promise |
| 1 | `1-promise.js` | Resolve or reject based on a boolean |
| 2 | `2-then.js` | Attach `.then()` and `.catch()` handlers |
| 3 | `3-all.js` | Run multiple Promises with `Promise.all` |
| 4 | `4-user-promise.js` | `Promise.resolve()` shorthand |
| 5 | `5-photo-reject.js` | `Promise.reject()` with custom error |
| 6 | `6-final-user.js` | Handle mixed results with `Promise.allSettled` |
| 7 | `7-load_balancer.js` | Return fastest Promise with `Promise.race` |
| 8 | `8-try.js` | Throw an error on invalid input |
| 9 | `9-try.js` | `try/catch/finally` guardrail pattern |

## Scripts

```bash
npm run test          # run all tests
npm run check-lint    # lint all numbered files
```

## Author

Holberton School — Web Back End
