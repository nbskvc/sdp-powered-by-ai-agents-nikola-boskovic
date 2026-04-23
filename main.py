import argparse

import renderer
import simulation
from grid import Grid


def run(grid: Grid, generations: int | None = 10, step: bool = False) -> None:
    try:
        count = 0
        while generations is None or count < generations:
            if step:
                input()
            grid = simulation.next_generation(grid)
            renderer.render(grid)
            count += 1
    except (KeyboardInterrupt, EOFError):
        pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--step", action="store_true", default=False)
    args = parser.parse_args()
    initial: Grid = {(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
    run(initial, generations=5, step=args.step)
