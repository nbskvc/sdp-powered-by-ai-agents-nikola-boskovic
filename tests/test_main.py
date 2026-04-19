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
