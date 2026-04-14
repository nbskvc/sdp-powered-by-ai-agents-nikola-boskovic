# Chapter 2: Architecture Constraints

## 2.1 Technical Constraints

| ID  | Constraint                                      | Rationale                                      |
|-----|-------------------------------------------------|------------------------------------------------|
| T1  | Implementation language is Python               | Kata requirement                               |
| T2  | No external runtime dependencies                | Simplicity; standard library only              |
| T3  | Grid state must be held entirely in memory      | No persistence layer needed for a simulation   |
| T4  | Visualization is console-based (stdout)         | Kata requirement; no GUI framework             |

## 2.2 Organisational Constraints

| ID  | Constraint                                      | Rationale                                      |
|-----|-------------------------------------------------|------------------------------------------------|
| O1  | Codebase must be structured as distinct modules | Enforces separation of concerns                |
| O2  | Core simulation logic must be unit-testable     | Correctness is the top quality goal            |

## 2.3 Conventions

| ID  | Convention                                      |
|-----|-------------------------------------------------|
| C1  | Follow PEP 8 style guidelines                   |
| C2  | Modules: `simulation`, `grid`, `renderer`       |
| C3  | No module may import from a higher-level module (dependency rule: renderer → simulation → grid) |
