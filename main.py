import argparse
import sys

import renderer
import simulation
from grid import Grid


def run(
    grid: Grid, generations: int | None = 10, step: bool = False, *, size: int = 8
) -> None:
    try:
        count = 0
        while generations is None or count < generations:
            if step:
                input()
            grid = simulation.next_generation(grid)
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


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--step", action="store_true", default=False)
    args = parser.parse_args()
    initial: Grid = {(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
    size = _prompt_grid_size(default=8) if sys.stdin.isatty() else 8
    run(initial, generations=5, step=args.step, size=size)
