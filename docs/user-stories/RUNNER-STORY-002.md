# RUNNER-STORY-002: Advance the simulation one generation at a time with `--step`

AS A user
I WANT to pass `--step` on the command line
SO THAT I can advance the simulation exactly one generation per Enter key press and inspect each state at my own pace

Architecture reference: architecture/05-building-block-view.md — `main` module, `run()` component; architecture/06-runtime-view.md#61-scenario-simulation-loop; architecture/08-crosscutting-concepts.md#81-error-handling

---

## Scenario RUNNER-STORY-002-S1: Step mode advances one generation per Enter press

GIVEN
* the program is started with `--step`
* `next_generation` and `render` are observable (spy/mock)

WHEN
* the user presses Enter N times

THEN
* `next_generation` is called exactly N times
* `render` is called exactly N times

---

## Scenario RUNNER-STORY-002-S2: Step mode exits cleanly on EOF

GIVEN
* the program is started with `--step`
* stdin reaches EOF (e.g. piped from `/dev/null` or a finite input stream)

WHEN
* the EOF condition is detected while waiting for the next Enter press

THEN
* the program exits with exit code 0
* no exception traceback is printed to stdout or stderr

---

## Scenario RUNNER-STORY-002-S3: Step mode exits cleanly on KeyboardInterrupt

GIVEN
* the program is started with `--step`
* the simulation is waiting for an Enter press

WHEN
* a `KeyboardInterrupt` is raised (e.g. Ctrl-C)

THEN
* the program exits with exit code 0
* no exception traceback is printed to stdout or stderr

---

## Scenario RUNNER-STORY-002-S4: Without `--step` the program runs non-interactively

GIVEN
* the program is started without `--step`

WHEN
* `run()` is called

THEN
* the simulation completes all configured generations without reading from stdin
* the program exits normally (exit code 0)
* `docker run --rm kata-ci` never blocks waiting for input

---

# Backend Stories

## RUNNER-BE-002.1: Parse `--step` CLI flag and pass it to `run()`

AS A developer
I WANT `main.py` to accept an optional `--step` flag via `argparse`
SO THAT the step-mode behaviour can be toggled from the command line without changing source code

Architecture reference: architecture/05-building-block-view.md — `main` module; architecture/08-crosscutting-concepts.md#84-configuration

### Scenario RUNNER-BE-002.1-S1: `--step` flag is parsed as `True`

GIVEN
* `sys.argv` contains `["main.py", "--step"]`

WHEN
* the argument parser runs

THEN
* the parsed namespace has `step=True`

### Scenario RUNNER-BE-002.1-S2: Absence of `--step` defaults to `False`

GIVEN
* `sys.argv` contains only `["main.py"]`

WHEN
* the argument parser runs

THEN
* the parsed namespace has `step=False`

---

## RUNNER-BE-002.2: Implement step-mode loop in `run()`

AS A developer
I WANT `run()` to accept a `step: bool = False` parameter
SO THAT when `step=True` it reads one line from stdin before each generation and when `step=False` it behaves as before

Architecture reference: architecture/05-building-block-view.md — `main` module, `run()` component; architecture/06-runtime-view.md#61-scenario-simulation-loop

### Scenario RUNNER-BE-002.2-S1: Each Enter press triggers exactly one generation

GIVEN
* `run(grid, generations=3, step=True)` is called
* stdin is replaced with a stream that yields 3 newline characters

WHEN
* the function runs to completion

THEN
* `next_generation` is called exactly 3 times
* `render` is called exactly 3 times

### Scenario RUNNER-BE-002.2-S2: EOF on stdin terminates the loop cleanly

GIVEN
* `run(grid, generations=None, step=True)` is called
* stdin is replaced with an empty stream (immediate EOF)

WHEN
* the function attempts to read the first line

THEN
* the function returns normally
* the process exit code is 0

### Scenario RUNNER-BE-002.2-S3: KeyboardInterrupt terminates the loop cleanly

GIVEN
* `run(grid, generations=None, step=True)` is called
* a `KeyboardInterrupt` is raised on the first `input()` call

WHEN
* the interrupt is raised

THEN
* the function returns normally (exception is caught internally)
* the process exit code is 0

### Scenario RUNNER-BE-002.2-S4: `step=False` does not read from stdin

GIVEN
* `run(grid, generations=3, step=False)` is called
* stdin is replaced with a stream that raises `RuntimeError` if read

WHEN
* the function runs to completion

THEN
* no read is attempted on stdin
* `next_generation` and `render` are each called exactly 3 times

---

# Infrastructure Stories

## RUNNER-INFRA-002.1: `docker run --rm kata-ci` never blocks in CI (no `--step`)

AS A developer
I WANT the default Docker invocation to run non-interactively and exit
SO THAT CI pipelines are never blocked waiting for user input

Architecture reference: architecture/07-deployment-view.md — Deployment Steps; architecture/02-constraints.md — T1, T2

### Scenario RUNNER-INFRA-002.1-S1: Default container run exits without stdin interaction

GIVEN
* the `kata-ci` image has been built successfully
* no `--step` flag is passed to `docker run`

WHEN
* `docker run --rm kata-ci` is executed

THEN
* the container completes and exits with code 0
* no prompt or blocking read on stdin occurs

### Scenario RUNNER-INFRA-002.1-S2: Step mode is accessible via Docker with piped input

GIVEN
* the `kata-ci` image has been built successfully

WHEN
* `echo -e "\n\n\n" | docker run --rm -i kata-ci --step` is executed (3 Enter presses piped in)

THEN
* `next_generation` and `render` are each invoked 3 times
* the container exits with code 0 after stdin is exhausted
