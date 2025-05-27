"""
Simulation 05: Collapse Threshold Test
Domain: Quantum Collapse
Source: URFT Whitepaper — Section 2.5, Appendix E.5, Simulation Index p.56
Key Equation: Ψ = ∇²ρ − λ|∇ϕ|² + γ · Var(ω)
Expected Result: Collapse triggered at Ψ = 1.03Ψc with Δρ = 0.011
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from engine.constants import PSI_CRITICAL
from engine.coherence_tools import compute_gradients
from engine.field_tensors import compute_R_mu
from engine.collapse_potential import compute_collapse_potential, collapse_mask

# Grid setup
nx, ny = 200, 200
x = np.linspace(-10, 10, nx)
y = np.linspace(-10, 10, ny)
X, Y = np.meshgrid(x, y)

# Define ρ (coherence density)
rho = np.exp(-0.1 * (X**2 + Y**2))

# Define φ (phase field)
phi = np.arctan2(Y, X)

# Compute ∇φ
grad_phi = compute_gradients(phi)

# Compute Rμ = ρ ∇φ
R_mu = compute_R_mu(rho, grad_phi)

# Collapse potential Ψ
psi = compute_collapse_potential(rho, phi, grad_phi)

# Collapse zone mask
mask = collapse_mask(psi)

# Plot
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.contourf(X, Y, psi, 100, cmap='inferno')
plt.colorbar(label='Ψ (Collapse Potential)')
plt.title('Collapse Potential Field Ψ')
plt.xlabel('x'); plt.ylabel('y')

plt.subplot(1, 2, 2)
plt.contourf(X, Y, mask.astype(float), levels=[0, 0.5, 1], colors=['white', 'red'])
plt.title(f'Collapse Regions (Ψ > {PSI_CRITICAL})')
plt.xlabel('x'); plt.ylabel('y')

plt.tight_layout()
output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../figures'))
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'sim05_collapse_threshold.png'), dpi=300)
plt.show()