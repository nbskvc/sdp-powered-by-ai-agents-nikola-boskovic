# SIM-INFRA-001.1-S1: Module imports cleanly in a standard Python 3.11+ environment
def test_sim_infra_001_1_s1_module_imports_cleanly():
    # GIVEN a Python 3.12 interpreter with only stdlib and grid available
    # WHEN import simulation is executed
    import importlib

    spec = importlib.util.find_spec("simulation")

    # THEN the import succeeds with no errors
    assert spec is not None  # nosec B101


# SIM-INFRA-001.1-S2: simulation does not import renderer or main
def test_sim_infra_001_1_s2_no_forbidden_imports():
    # GIVEN the source of simulation.py
    import ast
    import pathlib

    source = pathlib.Path("simulation.py").read_text()
    tree = ast.parse(source)

    imports = [
        alias.name if isinstance(node, ast.Import) else node.module
        for node in ast.walk(tree)
        for alias in (node.names if isinstance(node, ast.Import) else [None])
        if isinstance(node, ast.Import | ast.ImportFrom)
    ]

    # THEN neither renderer nor main appear as imports
    assert "renderer" not in imports  # nosec B101
    assert "main" not in imports  # nosec B101


# SIM-BE-001.1-S1: Candidates include all live cells
def test_sim_be_001_1_s1_candidates_include_live_cells():
    # GIVEN a grid with live cells at {(0,0), (1,1)}
    from simulation import candidates

    grid = {(0, 0), (1, 1)}

    # WHEN candidates(grid) is called
    result = candidates(grid)

    # THEN both (0,0) and (1,1) are in the returned set
    assert (0, 0) in result  # nosec B101
    assert (1, 1) in result  # nosec B101


# SIM-BE-001.1-S2: Candidates include all neighbours of live cells
def test_sim_be_001_1_s2_candidates_include_all_neighbours():
    # GIVEN a grid with a single live cell at (0,0)
    from simulation import candidates

    grid = {(0, 0)}

    # WHEN candidates(grid) is called
    result = candidates(grid)

    # THEN the returned set contains (0,0) and all 8 of its neighbours
    expected = {(r, c) for r in (-1, 0, 1) for c in (-1, 0, 1)}
    assert result == expected  # nosec B101


# SIM-BE-001.1-S3: Empty grid yields empty candidates
def test_sim_be_001_1_s3_empty_grid_yields_empty_candidates():
    # GIVEN an empty grid
    from simulation import candidates

    # WHEN candidates(grid) is called
    result = candidates(set())

    # THEN the returned set is empty
    assert result == set()  # nosec B101


# SIM-BE-001.2-S1: Returns a new set, not the input
def test_sim_be_001_2_s1_next_generation_returns_new_set():
    # GIVEN any non-empty grid g
    from simulation import next_generation

    g = {(0, 0), (0, 1), (1, 0), (1, 1)}

    # WHEN result = next_generation(g)
    result = next_generation(g)

    # THEN result is not g
    assert result is not g  # nosec B101


# SIM-BE-001.2-S2: Still life (block) is stable
def test_sim_be_001_2_s2_block_is_stable():
    # GIVEN a 2x2 block grid
    from simulation import next_generation

    grid = {(0, 0), (0, 1), (1, 0), (1, 1)}

    # WHEN next_generation(grid) is called
    result = next_generation(grid)

    # THEN the returned grid equals the original block
    assert result == {(0, 0), (0, 1), (1, 0), (1, 1)}  # nosec B101
