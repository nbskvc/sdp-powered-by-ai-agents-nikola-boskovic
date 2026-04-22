# Chapter 1: Introduction and Goals

## 1.1 Purpose

This document describes the architecture of a Conway's Game of Life simulation system. The system evolves a 2D grid of cells across discrete generations according to Conway's rules, rendering each generation to the console.

## 1.2 Requirements Overview

| ID  | Requirement                                                                 |
|-----|-----------------------------------------------------------------------------|
| R1  | The user can start a simulation with an initial grid configuration          |
| R2  | The system computes the next generation according to Conway's rules         |
| R3  | The system renders each generation to the console                           |
| R4  | The simulation runs for a configurable number of generations or indefinitely |
| R5  | The grid state is held entirely in memory                                   |

### Conway's Rules

A cell is either **alive** or **dead**. At each generation:

- A live cell with 2 or 3 live neighbours survives.
- A dead cell with exactly 3 live neighbours becomes alive.
- All other cells die or remain dead.

## 1.3 Quality Goals

| Priority | Quality Goal    | Motivation                                                  |
|----------|-----------------|-------------------------------------------------------------|
| 1        | Correctness     | The simulation must faithfully implement Conway's rules     |
| 2        | Modularity      | Simulation, state, and visualization are independently replaceable |
| 3        | Testability     | Core logic must be testable without a UI or side effects    |
| 4        | Simplicity      | Minimal dependencies; easy to understand and extend         |

## 1.4 Stakeholders

| Role       | Expectation                                                  |
|------------|--------------------------------------------------------------|
| Developer  | Clean, modular codebase that is easy to test and extend      |
| User       | Start a simulation and observe grid evolution in the console |
