"""
Simulation 13: Time Symmetry (Retrocausality)
Domain: Temporal Logic
Source: URFT Whitepaper — Section 2.7, Simulation Index p.57
Key Principle: Phase pre-lock across coherence boundary
Expected Result: Reversal path stable when Δω < 10⁻⁴ rad/s
"""

import numpy as np
import matplotlib.pyplot as plt

# Forward and reverse wave evolution
x = np.linspace(-5, 5, 400)
t_forward = np.sin(2 * np.pi * x)
t_reverse = np.sin(2 * np.pi * (-x))

# Delta omega effect
delta_omega = 1e-4
stability = 1 - delta_omega  # approximate symmetry factor

# Plot
plt.plot(x, t_forward, label='Forward Propagation')
plt.plot(x, t_reverse * stability, label='Reversed with Δω', linestyle='dashed')
plt.title('Retrocausal Phase Symmetry')
plt.xlabel('x'); plt.ylabel('ϕ(x)')
plt.legend(); plt.grid(True)

plt.savefig('../figures/sim13_time_symmetry.png', dpi=300)
plt.show()
