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


# RUNNER-BE-001.1-S1: next_generation is called before render each iteration
def test_runner_be_001_1_s1_next_generation_called_before_render():
    # GIVEN spies on next_generation and render
    import main
    import renderer
    import simulation

    call_order = []
    orig_next = simulation.next_generation
    orig_render = renderer.render

    simulation.next_generation = lambda g: call_order.append("next") or orig_next(g)
    renderer.render = lambda g, **kwargs: call_order.append("render")

    # WHEN run(grid, generations=1) is called
    try:
        main.run({(1, 0), (1, 1), (1, 2)}, generations=1)
    finally:
        simulation.next_generation = orig_next
        renderer.render = orig_render

    # THEN next_generation is called before render
    assert call_order == ["next", "render"]  # nosec B101


# RUNNER-BE-001.1-S2: run passes the updated grid to render
def test_runner_be_001_1_s2_run_passes_updated_grid_to_render():
    # GIVEN next_generation returns a known grid g1
    import main
    import renderer
    import simulation

    g0 = {(1, 0), (1, 1), (1, 2)}
    orig_next = simulation.next_generation
    rendered_grids = []
    orig_render = renderer.render

    renderer.render = lambda g, **kwargs: rendered_grids.append(g)

    # WHEN run(g0, generations=1) is called
    try:
        main.run(g0, generations=1)
    finally:
        simulation.next_generation = orig_next
        renderer.render = orig_render

    # THEN render is called with the result of next_generation
    assert rendered_grids[0] == orig_next(g0)  # nosec B101


# RUNNER-BE-001.1-S3: run replaces grid with result of next_generation each step
def test_runner_be_001_1_s3_run_chains_generations():
    # GIVEN two successive generations g1 and g2
    import main
    import renderer
    import simulation

    g0 = {(1, 0), (1, 1), (1, 2)}
    orig_next = simulation.next_generation
    orig_render = renderer.render
    received = []

    simulation.next_generation = lambda g: received.append(g) or orig_next(g)
    renderer.render = lambda g, **kwargs: None

    # WHEN run(g0, generations=2) is called
    try:
        main.run(g0, generations=2)
    finally:
        simulation.next_generation = orig_next
        renderer.render = orig_render

    # THEN second call to next_generation receives g1, not g0
    g1 = orig_next(g0)
    assert received[0] == g0  # nosec B101
    assert received[1] == g1  # nosec B101


# RUNNER-STORY-001-S1: Loop runs exactly N generations
def test_runner_story_001_s1_loop_runs_exactly_n_generations():
    # GIVEN an initial grid and generations=3
    import main
    import renderer
    import simulation

    orig_next = simulation.next_generation
    orig_render = renderer.render
    next_calls, render_calls = [], []

    simulation.next_generation = lambda g: next_calls.append(1) or orig_next(g)
    renderer.render = lambda g, **kwargs: render_calls.append(1)

    # WHEN run(grid, generations=3) is called
    try:
        main.run({(1, 0), (1, 1), (1, 2)}, generations=3)
    finally:
        simulation.next_generation = orig_next
        renderer.render = orig_render

    # THEN next_generation and render are each called exactly 3 times
    assert len(next_calls) == 3  # nosec B101
    assert len(render_calls) == 3  # nosec B101


# RUNNER-STORY-001-S2: Grid state advances each iteration
def test_runner_story_001_s2_grid_advances_each_iteration():
    # GIVEN initial grid g0
    import main
    import renderer
    import simulation

    g0 = {(1, 0), (1, 1), (1, 2)}
    orig_next = simulation.next_generation
    orig_render = renderer.render
    rendered = []

    renderer.render = lambda g, **kwargs: rendered.append(g)

    # WHEN run(g0, generations=2) is called
    try:
        main.run(g0, generations=2)
    finally:
        simulation.next_generation = orig_next
        renderer.render = orig_render

    # THEN render receives next_generation(g0) then next_generation(next_generation(g0))
    g1 = orig_next(g0)
    g2 = orig_next(g1)
    assert rendered[0] == g1  # nosec B101
    assert rendered[1] == g2  # nosec B101


# RUNNER-STORY-001-S3: Loop terminates when generation count is reached
def test_runner_story_001_s3_loop_terminates():
    # GIVEN run(grid, generations=5)
    import main
    import renderer

    orig_render = renderer.render
    renderer.render = lambda g, **kwargs: None

    # WHEN the loop completes
    try:
        main.run({(1, 0), (1, 1), (1, 2)}, generations=5)
        terminated = True
    except Exception:
        terminated = False
    finally:
        renderer.render = orig_render

    # THEN execution returns normally
    assert terminated  # nosec B101


# RUNNER-STORY-001-S4: Unbounded run exits cleanly on KeyboardInterrupt
def test_runner_story_001_s4_unbounded_exits_on_keyboard_interrupt():
    # GIVEN run(grid, generations=None)
    import main
    import renderer
    import simulation

    orig_next = simulation.next_generation
    orig_render = renderer.render
    count = 0

    def raising_next(g):
        nonlocal count
        count += 1
        if count >= 3:
            raise KeyboardInterrupt
        return orig_next(g)

    simulation.next_generation = raising_next
    renderer.render = lambda g, **kwargs: None

    # WHEN a KeyboardInterrupt is raised externally
    try:
        main.run({(1, 0), (1, 1), (1, 2)}, generations=None)
        exited_cleanly = True
    except KeyboardInterrupt:
        exited_cleanly = False
    finally:
        simulation.next_generation = orig_next
        renderer.render = orig_render

    # THEN the simulation exits cleanly without an unhandled exception
    assert exited_cleanly  # nosec B101


# RUNNER-BE-002.2-S1: Each Enter press triggers exactly one generation
def test_runner_be_002_2_s1_step_mode_each_enter_triggers_one_generation(monkeypatch):
    # GIVEN run(grid, generations=3, step=True) with stdin yielding 3 Enter presses
    import main
    import renderer
    import simulation

    orig_next = simulation.next_generation
    orig_render = renderer.render
    next_calls, render_calls = [], []

    simulation.next_generation = lambda g: next_calls.append(1) or orig_next(g)
    renderer.render = lambda g, **kwargs: render_calls.append(kwargs.get("size"))

    inputs = iter(["", "", "", EOFError()])

    def fake_input():
        val = next(inputs)
        if isinstance(val, BaseException):
            raise val
        return val

    monkeypatch.setattr("builtins.input", fake_input)

    # WHEN run(grid, generations=3, step=True) is called
    try:
        main.run({(1, 0), (1, 1), (1, 2)}, generations=3, step=True)
    finally:
        simulation.next_generation = orig_next
        renderer.render = orig_render

    # THEN next_generation and render are each called exactly 3 times
    assert len(next_calls) == 3  # nosec B101
    assert len(render_calls) == 3  # nosec B101


# RUNNER-BE-002.2-S5: run passes render size through to renderer
def test_runner_be_002_2_s5_run_passes_size_to_renderer(monkeypatch):
    # GIVEN a spy renderer
    import main
    import renderer

    seen_sizes = []
    orig_render = renderer.render
    renderer.render = lambda g, **kwargs: seen_sizes.append(kwargs.get("size"))

    # WHEN run is called with a custom size
    try:
        main.run({(0, 0)}, generations=2, step=False, size=12)
    finally:
        renderer.render = orig_render

    # THEN renderer receives that size for each iteration
    assert seen_sizes == [12, 12]  # nosec B101
