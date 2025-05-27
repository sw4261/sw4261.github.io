"""
Simulation 06: Quantum Tunneling
Domain: QM / QFT
Source: URFT Whitepaper — Appendix F, Simulation Index p.56
Key Principle: Continuity of φ across barrier
Expected Result: Tunneling probability P = 18.5% through ρ-barrier of width 4 cm
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Spatial grid
x = np.linspace(-10, 10, 400)
dx = x[1] - x[0]

# Define coherence density barrier
rho = np.ones_like(x)
rho[(x > -2) & (x < 2)] = 5.0  # ρ-barrier region (barrier width = 4)

# Initial φ wave (Gaussian pulse)
phi0 = np.exp(-0.5 * (x + 4)**2)
phi = phi0.copy()

# Simulate tunneling using basic iterative damping
for t in range(50):
    grad_phi = np.gradient(phi, dx)
    laplacian_phi = np.gradient(grad_phi, dx)
    phi += -0.05 * (laplacian_phi / rho)  # simplified evolution

# Calculate tunneling probability beyond barrier
P_tunnel = np.sum(phi[x > 3]**2) / np.sum(phi0**2)

# Plot result
plt.plot(x, phi0, label='Initial ϕ')
plt.plot(x, phi, label=f'Final ϕ (P = {P_tunnel*100:.1f}%)')
plt.axvspan(-2, 2, color='gray', alpha=0.3, label='ρ Barrier')
plt.legend(); plt.title('Quantum Tunneling via ρ(x) Barrier')
plt.xlabel('x'); plt.ylabel('ϕ(x)')
plt.grid(True)

output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../figures'))
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'sim06_quantum_tunneling.png'), dpi=300)
plt.show()