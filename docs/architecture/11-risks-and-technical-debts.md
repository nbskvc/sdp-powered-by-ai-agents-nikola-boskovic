# Chapter 11: Risks and Technical Debts

## 11.1 Risks

| ID  | Risk | Likelihood | Impact | Mitigation |
|-----|------|------------|--------|------------|
| R1  | Unbounded grid grows very large with explosive patterns (e.g. Gosper glider gun) | Medium | Performance degrades | Accept for kata scope; add bounding box limit if needed |
| R2  | Console rendering flickers on fast generation cycles | Low | Poor user experience | Add configurable delay between generations; use ANSI clear-screen escape code |

## 11.2 Technical Debts

| ID  | Debt | Impact | Resolution Path |
|-----|------|--------|-----------------|
| D1  | No configurable initial patterns (hardcoded in `main`) | Low — acceptable for kata | Extract pattern definitions to a separate `patterns.py` module |
| D2  | Renderer computes bounding box on every call | Negligible at kata scale | Cache or pass bounding box explicitly if performance matters |
| D3  | No pause/resume/step controls for the simulation | Low — out of scope for kata | Add a simple REPL loop in `main` if interactive control is needed |
