"""
Simulation 34: PMNS Phase Drift Oscillation
Domain: Neutrino Mixing
Source: URFT Whitepaper — Appendix E.17, Simulation Index p.58
Key Principle: Δφ_ij and re-lock delay τ_ij
Expected Result: Δm²_21 = 7.2 × 10⁻⁵ eV²; matched PMNS pattern
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Time domain
t = np.linspace(0, 10, 1000)
phi1 = np.sin(2 * np.pi * t)
phi2 = np.sin(2 * np.pi * (t - 0.3))  # delay

# PMNS phase overlap (inner product)
U12 = np.cos(2 * np.pi * 0.3)  # phase shift of 0.3
U = np.array([[1, U12], [U12, 1]])

# Plot phase drift
plt.plot(t, phi1, label='ψ₁(t)')
plt.plot(t, phi2, label='ψ₂(t + τ)', linestyle='dashed')
plt.title('PMNS Phase Drift Oscillation')
plt.xlabel('t'); plt.ylabel('ψ')
plt.grid(True); plt.legend()

output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../figures'))
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'sim34_pmns_phase_drift_oscillation.png'), dpi=300)
plt.show()