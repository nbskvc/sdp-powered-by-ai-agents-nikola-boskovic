# ADR-002: Pure Functions for Simulation Logic

Status: Accepted

## Context
The simulation needs to compute the next generation from the current one. The logic could be implemented as a stateful class or as pure functions.

## Decision
Implement `next_generation(grid) -> Grid` as a pure function with no side effects and no mutation of the input.

## Rationale
- Pure functions are trivially unit-testable: given input X, always produces output Y
- No shared mutable state eliminates a whole class of bugs
- Aligns with the testability quality goal

## Consequences
- (+) Zero test setup; no mocks or fixtures needed for core logic
- (+) Each generation is an independent value; easy to inspect or snapshot
- (-) A new set is allocated each generation (acceptable for this scale)
