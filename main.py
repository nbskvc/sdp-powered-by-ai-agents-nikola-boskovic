from grid import Grid
from renderer import render
from simulation import next_generation


def run(grid: Grid, generations: int | None = 10) -> None:
    try:
        count = 0
        while generations is None or count < generations:
            grid = next_generation(grid)
            render(grid)
            count += 1
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    initial: Grid = {(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
    run(initial, generations=5)
