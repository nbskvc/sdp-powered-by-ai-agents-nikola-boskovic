# RENDER-STORY-001: Render each generation to the console

AS A user
I WANT each generation's grid printed to the console
SO THAT I can observe the simulation evolving in real time

Architecture reference: architecture/05-building-block-view.md — `renderer` module, `render()` component; architecture/06-runtime-view.md#61-scenario-simulation-loop

---

## Scenario RENDER-STORY-001-S1: Live cells are represented visually in output

GIVEN
* a grid with live cells at known coordinates

WHEN
* `render(grid)` is called

THEN
* stdout contains a non-empty string with a distinct character marking live cells

---

## Scenario RENDER-STORY-001-S2: Dead cells within the viewport are represented

GIVEN
* a grid where some cells within the viewport are dead

WHEN
* `render(grid)` is called

THEN
* stdout contains a distinct character for dead cells at those positions (`.`)

---

## Scenario RENDER-STORY-001-S3: Output is a fixed-size viewport

GIVEN
* a grid with live cells spanning rows 1–3 and columns 1–3

WHEN
* `render(grid)` is called

THEN
* the printed output is a fixed-size viewport (default 8×8)

---

## Scenario RENDER-STORY-001-S4: Empty grid renders as all dead cells

GIVEN
* an empty grid

WHEN
* `render(grid)` is called

THEN
* stdout contains only the dead-cell character (`.`) and no live-cell character (`O`)

---

# Backend Stories

## RENDER-BE-001.1: Implement `render()` to print a fixed viewport to stdout

AS A developer
I WANT `render(grid: Grid, size: int = 8) -> None` to print a fixed `size×size` viewport
SO THAT the console output is stable and easy to compare across generations

Architecture reference: architecture/05-building-block-view.md — `renderer` module; architecture/decisions/adr-001-sparse-set-grid.md — sparse live-cell set

### Scenario RENDER-BE-001.1-S1: Fixed viewport is 8×8 by default

GIVEN
* a grid with any live cells

WHEN
* `render(grid)` is called

THEN
* stdout contains exactly 8 lines of 8 characters

### Scenario RENDER-BE-001.1-S2: Live cells map to correct positions in the viewport

GIVEN
* a grid with live cells at known coordinates

WHEN
* `render(grid)` is called

THEN
* the corresponding characters in stdout are marked as live (`O`)

### Scenario RENDER-BE-001.1-S3: `render` writes only to stdout, not stderr

GIVEN
* any non-empty grid

WHEN
* `render(grid)` is called

THEN
* stderr remains empty

---

# Infrastructure Stories

## RENDER-INFRA-001.1: `renderer` module has no dependency on `main` or `simulation`

AS A developer
I WANT `renderer.py` to import only from the standard library and `grid`
SO THAT the renderer is independently replaceable without touching simulation logic

Architecture reference: architecture/04-solution-strategy.md — dependency direction `renderer → simulation → grid`; architecture/decisions/adr-003-module-separation.md

### Scenario RENDER-INFRA-001.1-S1: Module imports cleanly in isolation

GIVEN
* a Python 3.11+ environment with only `grid.py` and `renderer.py` present

WHEN
* `import renderer` is executed

THEN
* the import succeeds with no errors

### Scenario RENDER-INFRA-001.1-S2: `renderer` does not import `simulation` or `main`

GIVEN
* the source of `renderer.py`

WHEN
* its import statements are inspected

THEN
* neither `simulation` nor `main` appear as imports

## RENDER-INFRA-001.2: stdout is the sole output channel for rendered grid output

AS A developer
I WANT all rendered grid output to go to stdout
SO THAT the terminal displays the simulation and stdout can be redirected or captured cleanly

Architecture reference: architecture/08-crosscutting-concepts.md#82-logging — stdout for grid output, stderr for debug only; architecture/07-deployment-view.md — Output: stdout (terminal)

### Scenario RENDER-INFRA-001.2-S1: Rendered output is capturable by redirecting stdout

GIVEN
* stdout redirected to an `io.StringIO` buffer

WHEN
* `render(grid)` is called with a non-empty grid

THEN
* the buffer contains the rendered grid text

### Scenario RENDER-INFRA-001.2-S2: No output is written to stderr during normal rendering

GIVEN
* stderr redirected to an `io.StringIO` buffer

WHEN
* `render(grid)` is called

THEN
* the stderr buffer remains empty
