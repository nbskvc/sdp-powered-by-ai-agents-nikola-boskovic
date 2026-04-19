# GRID-BE-001.1-S1: Grid type alias is importable
def test_grid_be_001_1_s1_grid_type_alias_is_importable():
    # GIVEN the grid module is imported
    from grid import Grid

    # WHEN Grid is referenced as a type annotation
    def annotated(g: Grid) -> Grid:
        return g

    # THEN it resolves without error and is usable
    assert Grid is not None  # nosec B101
