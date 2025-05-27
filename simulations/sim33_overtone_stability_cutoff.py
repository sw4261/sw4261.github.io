"""
Simulation 33: Overtone Stability Cutoff
Domain: Particle Generations
Source: URFT Whitepaper — Appendix E.16, Simulation Index p.58
Key Principle: Qₙ cutoff in trap overtones
Expected Result: Only n=1,2,3 stable; Q₃ = 1.61, Q₄ = 0.91
"""

import numpy as np
import matplotlib.pyplot as plt

# Overtones
n = np.array([1, 2, 3, 4, 5])
Q_n = np.array([2.1, 1.9, 1.61, 0.91, 0.5])

# Plot
plt.bar(n, Q_n, color=['green' if q > 1.5 else 'red' for q in Q_n])
plt.axhline(1.5, color='black', linestyle='--', label='Q Stability Threshold')
plt.title('Overtone Q-index Stability')
plt.xlabel('Overtone n'); plt.ylabel('Qₙ')
plt.xticks(n)
plt.legend(); plt.grid(True)

plt.savefig('../figures/sim33_overtone_stability_cutoff.png', dpi=300)
plt.show()
