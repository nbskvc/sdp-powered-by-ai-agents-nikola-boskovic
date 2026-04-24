import argparse
import sys

import renderer
import simulation
from grid import Grid


def run(
    grid: Grid, generations: int | None = 10, step: bool = False, *, size: int = 8
) -> None:
    if not isinstance(grid, set):
        raise TypeError("grid must be a set of (row, col) integer tuples")
    for cell in grid:
        if (
            not isinstance(cell, tuple)
            or len(cell) != 2
            or not isinstance(cell[0], int)
            or not isinstance(cell[1], int)
        ):
            raise TypeError("grid cells must be (row, col) integer tuples")
    if generations is not None:
        if not isinstance(generations, int):
            raise TypeError("generations must be an int or None")
        if generations < 0:
            raise ValueError("generations must be >= 0")
    try:
        count = 0
        while generations is None or count < generations:
            if step:
                input()
            grid = simulation.next_generation(grid, size=size)
            renderer.render(grid, size=size)
            count += 1
    except (KeyboardInterrupt, EOFError):
        pass


def _prompt_grid_size(default: int = 8) -> int:
    raw = input(f"Grid size (N for NxN) [{default}]: ").strip()
    if raw == "":
        return default
    try:
        size = int(raw)
    except ValueError:
        return default
    return size if size > 0 else default


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--step", action="store_true", default=False)
    return parser.parse_args(argv)


if __name__ == "__main__":
    args = parse_args()
    initial: Grid = {(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
    size = _prompt_grid_size(default=8) if sys.stdin.isatty() else 8
    run(initial, generations=5, step=args.step, size=size)
