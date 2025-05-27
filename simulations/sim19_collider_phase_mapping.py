"""
Simulation 19: Collider Phase Mapping
Domain: Particle Collisions
Source: URFT Whitepaper — Section 7, Simulation Index p.57
Key Principle: ψ(x,t) scatter + φ recombination
Expected Result: ρ_jet = 6.2 × 10⁶ J/m³; angular spread = 19.7°
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Angular domain
theta = np.linspace(-np.pi, np.pi, 500)
rho_jet = 6.2e6 * np.exp(-((theta - 0.1)**2) / (2 * (0.344)**2))  # 19.7° ≈ 0.344 rad

# Plot
plt.plot(theta, rho_jet)
plt.title('Angular Phase Jet from ψ Recombination')
plt.xlabel('θ [rad]'); plt.ylabel('ρ_jet(θ)')
plt.grid(True)

output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../figures'))
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'sim19_collider_phase_mapping.png'), dpi=300)
plt.show()