"""
Simulation 29: Nested Trap Mode Coupling
Domain: Multi-Particle Systems
Source: URFT Whitepaper — Section 5.4, Simulation Index p.58
Key Principle: Orbital shell overlap ψₙ(x)
Expected Result: Coupling at κ₁ = 2.5, κ₂ = 5.0 rad/m
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Spatial domain
x = np.linspace(0, 2*np.pi, 500)
k1, k2 = 2.5, 5.0
psi1 = np.sin(k1 * x)
psi2 = np.sin(k2 * x)
coupling = psi1 * psi2

# Plot
plt.plot(x, psi1, label='ψ₁ (κ=2.5)')
plt.plot(x, psi2, label='ψ₂ (κ=5.0)')
plt.plot(x, coupling, label='Coupling ψ₁·ψ₂', linestyle='dashed')
plt.title('Nested Trap Mode Coupling')
plt.xlabel('x'); plt.ylabel('ψ')
plt.grid(True); plt.legend()

output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../figures'))
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'sim29_nested_trap_mode_coupling.png'), dpi=300)
plt.show()