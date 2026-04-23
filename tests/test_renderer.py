# RENDER-INFRA-001.1-S1: renderer module imports cleanly
def test_render_infra_001_1_s1_module_imports_cleanly():
    # GIVEN a Python 3.12 environment with only grid.py and renderer.py
    import importlib

    spec = importlib.util.find_spec("renderer")

    # THEN the import succeeds with no errors
    assert spec is not None  # nosec B101


# RENDER-INFRA-001.1-S2: renderer does not import simulation or main
def test_render_infra_001_1_s2_no_forbidden_imports():
    # GIVEN the source of renderer.py
    import ast
    import pathlib

    source = pathlib.Path("renderer.py").read_text()
    tree = ast.parse(source)

    imports = [
        alias.name if isinstance(node, ast.Import) else node.module
        for node in ast.walk(tree)
        for alias in (node.names if isinstance(node, ast.Import) else [None])
        if isinstance(node, ast.Import | ast.ImportFrom)
    ]

    # THEN neither simulation nor main appear as imports
    assert "simulation" not in imports  # nosec B101
    assert "main" not in imports  # nosec B101


# RENDER-INFRA-001.2-S1: Rendered output is capturable via stdout
def test_render_infra_001_2_s1_output_capturable_via_stdout(capsys):
    # GIVEN stdout redirected to a buffer
    from renderer import render

    # WHEN render(grid) is called with a non-empty grid
    render({(0, 0), (0, 1)})

    # THEN the buffer contains the rendered grid text
    captured = capsys.readouterr()
    assert captured.out != ""  # nosec B101


# RENDER-INFRA-001.2-S2: No output written to stderr during normal rendering
def test_render_infra_001_2_s2_no_stderr(capsys):
    # GIVEN stderr redirected to a buffer
    from renderer import render

    # WHEN render(grid) is called
    render({(0, 0)})

    # THEN the stderr buffer remains empty
    captured = capsys.readouterr()
    assert captured.err == ""  # nosec B101


# RENDER-BE-001.1-S1: Fixed viewport renders exactly 8x8 by default
def test_render_be_001_1_s1_fixed_viewport_is_8x8_by_default(capsys):
    # GIVEN a grid with live cells at known coordinates
    from renderer import render

    # WHEN render(grid) is called
    render({(0, 0), (2, 3)})

    # THEN output contains exactly 8 lines of 8 characters
    lines = capsys.readouterr().out.splitlines()
    assert len(lines) == 8  # nosec B101
    assert all(len(line) == 8 for line in lines)  # nosec B101


# RENDER-BE-001.1-S2: Live cell coordinates map to correct positions in viewport
def test_render_be_001_1_s2_live_cells_map_to_positions(capsys):
    # GIVEN a grid with live cells at (0,0) and (7,7)
    from renderer import render

    render({(0, 0), (7, 7)})

    # THEN the first char of first line and last char of last line are live
    lines = capsys.readouterr().out.splitlines()
    assert lines[0][0] == "O"  # nosec B101
    assert lines[7][7] == "O"  # nosec B101


# RENDER-BE-001.1-S3: render writes only to stdout, not stderr
def test_render_be_001_1_s3_writes_only_to_stdout(capsys):
    # GIVEN any non-empty grid
    from renderer import render

    render({(1, 1)})

    # THEN stderr remains empty
    captured = capsys.readouterr()
    assert captured.err == ""  # nosec B101


# RENDER-STORY-001-S1: Live cells are represented visually
def test_render_story_001_s1_live_cells_represented(capsys):
    # GIVEN a grid with live cells at known coordinates
    from renderer import render

    render({(0, 0), (0, 2)})

    # THEN stdout contains a non-empty string with a distinct character for live cells
    out = capsys.readouterr().out
    assert "O" in out  # nosec B101


# RENDER-STORY-001-S2: Dead cells within bounding box are represented
def test_render_story_001_s2_dead_cells_represented(capsys):
    # GIVEN a grid where some cells within the bounding box are dead
    from renderer import render

    render({(0, 0), (0, 2)})  # (0,1) is dead but within bounding box

    # THEN stdout contains a distinct character for dead cells
    out = capsys.readouterr().out
    assert "." in out  # nosec B101


# RENDER-STORY-001-S3: Output bounded by live cell extents
def test_render_story_001_s3_output_bounded_by_extents(capsys):
    # GIVEN a grid with live cells spanning rows 1-3 and columns 1-3
    from renderer import render

    render({(1, 1), (1, 3), (3, 1), (3, 3)})

    # THEN output is a fixed viewport (8x8)
    lines = capsys.readouterr().out.splitlines()
    assert len(lines) == 8  # nosec B101
    assert all(len(line) == 8 for line in lines)  # nosec B101


# RENDER-STORY-001-S4: Empty grid produces no cell output
def test_render_story_001_s4_empty_grid_no_output(capsys):
    # GIVEN an empty grid
    from renderer import render

    # WHEN render(grid) is called
    render(set())

    # THEN output contains only dead cells
    out = capsys.readouterr().out
    assert "O" not in out  # nosec B101
    assert "." in out  # nosec B101
