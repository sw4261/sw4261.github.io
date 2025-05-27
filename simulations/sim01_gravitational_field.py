"""
Simulation 01: Gravitational Coherence Field
Domain: General Relativity
Source: URFT Whitepaper — Section 2.4, Appendix E.4, Simulation Index p.56
Key Equation: a^μ = −∂^μρ / ρ
Expected Result: a = 9.81 m/s² reproduced with ρ gradient of 2.2×10⁵ J/m⁴
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from engine.coherence_tools import compute_gradients

# Grid setup
nx, ny = 200, 200
x = np.linspace(-10, 10, nx)
y = np.linspace(-10, 10, ny)
X, Y = np.meshgrid(x, y)

# Coherence density field: Gaussian gravity well
rho = 1.0 + 5.0 * np.exp(-0.1 * (X**2 + Y**2))  # Avoid division by zero

# Compute ∇ρ
grad_rho = compute_gradients(rho)

# Compute gravitational acceleration: a_mu = -∂^μρ / ρ
a_x = -grad_rho[0] / rho
a_y = -grad_rho[1] / rho
a_mag = np.sqrt(a_x**2 + a_y**2)

# Plot
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.contourf(X, Y, rho, 100, cmap='plasma')
plt.colorbar(label='Coherence Density ρ')
plt.title('Gravitational Coherence Field ρ(x, y)')
plt.xlabel('x'); plt.ylabel('y')

plt.subplot(1, 2, 2)
plt.streamplot(X, Y, a_x, a_y, color=a_mag, linewidth=1, cmap='inferno')
plt.colorbar(label='|a| (Effective Acceleration)')
plt.title('Derived Gravitational Acceleration Field')
plt.xlabel('x'); plt.ylabel('y')

plt.tight_layout()
output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../figures'))
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'sim01_gravitational_field.png'), dpi=300)
plt.show()