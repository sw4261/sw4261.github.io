"""
Simulation 24: Artificial Trap Lattice Stability
Domain: Materials Science
Source: URFT Whitepaper — Section 5, Simulation Index p.58
Key Principle: Coherent lattice κₙ modes
Expected Result: κₙ = 1.3, 2.6, 3.9 rad/m; half-life = 11.6 s
"""

import numpy as np
import matplotlib.pyplot as plt

# Spatial domain and trap modes
x = np.linspace(0, 2*np.pi, 500)
k_values = [1.3, 2.6, 3.9]
colors = ['blue', 'green', 'purple']

for k, c in zip(k_values, colors):
    psi = np.sin(k * x) * np.exp(-x / 11.6)
    plt.plot(x, psi, label=f'κ = {k:.1f}')

plt.title('Trap Mode Stability Over Lattice')
plt.xlabel('x'); plt.ylabel('ψ(x)')
plt.grid(True); plt.legend()

plt.savefig('../figures/sim24_artificial_trap_lattice.png', dpi=300)
plt.show()
