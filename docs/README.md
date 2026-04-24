# Conway's Game of Life

A clean Python implementation of Conway's Game of Life, built as part of the *Software Development Processes Powered by AI Agents* course. The project demonstrates TDD/BDD practices, arc42 architecture documentation, and CI/CD pipelines.

## Run (Docker)

```bash
docker build -t kata-ci .
docker run --rm kata-ci
```

Step mode (one generation per Enter press):

```bash
docker run --rm -it kata-ci --step
```

Run tests in Docker:

```bash
docker run --rm kata-ci pytest -q
```
