# GRID-BE-001.1-S1: Grid type alias is importable
def test_grid_be_001_1_s1_grid_type_alias_is_importable():
    # GIVEN the grid module is imported
    from grid import Grid

    # WHEN Grid is referenced as a type annotation
    def annotated(g: Grid) -> Grid:
        return g

    # THEN it resolves without error and is usable
    assert Grid is not None  # nosec B101


# GRID-BE-001.1-S2: A valid grid value satisfies the type
def test_grid_be_001_1_s2_valid_grid_value_satisfies_type():
    # GIVEN a set of coordinate tuples
    from grid import Grid

    # WHEN assigned to a Grid-annotated variable
    g: Grid = {(0, 0), (1, 2)}

    # THEN it is usable as a grid
    assert g == {(0, 0), (1, 2)}  # nosec B101


# GRID-INFRA-001.1-S1: Module imports cleanly in a standard Python 3.11+ environment
def test_grid_infra_001_1_s1_module_imports_cleanly():
    # GIVEN a Python 3.12 interpreter
    # WHEN import grid is executed
    import importlib

    spec = importlib.util.find_spec("grid")

    # THEN the import succeeds with no errors
    assert spec is not None  # nosec B101


# GRID-INFRA-001.1-S2: No side effects on import
def test_grid_infra_001_1_s2_no_side_effects_on_import(capsys):
    # GIVEN the grid module
    import importlib
    import sys

    # WHEN it is imported (force reimport)
    sys.modules.pop("grid", None)
    importlib.import_module("grid")

    # THEN no output is written to stdout or stderr
    captured = capsys.readouterr()
    assert captured.out == ""  # nosec B101
    assert captured.err == ""  # nosec B101


# GRID-BE-001.2-S1: neighbours() returns the 8 surrounding coordinates
def test_grid_be_001_2_s1_neighbours_returns_8_surrounding_coordinates():
    # GIVEN a cell coordinate (0,0)
    from grid import neighbours

    # WHEN neighbours((0,0)) is called
    result = neighbours((0, 0))

    # THEN it returns exactly the 8 surrounding coordinates and not the cell itself
    expected = {
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    }
    assert result == expected  # nosec B101
