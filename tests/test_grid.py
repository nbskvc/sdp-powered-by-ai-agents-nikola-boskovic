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
