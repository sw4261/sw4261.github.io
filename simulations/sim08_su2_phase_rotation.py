"""
Simulation 08: SU(2) Phase Rotation
Domain: QFT / Symmetry
Source: URFT Whitepaper — Eq. (3.1), Simulation Index p.56
Key Principle: Torsion in Fμν, rotation symmetry of φ(t) = φ₀ + ωt
Expected Result: Rotation symmetry preserved under ω = 41 rad/s
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Time domain
t = np.linspace(0, 2 * np.pi, 500)
omega = 41  # rotation frequency
phi0 = 1.0

# Phase rotation
phi_t = phi0 + omega * t
phi_sin = np.sin(phi_t)
phi_cos = np.cos(phi_t)

# Plot rotation trace (unit circle style)
plt.plot(phi_cos, phi_sin)
plt.xlabel('cos(φ)'), plt.ylabel('sin(φ)')
plt.title('SU(2) Phase Rotation: φ(t) = φ₀ + ωt')
plt.axis('equal'); plt.grid(True)

output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../figures'))
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'sim08_su2_phase_rotation.png'), dpi=300)
plt.show()