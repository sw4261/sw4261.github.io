"""
Simulation 18: Chiral Anomaly Mapping
Domain: QFT Topology
Source: URFT Whitepaper — Equation (3.2), Simulation Index p.57
Key Principle: ∇ · F ≠ 0 under φ shear
Expected Result: Asymmetry induced at Δφ = π/2 offset
"""

import numpy as np
import matplotlib.pyplot as plt

# Phase shear profile
x = np.linspace(0, 2 * np.pi, 500)
phi = np.sin(x)
phi_shifted = np.sin(x + np.pi / 2)
divergence_F = phi - phi_shifted  # ∇·F ~ Δφ structure

# Plot
plt.plot(x, divergence_F)
plt.title('Chiral Phase Shear (Δφ = π/2)')
plt.xlabel('x'); plt.ylabel('∇·F (Shear Indicator)')
plt.grid(True)

plt.savefig('../figures/sim18_chiral_anomaly_mapping.png', dpi=300)
plt.show()
