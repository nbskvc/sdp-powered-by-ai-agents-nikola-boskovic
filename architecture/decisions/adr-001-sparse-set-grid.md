# ADR-001: Sparse Set as Grid Representation

Status: Accepted

## Context
The grid needs to store cell state across potentially unbounded coordinates. Options considered:
- 2D list/array (dense matrix)
- `set` of live cell coordinates (sparse)

## Decision
Represent the grid as `set[tuple[int, int]]` containing only live cell coordinates.

## Rationale
- No fixed grid size required; the grid grows naturally with live cells
- Neighbour counting only requires iterating live cells and their neighbours, not the full grid
- Simple equality and set operations make testing straightforward

## Consequences
- (+) No memory wasted on dead cells
- (+) `next_generation` only processes relevant cells via `candidates()`
- (-) Bounding box must be computed dynamically for rendering
