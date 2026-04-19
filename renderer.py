from grid import Grid


def render(grid: Grid) -> None:
    if not grid:
        return
    rows = [r for r, _ in grid]
    cols = [c for _, c in grid]
    for r in range(min(rows), max(rows) + 1):
        print(
            "".join(
                "O" if (r, c) in grid else "." for c in range(min(cols), max(cols) + 1)
            )
        )
