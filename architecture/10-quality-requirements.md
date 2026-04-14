# Chapter 10: Quality Requirements

## 10.1 Quality Tree

| Quality Goal | Scenario | Measure |
|--------------|----------|---------|
| Correctness | Given a known pattern (e.g. blinker), `next_generation` produces the exact expected output | Unit tests pass for all standard patterns |
| Modularity | Renderer is replaced with a no-op | No changes required in `grid` or `simulation` |
| Testability | Core logic is tested without any I/O or mocks | `grid` and `simulation` tests have zero external dependencies |
| Simplicity | A new developer reads the codebase | Four files, each under 50 lines |

## 10.2 Quality Scenarios

### Correctness — Blinker Pattern
- **Stimulus:** `next_generation` called on a horizontal blinker
- **Expected:** Returns the vertical blinker (and vice versa on the next call)
- **Measure:** Exact set equality

### Correctness — Still Life (Block)
- **Stimulus:** `next_generation` called on a 2×2 block
- **Expected:** Returns the identical 2×2 block
- **Measure:** Exact set equality

### Testability — No I/O in core
- **Stimulus:** Run the full test suite for `grid` and `simulation`
- **Expected:** No file, stdout, or network access occurs
- **Measure:** Tests pass with stdout redirected to `/dev/null`

### Simplicity — No dependencies
- **Stimulus:** Run `pip install` on a fresh environment
- **Expected:** No packages installed; standard library only
- **Measure:** Empty `requirements.txt` or no `requirements.txt`
