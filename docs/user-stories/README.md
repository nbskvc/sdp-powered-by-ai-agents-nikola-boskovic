# User Stories

## Domains

The following domains were derived from the architecture
(Module 2 – Chapter 5 Building Block View).

| Domain | Architecture Component | Responsibility |
|------|------|------|
| GRID | grid module | Grid representation and neighbour logic |
| SIM | simulation module | Conway rule evaluation |
| RENDER | renderer module | Grid visualization |
| APP | main module | Application entry point and simulation loop |

## Story List

| ID | Story | Priority |
|----|------|---------|
| GRID-STORY-001 | Represent sparse grid of live cells | Supporting |
| GRID-STORY-002 | Compute neighbours of a cell | Supporting |
| SIM-STORY-001 | Compute next generation using Conway rules | Core |
| RENDER-STORY-001 | Render grid to stdout | Core |
| APP-STORY-001 | Run simulation loop | Supporting |

### Pareto Analysis

Total stories: 5
Core stories (20%): 2
