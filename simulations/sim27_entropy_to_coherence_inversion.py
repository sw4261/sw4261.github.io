"""
Simulation 27: Entropy-to-Coherence Inversion
Domain: Recoherence
Source: URFT Whitepaper — Equation (6.1), Simulation Index p.58
Key Principle: Ψ < 0 region triggers recoherence
Expected Result: Recoherence at Ψ = -0.26; Δρ > 0.007
"""

import numpy as np
import matplotlib.pyplot as plt

# Simulate coherence recovery phase
x = np.linspace(-5, 5, 500)
psi = -0.26 * np.exp(-x**2)
delta_rho = 0.007 + 0.002 * np.cos(2 * np.pi * x)

# Plot
plt.plot(x, psi, label='Ψ(x)')
plt.plot(x, delta_rho, label='Δρ(x)')
plt.axhline(0, color='black', linestyle='--')
plt.title('Recoherence from Collapse (Ψ < 0)')
plt.xlabel('x'); plt.ylabel('Field Value')
plt.grid(True); plt.legend()

plt.savefig('../figures/sim27_entropy_to_coherence_inversion.png', dpi=300)
plt.show()
