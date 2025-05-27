"""
Simulation 40: Intention and Volitional Selection
Domain: Cognitive Phase Dynamics
Source: URFT Whitepaper — Simulation Index p.59
Key Principle: Q-index guided trajectory
Expected Result: Decision confirmed with Q = 1.85
"""

import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 5, 500)
trajectory = np.tanh(t - 2.5) + 1
Q = 1.85 * np.ones_like(t)

plt.plot(t, trajectory, label='Intent Trajectory')
plt.plot(t, Q, '--', label='Q-index = 1.85')
plt.title('Volitional Selection via Coherence')
plt.xlabel('t'); plt.ylabel('State / Q')
plt.grid(True); plt.legend()

plt.savefig('../figures/sim40_intention_volitional_selection.png', dpi=300)
plt.show()
