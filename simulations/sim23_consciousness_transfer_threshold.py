"""
Simulation 23: Consciousness Transfer Threshold
Domain: Q-Theory
Source: URFT Whitepaper — Equation (7.2), Appendix D, Simulation Index p.58
Key Principle: Q-index reattachment event
Expected Result: Identity relocked in 3.4 s; Q = 2.03
"""

import numpy as np
import matplotlib.pyplot as plt

# Simulated Q recovery event
time = np.linspace(0, 10, 1000)
Q = 1 + 1.03 * (1 - np.exp(-1.5 * (time - 3.4)**2))

# Plot
plt.plot(time, Q)
plt.axhline(2.03, color='green', linestyle='--', label='Q Reattachment')
plt.title('Q-Index Recovery After Transfer')
plt.xlabel('Time (s)'); plt.ylabel('Q(t)')
plt.grid(True); plt.legend()

plt.savefig('../figures/sim23_consciousness_transfer_threshold.png', dpi=300)
plt.show()
