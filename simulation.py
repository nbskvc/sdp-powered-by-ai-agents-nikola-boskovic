from grid import Grid


def candidates(grid: Grid) -> set:
    return {(r + dr, c + dc) for r, c in grid for dr in (-1, 0, 1) for dc in (-1, 0, 1)}
