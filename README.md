# URFT Simulation Archive

This repository contains all 43 high-fidelity simulation scripts supporting the Unified Resonance Field Theory (URFT).  
Each simulation validates specific equations, phenomena, or predictions outlined in the whitepaper.

## Directory Structure

```
/engine/         # Shared solvers, constants, tensor tools
/simulations/    # 43 simulation scripts (sim01_*.py to sim43_*.py)
/figures/        # Output visualizations from each simulation
/notebook/       # Optional space for aggregated or exploratory work
README.md        # This file
requirements.txt # Python dependencies
```

## How to Run

1. Make sure you have Python 3.8+ installed.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run any simulation script from `/simulations/`, e.g.:

```bash
python simulations/sim01_gravitational_field.py
```

Each script will generate its corresponding figure in `/figures/`.

## Simulation Coverage

| Sim # | Domain                      | Description |
|-------|-----------------------------|-------------|
| 1–5   | Gravity / Collapse          | Core coherence motion, thresholding |
| 6–10  | QM / Particles              | Trap modes, tunneling, oscillation |
| 11–20 | Systems / Computing         | Logic states, time control, mass |
| 21–30 | Consciousness / Q-Theory    | Q-index feedback and transfer |
| 31–35 | Standard Model Completion   | SU(2), Higgs analogs, matrix behavior |
| 36–43 | Origin / Turbulence         | Big bang, cascade collapse, abiogenesis |

See whitepaper Appendix F for full details.
