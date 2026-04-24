from grid import Grid, neighbours


def candidates(grid: Grid) -> Grid:
    return set(grid) | {n for cell in grid for n in neighbours(cell)}


def _live_neighbour_count(cell: tuple[int, int], grid: Grid) -> int:
    return sum(1 for n in neighbours(cell) if n in grid)


def _in_bounds(cell: tuple[int, int], size: int) -> bool:
    r, c = cell
    return 0 <= r < size and 0 <= c < size


def next_generation(grid: Grid, *, size: int | None = None) -> Grid:
    next_grid = {
        cell
        for cell in candidates(grid)
        if _live_neighbour_count(cell, grid) == 3
        or (cell in grid and _live_neighbour_count(cell, grid) == 2)
    }
    if size is None:
        return next_grid
    return {cell for cell in next_grid if _in_bounds(cell, size)}
