"""
Simulation 42: Topological Defect Tracking
Domain: Turbulence / Topology
Source: URFT Whitepaper — Appendix AG, Eq. (AG.2)
Key Principle: D(x,t) = |sin(3φ)cos(3φ)|·Θ(κ−κc)
Expected Result: Defect density spike precedes field crash
"""

import numpy as np
import matplotlib.pyplot as plt
import os

x = np.linspace(-np.pi, np.pi, 1000)
phi = x
kappa = np.abs(np.sin(2 * x))
kappa_c = 0.5
D = np.abs(np.sin(3 * phi) * np.cos(3 * phi)) * (kappa > kappa_c)

plt.plot(x, D)
plt.title('Topological Defect Density')
plt.xlabel('x'); plt.ylabel('D(x)')
plt.grid(True)

output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../figures'))
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'sim42_topological_defect_tracking.png'), dpi=300)
plt.show()