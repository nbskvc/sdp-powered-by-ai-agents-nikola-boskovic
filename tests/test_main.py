# RUNNER-INFRA-001.1-S1: Executing python main.py starts the simulation
def test_runner_infra_001_1_s1_main_starts_simulation(tmp_path, monkeypatch):
    # GIVEN a Python 3.12 environment with all source files present
    import subprocess  # nosec B404
    import sys

    # WHEN python main.py is run
    result = subprocess.run(  # nosec B603
        [sys.executable, "main.py"],
        capture_output=True,
        text=True,
        timeout=5,
    )

    # THEN execution returns and grid output appears on stdout
    assert result.returncode == 0  # nosec B101
    assert result.stdout != ""  # nosec B101


# RUNNER-INFRA-001.1-S2: run() is not called on import of main
def test_runner_infra_001_1_s2_run_not_called_on_import(capsys):
    # GIVEN another module that imports main
    import importlib
    import sys

    sys.modules.pop("main", None)

    # WHEN import main is executed
    importlib.import_module("main")

    # THEN run() is not invoked and no output is produced
    captured = capsys.readouterr()
    assert captured.out == ""  # nosec B101


# RUNNER-INFRA-001.2-S1: No files are created during a simulation run
def test_runner_infra_001_2_s1_no_files_created(tmp_path, monkeypatch):
    # GIVEN a clean working directory
    from main import run

    monkeypatch.chdir(tmp_path)

    # WHEN run(grid, generations=5) is called
    run({(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)}, generations=5)

    # THEN no new files exist in the working directory after the call
    assert list(tmp_path.iterdir()) == []  # nosec B101


# RUNNER-INFRA-001.2-S2: Grid variable is a Python set throughout execution
def test_runner_infra_001_2_s2_grid_is_always_a_set():
    # GIVEN the run() function executing
    from main import run

    seen_types = []
    original_next = __import__("simulation").next_generation

    def spy_next(grid):
        seen_types.append(type(grid))
        return original_next(grid)

    import simulation

    simulation.next_generation = spy_next

    # WHEN run executes iterations
    try:
        run({(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)}, generations=3)
    finally:
        simulation.next_generation = original_next

    # THEN the grid is a set at every iteration boundary
    assert all(t is set for t in seen_types)  # nosec B101
