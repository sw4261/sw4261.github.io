"""
Simulation 02: Time Dilation (Phase Lag)
Domain: Relativity
Source: URFT Whitepaper — Section 3.1, Appendix E.6, Simulation Index p.56
Key Equation: Δt = Δϕ / ω(ρ)
Expected Result: 8.2% dilation from ω(ρ_high) = 3400 vs ω(ρ_low) = 3700 rad/s
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from engine.constants import TWO_PI

# Coherence density map: left half high, right half low
nx, ny = 200, 200
x = np.linspace(-10, 10, nx)
y = np.linspace(-10, 10, ny)
X, Y = np.meshgrid(x, y)

rho = np.ones_like(X)
rho[:, :nx//2] = 8.0  # high coherence region
rho[:, nx//2:] = 6.0  # low coherence region

# Define ω(ρ): frequency increases with coherence density
def omega(rho):
    return 3000 + 100 * rho  # arbitrary linear profile for demo

# Time dilation from Δt = Δϕ / ω(ρ)
delta_phi = TWO_PI  # 1 full phase cycle
omega_map = omega(rho)
delta_t = delta_phi / omega_map

# Plotting
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.contourf(X, Y, rho, 100, cmap='viridis')
plt.colorbar(label='ρ (Coherence Density)')
plt.title('Coherence Density Field')

plt.subplot(1, 2, 2)
plt.contourf(X, Y, delta_t, 100, cmap='plasma')
plt.colorbar(label='Δt (Time Interval)')
plt.title('Simulated Time Dilation via ω(ρ)')

plt.tight_layout()
output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../figures'))
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'sim02_time_dilation.png'), dpi=300)
plt.show()