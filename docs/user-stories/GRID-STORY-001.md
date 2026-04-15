# GRID-STORY-001: Represent live cells as a sparse set

AS A developer
I WANT the grid to store only live cell coordinates as a set of (row, col) tuples
SO THAT the simulation can operate on unbounded grids without wasting memory on dead cells

Architecture reference: architecture/05-building-block-view.md — `grid` module; architecture/decisions/adr-001-sparse-set-grid.md

---

## Scenario GRID-STORY-001-S1: Empty grid has no live cells

GIVEN
* a newly created grid with no live cells

WHEN
* the grid is inspected

THEN
* the grid is an empty set
* no coordinates are present

---

## Scenario GRID-STORY-001-S2: Grid holds only live cell coordinates

GIVEN
* a grid initialised with live cells at (0,0), (0,1), and (1,0)

WHEN
* the grid is inspected

THEN
* the set contains exactly {(0,0), (0,1), (1,0)}
* dead cells are not stored

---

## Scenario GRID-STORY-001-S3: Grid supports set equality for testing

GIVEN
* two grids with identical live cell coordinates

WHEN
* they are compared with ==

THEN
* the comparison returns True

---

# Backend Stories

## GRID-BE-001.1: Define the Grid type alias

AS A developer
I WANT a `Grid` type alias defined as `set[tuple[int, int]]`
SO THAT all modules share a consistent, typed contract for grid values

Architecture reference: architecture/05-building-block-view.md — `grid` module, `Grid` type

### Scenario GRID-BE-001.1-S1: Grid type alias is importable

GIVEN
* the `grid` module is imported

WHEN
* `Grid` is referenced as a type annotation

THEN
* it resolves to `set[tuple[int, int]]` without error

### Scenario GRID-BE-001.1-S2: A valid grid value satisfies the type

GIVEN
* a set `{(0, 0), (1, 2)}`

WHEN
* it is assigned to a variable annotated as `Grid`

THEN
* no type error is raised and the value is usable as a grid

---

# Infrastructure Stories

## GRID-INFRA-001.1: grid module is importable as a standalone Python file

AS A developer
I WANT `grid.py` to be a self-contained module with no third-party dependencies
SO THAT the system runs with the Python standard library only

Architecture reference: architecture/07-deployment-view.md — Deployment Environment; architecture/04-solution-strategy.md — Simplicity strategy

### Scenario GRID-INFRA-001.1-S1: Module imports cleanly in a standard Python 3.11+ environment

GIVEN
* a Python 3.11+ interpreter with no packages installed beyond the standard library

WHEN
* `import grid` is executed

THEN
* the import succeeds with no errors or warnings

### Scenario GRID-INFRA-001.1-S2: No side effects on import

GIVEN
* the `grid` module

WHEN
* it is imported

THEN
* no output is written to stdout or stderr
* no files are created or modified
