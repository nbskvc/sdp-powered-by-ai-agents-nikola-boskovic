# SIM-STORY-001: Compute Next Generation

AS A developer
I WANT the simulation engine to compute the next generation of the grid
SO THAT Conway's Game of Life evolves correctly over time.

Architecture reference:
[Simulation module](../../architecture/05-building-block-view.md#simulation-module)

---

## Scenario SIM-STORY-001-S1 — Blinker oscillator

GIVEN a grid containing live cells at coordinates (1,2), (2,2), (3,2)
AND all other cells are dead
WHEN next_generation() is called
THEN the next grid contains live cells at (2,1), (2,2), (2,3)

---

# Backend Stories

## SIM-BE-001.1 Next Generation Function

AS A developer
I WANT a pure function `next_generation(grid: Grid) -> Grid`
SO THAT Conway's Game of Life rules are applied to compute the next grid state.

Architecture reference:
[Simulation module](../../architecture/05-building-block-view.md#simulation-module)

### Scenario SIM-BE-001.1-S1 — Apply Conway rules

GIVEN a grid state
WHEN `next_generation(grid)` is executed
THEN cells with fewer than 2 neighbours die
AND cells with 2 or 3 neighbours survive
AND cells with more than 3 neighbours die
AND dead cells with exactly 3 neighbours become alive

---

# Infrastructure Stories

## SIM-INFRA-001.1 Simulation Loop Integration

AS A developer
I WANT the simulation to run through the main application loop
SO THAT the next generation is computed repeatedly.

Architecture reference:
[Main module](../../architecture/05-building-block-view.md#main-module)

### Scenario SIM-INFRA-001.1-S1 — Simulation loop execution

GIVEN the application entry point `run()` in the main module
WHEN the simulation loop executes
THEN `next_generation()` is called repeatedly
AND the grid state updates each iteration
