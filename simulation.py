from grid import Grid


def candidates(grid: Grid) -> Grid:
    return {(r + dr, c + dc) for r, c in grid for dr in (-1, 0, 1) for dc in (-1, 0, 1)}


def _live_neighbour_count(cell: tuple, grid: Grid) -> int:
    r, c = cell
    return sum(
        1
        for dr in (-1, 0, 1)
        for dc in (-1, 0, 1)
        if (dr, dc) != (0, 0) and (r + dr, c + dc) in grid
    )


def next_generation(grid: Grid) -> Grid:
    return {
        cell
        for cell in candidates(grid)
        if _live_neighbour_count(cell, grid) == 3
        or (cell in grid and _live_neighbour_count(cell, grid) == 2)
    }
