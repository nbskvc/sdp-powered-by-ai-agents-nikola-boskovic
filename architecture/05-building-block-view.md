# Chapter 5: Building Block View

## 5.1 Level 1 — Containers

See `diagrams/container.puml`.

| Container   | Responsibility |
|-------------|----------------|
| `main`      | Entry point; wires modules, runs the simulation loop |
| `simulation`| Applies Conway's rules; produces the next generation |
| `grid`      | Grid data type (`set[tuple[int,int]]`) and neighbour logic |
| `renderer`  | Formats and prints the grid to stdout |

Dependency rule: `main` → `renderer` → `simulation` → `grid`

---

## 5.2 Level 2 — Components

See `diagrams/component.puml`.

### `grid` module

| Component | Signature | Responsibility |
|-----------|-----------|----------------|
| `Grid` | `type Grid = set[tuple[int, int]]` | Sparse set of live cell coordinates |
| `neighbours()` | `(cell) → set[Cell]` | Returns the 8 neighbours of a given cell |

### `simulation` module

| Component | Signature | Responsibility |
|-----------|-----------|----------------|
| `candidates()` | `(grid) → set[Cell]` | Union of all live cells and their neighbours |
| `next_generation()` | `(grid: Grid) → Grid` | Pure function; applies Conway's rules |

### `renderer` module

| Component | Signature | Responsibility |
|-----------|-----------|----------------|
| `render()` | `(grid: Grid) → None` | Prints bounding-box view of the grid to stdout |

### `main` module

| Component | Responsibility |
|-----------|----------------|
| `run()` | Initialises grid, loops calling `next_generation` and `render` |
