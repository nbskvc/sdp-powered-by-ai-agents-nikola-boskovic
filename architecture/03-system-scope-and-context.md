# Chapter 3: System Scope and Context

## 3.1 System Scope

The Game of Life system accepts an initial grid configuration, evolves it generation by generation according to Conway's rules, and renders each generation to the console. There are no external systems, databases, or network interfaces.

## 3.2 Context Diagram

See `diagrams/context.puml`.

## 3.3 External Interfaces

| Actor | Interaction |
|-------|-------------|
| User  | Provides initial configuration (e.g. pattern, grid size) and observes console output |
| stdout | Receives rendered grid output each generation |
