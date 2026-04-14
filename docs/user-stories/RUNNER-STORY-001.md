# RUNNER-STORY-001: Run the simulation loop for N generations

AS A user
I WANT to start the simulation with an initial grid and a generation count
SO THAT I can observe the grid evolving for the configured number of steps

Architecture reference: architecture/05-building-block-view.md — `main` module, `run()` component; architecture/06-runtime-view.md#61-scenario-simulation-loop

---

## Scenario RUNNER-STORY-001-S1: Loop runs exactly N generations

GIVEN
* an initial grid and `generations=3`

WHEN
* `run(initial_grid, generations=3)` is called

THEN
* `next_generation` is called exactly 3 times
* `render` is called exactly 3 times

---

## Scenario RUNNER-STORY-001-S2: Grid state advances each iteration

GIVEN
* an initial grid `g0`

WHEN
* `run(g0, generations=2)` is called

THEN
* the grid passed to `render` on iteration 1 is `next_generation(g0)`
* the grid passed to `render` on iteration 2 is `next_generation(next_generation(g0))`

---

## Scenario RUNNER-STORY-001-S3: Loop terminates when generation count is reached

GIVEN
* `run(grid, generations=5)` is called

WHEN
* the loop completes

THEN
* execution returns normally after exactly 5 iterations
* no infinite loop occurs

---

## Scenario RUNNER-STORY-001-S4: Unbounded run loops indefinitely until interrupted

GIVEN
* `run(grid, generations=None)` is called

WHEN
* a `KeyboardInterrupt` is raised externally

THEN
* the simulation exits cleanly without an unhandled exception traceback

---

# Backend Stories

## RUNNER-BE-001.1: Implement `run()` to wire simulation and renderer

AS A developer
I WANT `run(initial_grid, generations)` to call `next_generation` then `render` in a loop
SO THAT the simulation and rendering are correctly sequenced each generation

Architecture reference: architecture/05-building-block-view.md — `main` module; architecture/06-runtime-view.md#61-scenario-simulation-loop

### Scenario RUNNER-BE-001.1-S1: `run` calls next_generation before render each iteration

GIVEN
* a spy on `next_generation` and `render`

WHEN
* `run(grid, generations=1)` is called

THEN
* `next_generation` is called before `render` within the same iteration

### Scenario RUNNER-BE-001.1-S2: `run` passes the updated grid to render

GIVEN
* `next_generation` returns a known grid `g1`

WHEN
* `run(g0, generations=1)` is called

THEN
* `render` is called with `g1`

### Scenario RUNNER-BE-001.1-S3: `run` replaces the current grid with the result of next_generation

GIVEN
* two successive generations g1 and g2

WHEN
* `run(g0, generations=2)` is called

THEN
* the second call to `next_generation` receives `g1`, not `g0`

---

# Infrastructure Stories

## RUNNER-INFRA-001.1: `main.py` is the CLI entry point executed via `python main.py`

AS A developer
I WANT `main.py` to invoke `run()` when executed directly
SO THAT the simulation starts from the command line with no additional tooling

Architecture reference: architecture/07-deployment-view.md — Entry point `python main.py`; architecture/05-building-block-view.md — `main` module

### Scenario RUNNER-INFRA-001.1-S1: Executing `python main.py` starts the simulation

GIVEN
* a Python 3.11+ environment with all four source files present

WHEN
* `python main.py` is run in the terminal

THEN
* the simulation loop executes and grid output appears on stdout

### Scenario RUNNER-INFRA-001.1-S2: `run()` is not called on import of `main`

GIVEN
* another module that imports `main`

WHEN
* `import main` is executed

THEN
* `run()` is not invoked and no output is produced

## RUNNER-INFRA-001.2: Simulation runs entirely in memory with no file or network I/O

AS A developer
I WANT the simulation state to be held in-process as a Python set
SO THAT no persistence layer or external service is required to run the simulation

Architecture reference: architecture/01-introduction-and-goals.md — R5 grid state held entirely in memory; architecture/07-deployment-view.md — single Python process

### Scenario RUNNER-INFRA-001.2-S1: No files are created during a simulation run

GIVEN
* a clean working directory

WHEN
* `run(grid, generations=5)` is called

THEN
* no new files exist in the working directory after the call

### Scenario RUNNER-INFRA-001.2-S2: Grid variable is a Python set throughout execution

GIVEN
* the `run()` function executing

WHEN
* the current grid is inspected at any iteration boundary

THEN
* it is an instance of `set`
