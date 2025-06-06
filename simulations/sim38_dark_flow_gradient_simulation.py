"""
Simulation 38: Dark Flow Gradient Simulation
Domain: Cosmology / Anisotropy
Source: URFT Whitepaper — Simulation Index p.59
Key Principle: ρ(x,θ) = ρ₀ + ε·cos(θ)
Expected Result: Matches WMAP dipole axis; directional superlattice
"""

import numpy as np
import matplotlib.pyplot as plt
import os

theta = np.linspace(0, 2*np.pi, 500)
rho0 = 1.0
epsilon = 0.1
rho_theta = rho0 + epsilon * np.cos(theta)

plt.polar(theta, rho_theta)
plt.title('Dark Flow Gradient (ρ(θ))')

output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../figures'))
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'sim38_dark_flow_gradient_simulation.png'), dpi=300)
plt.show()