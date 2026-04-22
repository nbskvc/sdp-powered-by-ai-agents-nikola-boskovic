# Chapter 12: Glossary

| Term | Definition |
|------|------------|
| Cell | The fundamental unit of the grid. A cell is either **alive** or **dead** at any given generation. |
| Grid | The complete state of the simulation at one point in time. Represented as `set[tuple[int, int]]` of live cell coordinates. |
| Generation | One discrete time step of the simulation. Each generation is computed from the previous by applying Conway's rules. |
| Neighbour | One of the 8 cells surrounding a given cell (horizontal, vertical, and diagonal). |
| Candidate | A cell that must be evaluated for the next generation — any live cell or direct neighbour of a live cell. |
| Conway's Rules | The four rules governing cell survival and birth: (1) live cell with 2–3 live neighbours survives; (2) dead cell with exactly 3 live neighbours becomes alive; (3) all other cells die or stay dead. |
| Still Life | A pattern that does not change between generations (e.g. the 2×2 block). |
| Oscillator | A pattern that cycles through a fixed set of states (e.g. the blinker, period 2). |
| Bounding Box | The smallest rectangle enclosing all live cells. Used by the renderer to determine what region to print. |
| Sparse Representation | Storing only live cells rather than the full grid matrix. Enables an unbounded grid with minimal memory. |
| Pure Function | A function whose output depends only on its inputs and which produces no side effects. Used for `next_generation()`. |
