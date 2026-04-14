# Chapter 8: Cross-cutting Concepts

## 8.1 Error Handling

The system is a local simulation with no I/O beyond stdin/stdout. Error handling is minimal by design.

| Concern | Strategy |
|---------|----------|
| Invalid initial grid | Validate that input is a `set` of `(int, int)` tuples at startup; raise `ValueError` with a clear message |
| Invalid generation count | Validate at startup; raise `ValueError` if not a positive integer or `None` |
| Unexpected exceptions | Let them propagate naturally — no silent swallowing; the terminal will show the traceback |

No custom exception hierarchy is needed.

## 8.2 Logging

No logging framework is used. The system has a single output channel (stdout via `renderer`). Debug output, if ever needed, goes to stderr to keep stdout clean for the rendered grid.

## 8.3 Testability

| Principle | Implementation |
|-----------|----------------|
| Pure core logic | `next_generation()` and `neighbours()` are pure functions — no setup, no mocks needed |
| Isolated renderer | `render()` writes to stdout; tests can redirect stdout via `io.StringIO` if needed |
| No global state | Grid is passed explicitly between functions; no module-level mutable state |

## 8.4 Configuration

All runtime parameters (initial grid, number of generations, optional delay between generations) are passed as arguments to `run()`. No config files or environment variables are used.
