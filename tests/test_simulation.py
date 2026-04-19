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
