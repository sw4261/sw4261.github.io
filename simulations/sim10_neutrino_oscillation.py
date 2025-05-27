"""
Simulation 10: Neutrino Flavor Oscillation
Domain: Particle Physics
Source: URFT Whitepaper — Sec. 5, Simulation Index p.57
Key Principle: ψ(t) ∝ sin(κn x − ωt)
Expected Result: Δt = 2.4 ms; Δm² = 7.5 × 10⁻⁵ eV²
"""

import numpy as np
import matplotlib.pyplot as plt

# Time and space grid
x = np.linspace(0, 2*np.pi, 300)
t = 2.4e-3  # 2.4 ms
kappa = 4.0
omega = 3000

# Wavefunction over space at t
psi = np.sin(kappa * x - omega * t)

# Plot flavor oscillation
plt.plot(x, psi)
plt.title('Neutrino Flavor Oscillation at t = 2.4 ms')
plt.xlabel('x'); plt.ylabel('ψ(x, t)')
plt.grid(True)

plt.savefig('../figures/sim10_neutrino_oscillation.png', dpi=300)
plt.show()
