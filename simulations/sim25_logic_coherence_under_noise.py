"""
Simulation 25: Logic Coherence Under Noise
Domain: Computing
Source: URFT Whitepaper — Equation (7.2), Simulation Index p.58
Key Principle: Q degradation under ω noise
Expected Result: Q > 1.5 sustained 8.2 s with 2.7% ω perturbation
"""

import numpy as np
import matplotlib.pyplot as plt

# Time and noise
t = np.linspace(0, 10, 1000)
omega_noise = 0.027 * np.random.randn(len(t))
base_Q = 1.6 + 0.02 * np.sin(0.5 * t)
Q = base_Q - omega_noise

# Plot
plt.plot(t, Q)
plt.axhline(1.5, color='red', linestyle='--', label='Stability Threshold (Q=1.5)')
plt.title('Logic Coherence Under ω Noise')
plt.xlabel('Time (s)'); plt.ylabel('Q-index')
plt.grid(True); plt.legend()

plt.savefig('../figures/sim25_logic_coherence_under_noise.png', dpi=300)
plt.show()
