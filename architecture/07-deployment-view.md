# Chapter 7: Deployment View

## 7.1 Overview

See `diagrams/deployment.puml`.

The system is a single Python process. There is no server, container, or network component. It runs entirely on a developer's local machine.

## 7.2 Deployment Environment

| Aspect | Detail |
|--------|--------|
| Runtime | Python 3.11+ |
| OS | Any (Linux, macOS, Windows) |
| Dependencies | Standard library only |
| Entry point | `python main.py` |
| Output | stdout (terminal) |

## 7.3 File Layout

```
game_of_life/
├── main.py          # Entry point and simulation loop
├── grid.py          # Grid type and neighbour logic
├── simulation.py    # Conway's rules / next_generation()
└── renderer.py      # Console rendering
```

## 7.4 Deployment Steps

1. Ensure Python 3.11+ is installed
2. Clone or copy the source files
3. Run: `python main.py`

No build step, no package installation, no configuration files required.
