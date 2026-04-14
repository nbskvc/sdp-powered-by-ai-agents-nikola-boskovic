# SIM-STORY-001: Compute next generation via Conway's rules

AS A developer
I WANT `next_generation(grid)` to return a new grid with Conway's rules applied
SO THAT the simulation correctly evolves the cell population each tick

Architecture reference: architecture/05-building-block-view.md — `simulation` module; architecture/06-runtime-view.md#62-scenario-next_generation-computation; architecture/decisions/adr-002-pure-functions.md

---

## Scenario SIM-STORY-001-S1: Live cell with 2 live neighbours survives

GIVEN
* a grid containing a live cell at (1,1) with exactly 2 live neighbours

WHEN
* `next_generation(grid)` is called

THEN
* (1,1) is present in the returned grid

---

## Scenario SIM-STORY-001-S2: Live cell with 3 live neighbours survives

GIVEN
* a grid containing a live cell at (1,1) with exactly 3 live neighbours

WHEN
* `next_generation(grid)` is called

THEN
* (1,1) is present in the returned grid

---

## Scenario SIM-STORY-001-S3: Live cell with fewer than 2 live neighbours dies

GIVEN
* a grid containing a live cell at (1,1) with exactly 1 live neighbour

WHEN
* `next_generation(grid)` is called

THEN
* (1,1) is absent from the returned grid

---

## Scenario SIM-STORY-001-S4: Live cell with more than 3 live neighbours dies

GIVEN
* a grid containing a live cell at (1,1) with exactly 4 live neighbours

WHEN
* `next_generation(grid)` is called

THEN
* (1,1) is absent from the returned grid

---

## Scenario SIM-STORY-001-S5: Dead cell with exactly 3 live neighbours becomes alive

GIVEN
* a grid where (2,2) is dead and has exactly 3 live neighbours

WHEN
* `next_generation(grid)` is called

THEN
* (2,2) is present in the returned grid

---

## Scenario SIM-STORY-001-S6: Input grid is not mutated

GIVEN
* a grid `g` with a known set of live cells

WHEN
* `next_generation(g)` is called

THEN
* `g` is unchanged after the call

---

## Scenario SIM-STORY-001-S7: Blinker oscillates correctly (integration)

GIVEN
* a grid with a horizontal blinker: {(1,0), (1,1), (1,2)}

WHEN
* `next_generation(grid)` is called

THEN
* the returned grid equals the vertical blinker: {(0,1), (1,1), (2,1)}

---

# Backend Stories

## SIM-BE-001.1: Implement `candidates()` to collect cells for evaluation

AS A developer
I WANT `candidates(grid)` to return the union of all live cells and their neighbours
SO THAT `next_generation` only evaluates cells that can possibly change state

Architecture reference: architecture/05-building-block-view.md — `simulation` module, `candidates()` component

### Scenario SIM-BE-001.1-S1: Candidates include all live cells

GIVEN
* a grid with live cells at {(0,0), (1,1)}

WHEN
* `candidates(grid)` is called

THEN
* both (0,0) and (1,1) are in the returned set

### Scenario SIM-BE-001.1-S2: Candidates include all neighbours of live cells

GIVEN
* a grid with a single live cell at (0,0)

WHEN
* `candidates(grid)` is called

THEN
* the returned set contains (0,0) and all 8 of its neighbours

### Scenario SIM-BE-001.1-S3: Empty grid yields empty candidates

GIVEN
* an empty grid

WHEN
* `candidates(grid)` is called

THEN
* the returned set is empty

---

## SIM-BE-001.2: Implement `next_generation()` as a pure function

AS A developer
I WANT `next_generation(grid: Grid) -> Grid` to apply Conway's rules to every candidate cell
SO THAT each generation is computed correctly and without side effects

Architecture reference: architecture/05-building-block-view.md — `simulation` module, `next_generation()` component; architecture/decisions/adr-002-pure-functions.md

### Scenario SIM-BE-001.2-S1: Returns a new set, not the input

GIVEN
* any non-empty grid `g`

WHEN
* `result = next_generation(g)` is called

THEN
* `result is not g` evaluates to True

### Scenario SIM-BE-001.2-S2: Still life (block) is stable

GIVEN
* a 2×2 block grid: {(0,0), (0,1), (1,0), (1,1)}

WHEN
* `next_generation(grid)` is called

THEN
* the returned grid equals {(0,0), (0,1), (1,0), (1,1)}

---

# Infrastructure Stories

## SIM-INFRA-001.1: `simulation` module is importable with no dependencies beyond `grid`

AS A developer
I WANT `simulation.py` to import only from the standard library and `grid`
SO THAT the module is self-contained and deployable without package installation

Architecture reference: architecture/07-deployment-view.md — Deployment Environment; architecture/04-solution-strategy.md — dependency direction `renderer → simulation → grid`

### Scenario SIM-INFRA-001.1-S1: Module imports cleanly in a standard Python 3.11+ environment

GIVEN
* a Python 3.11+ interpreter with only the standard library and `grid.py` available

WHEN
* `import simulation` is executed

THEN
* the import succeeds with no errors

### Scenario SIM-INFRA-001.1-S2: `simulation` does not import `renderer` or `main`

GIVEN
* the source of `simulation.py`

WHEN
* its import statements are inspected

THEN
* neither `renderer` nor `main` appear as imports
