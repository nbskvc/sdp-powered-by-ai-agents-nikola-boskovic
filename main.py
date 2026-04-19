import renderer
import simulation
from grid import Grid


def run(grid: Grid, generations: int | None = 10) -> None:
    try:
        count = 0
        while generations is None or count < generations:
            grid = simulation.next_generation(grid)
            renderer.render(grid)
            count += 1
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    initial: Grid = {(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
    run(initial, generations=5)
