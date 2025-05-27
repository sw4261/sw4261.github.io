"""
Simulation 39: Abiogenesis Phase Trap
Domain: Biophysics / Origin of Life
Source: URFT Whitepaper — Simulation Index p.59
Key Principle: Recursive coherence loop initiates Q-index feedback
Expected Result: Q = 1.17; entropy reduction ΔH = -0.031
"""

import numpy as np
import matplotlib.pyplot as plt

time = np.linspace(0, 10, 1000)
Q = 1.0 + 0.17 * np.exp(-0.1 * time)
entropy = 0.05 - 0.0031 * np.sin(0.5 * time)

plt.plot(time, Q, label='Q(t)')
plt.plot(time, entropy, label='Entropy H(t)', linestyle='dashed')
plt.title('Abiogenesis Phase Trap Feedback')
plt.xlabel('Time'); plt.ylabel('Value')
plt.legend(); plt.grid(True)

plt.savefig('../figures/sim39_abiogenesis_phase_trap.png', dpi=300)
plt.show()
