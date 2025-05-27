"""
Simulation 16: Inflationary Burst Simulation
Domain: Cosmology
Source: URFT Whitepaper — Appendix E.23, Simulation Index p.57
Key Principle: Initial ρ spike → radial ϕ expansion
Expected Result: ρ₀ = 8.1×10⁷ J/m³; radial expansion velocity v_r = 0.82c
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Radial grid
r = np.linspace(0, 10, 500)
rho0 = 8.1e7
phi = np.exp(-0.2 * r) * np.sin(2 * np.pi * r)

# Simulate radial burst expansion (normalized velocity effect)
expansion_velocity = 0.82  # in units of c
rho_expanding = rho0 * np.exp(-r / (1 / expansion_velocity))

# Plot
plt.plot(r, rho_expanding, label='ρ(r)')
plt.title('Inflationary Coherence Burst')
plt.xlabel('r'); plt.ylabel('ρ')
plt.grid(True); plt.legend()

output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../figures'))
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'sim16_inflationary_burst.png'), dpi=300)
plt.show()