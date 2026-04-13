# Chapter 6: Runtime View

## 6.1 Scenario: Simulation Loop

See `diagrams/seq-simulation-loop.puml`.

The user starts the simulation by calling `run(initial_grid, generations)`. For each generation:

1. `main` calls `simulation.next_generation(grid)` → receives a new grid
2. `main` calls `renderer.render(new_grid)` → grid is printed to stdout
3. `main` replaces the current grid with the new one and repeats

The loop runs for the configured number of generations (or indefinitely if unbounded).

---

## 6.2 Scenario: next_generation() Computation

See `diagrams/seq-next-generation.puml`.

Inside `next_generation(grid)`:

1. `candidates()` collects all live cells plus their neighbours — the only cells that can change state
2. For each candidate, `neighbours()` is called to count how many are currently alive
3. Conway's rules are applied to determine the next live set
4. A new `Grid` (set) is returned — the input is never mutated
