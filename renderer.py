from grid import Grid


def render(grid: Grid, *, size: int = 8, origin: tuple[int, int] = (0, 0)) -> None:
    top, left = origin
    for r in range(top, top + size):
        print("".join("O" if (r, c) in grid else "." for c in range(left, left + size)))
