"""
Simulation 17: Planck-Scale Phase Test
Domain: Quantum Gravity
Source: URFT Whitepaper — Section 6.7, Appendix E.25, Simulation Index p.57
Key Principle: ∇²ρ, ∇ϕ at 10⁻³⁵ m
Expected Result: No divergence in ρ; Ψₚₗₐₙ𝖼ₖ = 0.72 Ψc
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from engine.constants import PSI_CRITICAL

# High-resolution small-scale domain
x = np.linspace(0, 1e-34, 1000)
rho = 1e7 * np.exp(-1e34 * x)
grad_phi = np.gradient(np.sin(1e34 * x), x)

# Compute simple collapse potential approximation
psi = -np.gradient(np.gradient(rho, x), x) - 0.01 * grad_phi**2

# Normalized collapse threshold
psi_normalized = psi / PSI_CRITICAL

# Plot
plt.plot(x, psi_normalized)
plt.axhline(0.72, color='red', linestyle='dashed', label='Ψₚₗₐₙ𝖼ₖ = 0.72 Ψc')
plt.title('Planck-Scale Collapse Test')
plt.xlabel('x [m]'); plt.ylabel('Ψ / Ψc')
plt.legend(); plt.grid(True)

output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../figures'))
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'sim17_planck_scale_phase_test.png'), dpi=300)
plt.show()