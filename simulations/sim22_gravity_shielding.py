"""
Simulation 22: Gravity Shielding Field Ring
Domain: Propulsion
Source: URFT Whitepaper — Equation (7.1), Simulation Index p.57
Key Principle: Local reduction in ∇ρ
Expected Result: Δa = −2.1 m/s² at trap core; A = 0.87
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from engine.coherence_tools import compute_gradients

# 2D radial field ring
nx, ny = 200, 200
x = np.linspace(-10, 10, nx)
y = np.linspace(-10, 10, ny)
X, Y = np.meshgrid(x, y)
r = np.sqrt(X**2 + Y**2)

# Coherence trap ring (off-center peak)
rho = 1.0 + 5.0 * np.exp(-((r - 5)**2) / 2)

# Gradient and acceleration
grad_rho = compute_gradients(rho)
a_x = -grad_rho[0] / rho
a_y = -grad_rho[1] / rho
a_mag = np.sqrt(a_x**2 + a_y**2)

# Plot
plt.contourf(X, Y, a_mag, 100, cmap='inferno')
plt.title('Gravity Shielding Acceleration Field')
plt.xlabel('x'); plt.ylabel('y')
plt.colorbar(label='|a| [m/s²]')

output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../figures'))
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'sim22_gravity_shielding.png'), dpi=300)
plt.show()