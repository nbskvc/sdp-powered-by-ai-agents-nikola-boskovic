Cell = tuple[int, int]
Grid = set[Cell]


def neighbours(cell: Cell) -> set[Cell]:
    r, c = cell
    return {
        (r + dr, c + dc) for dr in (-1, 0, 1) for dc in (-1, 0, 1) if (dr, dc) != (0, 0)
    }
