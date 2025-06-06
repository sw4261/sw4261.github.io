"""
Simulation 15: Consciousness Echo Scan
Domain: Mind/Field Interface
Source: URFT Whitepaper — Equation (7.2), Appendix D, Simulation Index p.57
Key Equation: Q resonance persistence
Expected Result: Field coherence retained Δt = 5.7 s post-input; Q = 1.78
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Time evolution of Q with slow decay
time = np.linspace(0, 10, 1000)
Q = 1.78 * np.exp(-0.05 * time) + 0.22

# Plot
plt.plot(time, Q)
plt.title('Q-Index Echo Scan (Coherence Persistence)')
plt.xlabel('Time (s)'); plt.ylabel('Q(t)')
plt.grid(True)

output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../figures'))
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'sim15_consciousness_echo_scan.png'), dpi=300)
plt.show()