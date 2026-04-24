# Conway's Game of Life

[![CI](https://github.com/nbskvc/sdp-powered-by-ai-agents-nikola-boskovic/actions/workflows/ci.yml/badge.svg)](https://github.com/nbskvc/sdp-powered-by-ai-agents-nikola-boskovic/actions/workflows/ci.yml)
[![Docs](https://github.com/nbskvc/sdp-powered-by-ai-agents-nikola-boskovic/actions/workflows/docs-deploy.yml/badge.svg)](https://nbskvc.github.io/sdp-powered-by-ai-agents-nikola-boskovic/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/nbskvc/sdp-powered-by-ai-agents-nikola-boskovic/blob/main/LICENSE)

A clean Python implementation of Conway's Game of Life, built as part of the *Software Development Processes Powered by AI Agents* course. The project demonstrates TDD/BDD practices, arc42 architecture documentation, and a fully automated CI/CD pipeline.

## What the Kata Solves

Conway's Game of Life is a zero-player cellular automaton. Given an initial grid of live cells, the simulation evolves through discrete generations using four rules:

1. A live cell with fewer than 2 live neighbours dies (underpopulation).
2. A live cell with 2 or 3 live neighbours survives.
3. A live cell with more than 3 live neighbours dies (overpopulation).
4. A dead cell with exactly 3 live neighbours becomes alive (reproduction).

## Tech Stack & Architecture

| Layer | Choice |
|---|---|
| Language | Python 3.12 |
| Data model | `Grid = set[tuple[int, int]]` — sparse set of live cells |
| Testing | pytest + pre-commit hooks |
| Linting | ruff, black, isort |
| Docs | Sphinx → GitHub Pages |
| CI/CD | GitHub Actions |
| Container | Docker (python:3.12-slim) |

The core is split into three modules:

- `grid.py` — type alias for the grid
- `simulation.py` — pure functions: `candidates`, `next_generation`
- `renderer.py` — terminal rendering
- `main.py` — entry point / runner

## Build & Run Locally

**With Docker:**

```bash
docker build -t kata-ci .
docker run --rm kata-ci
```

To run interactively (you’ll be prompted for grid size):

```bash
docker run --rm -it kata-ci
```

**Without Docker:**

```bash
python -m venv .venv && source .venv/bin/activate
pip install pytest
python main.py
```

## Run (Docker)

**Default run (non-interactive):**

```bash
docker run --rm kata-ci
```

**Step mode (interactive, one generation per Enter):**

```bash
docker run --rm -it kata-ci --step
```

In step mode the program first prompts for a grid size (`NxN`), then advances one generation each time you press Enter.

> **Note:** `--step` without `-i` exits immediately because Docker receives EOF on a non-interactive stdin. To pipe a fixed number of steps instead:
>
> ```bash
> printf "\n\n\n" | docker run --rm -i kata-ci --step
> ```
>
> Each `\n` advances one generation.

## Run Tests

```bash
.venv/bin/pytest -q
```

Or via Docker:

```bash
docker run --rm kata-ci pytest -q
```

## Documentation

Full Sphinx documentation (architecture, user stories, API) is published at:

**[nbskvc.github.io/sdp-powered-by-ai-agents-nikola-boskovic](https://nbskvc.github.io/sdp-powered-by-ai-agents-nikola-boskovic/)**

## Project Structure

```
.
├── grid.py              # Grid type alias
├── simulation.py        # Core Game of Life logic
├── renderer.py          # Terminal renderer
├── main.py              # Entry point
├── tests/               # pytest test suite
├── docs/                # Sphinx documentation source
│   ├── architecture/    # arc42 architecture docs
│   └── user-stories/    # BDD user stories
├── .github/workflows/   # CI and docs deployment pipelines
├── Dockerfile
└── pyproject.toml
```

## Author

**Nikola Bošković** — [@nbskvc](https://github.com/nbskvc)

*SDP Course — Module 6: Final Project*
