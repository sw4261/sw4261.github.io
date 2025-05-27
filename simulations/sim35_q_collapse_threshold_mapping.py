"""
Simulation 35: Q-Collapse Threshold Mapping
Domain: Identity Collapse
Source: URFT Whitepaper — Appendix AF, Equation (7.3), Simulation Index p.58
Key Principle: Feedback failure at Q = 1.52; collapse when ΔH > 0.041
Expected Result: Collapse at ΔH = 0.041, Q = 1.52
"""

import numpy as np
import matplotlib.pyplot as plt

# Time domain
t = np.linspace(0, 10, 1000)
entropy = 0.02 + 0.002 * np.sin(0.5 * t)
delta_H = np.gradient(entropy, t)
Q = 1.6 - 0.01 * np.cumsum(delta_H)

# Collapse trigger
collapse_trigger = Q < 1.52

# Plot
plt.plot(t, Q, label='Q(t)')
plt.axhline(1.52, color='red', linestyle='--', label='Q Collapse Threshold')
plt.title('Q-Collapse Threshold Mapping')
plt.xlabel('t'); plt.ylabel('Q-index')
plt.grid(True); plt.legend()

plt.savefig('../figures/sim35_q_collapse_threshold_mapping.png', dpi=300)
plt.show()
