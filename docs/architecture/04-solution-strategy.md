# Chapter 4: Solution Strategy

## 4.1 Core Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Language | Python | Kata requirement |
| Grid representation | Set of (row, col) tuples for live cells | Sparse; simple to compute neighbours |
| Module structure | `grid`, `simulation`, `renderer` | Separates state, logic, and output |
| Dependency direction | `renderer → simulation → grid` | Core logic has no UI dependency |
| Visualization | Console (stdout) | Kata requirement; no framework needed |

## 4.2 Key Strategies

**Sparse grid representation**
Only live cells are stored as a `set` of `(row, col)` tuples. This keeps the data structure simple and makes neighbour counting straightforward without iterating a full matrix.

**Pure functions for simulation logic**
`next_generation(grid)` takes a grid and returns a new grid with no mutation. This makes the core logic trivially testable and free of side effects.

**Separation of concerns**
- `grid` — data type and neighbour logic
- `simulation` — applies Conway's rules to produce the next generation
- `renderer` — formats and prints the grid to stdout

## 4.3 How Quality Goals Are Met

| Quality Goal | Strategy |
|--------------|----------|
| Correctness  | Pure `next_generation` function, fully unit-testable |
| Modularity   | Three independent modules with a strict dependency rule |
| Testability  | No I/O in `grid` or `simulation`; renderer is isolated |
| Simplicity   | Standard library only; minimal abstractions |
