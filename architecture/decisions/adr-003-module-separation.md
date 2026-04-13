# ADR-003: Three-Module Separation (grid / simulation / renderer)

Status: Accepted

## Context
The system has three distinct concerns: data representation, rule application, and output. These could live in a single file or be split into modules.

## Decision
Separate the system into three modules — `grid`, `simulation`, `renderer` — with a strict one-way dependency rule: `renderer → simulation → grid`.

## Rationale
- Each module has a single, clear responsibility
- `grid` and `simulation` have no I/O dependency, making them fully testable in isolation
- The renderer can be swapped (e.g. for a GUI) without touching core logic

## Consequences
- (+) Core logic is independently testable
- (+) Renderer is replaceable without affecting simulation correctness
- (-) Slightly more files than a single-script solution (acceptable trade-off)
