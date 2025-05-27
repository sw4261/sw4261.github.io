"""
Simulation 14: Q-Gate Coherence Logic
Domain: Quantum Computing
Source: URFT Whitepaper — Section 7, Simulation Index p.57
Key Principle: Logic state flip at Ψ = 0.97 Ψc
Expected Result: Reset delay = 3.2 ns
"""

import numpy as np
import matplotlib.pyplot as plt
from engine.constants import PSI_CRITICAL

# Coherence input signal
time = np.linspace(0, 10, 1000)
psi = 0.95 + 0.03 * np.sin(2 * np.pi * time / 3)

# Logic state: 1 if ψ > 0.97 Ψc
psi_threshold = 0.97 * PSI_CRITICAL
logic_state = (psi > psi_threshold).astype(int)

# Plot
plt.plot(time, psi, label='Ψ(t)')
plt.plot(time, logic_state, label='Logic Output (Q-Gate)', linestyle='dashed')
plt.axhline(psi_threshold, color='red', linestyle='dotted', label='0.97 Ψc')
plt.title('Ψ-Gated Logic Flip')
plt.xlabel('Time (ns)'); plt.ylabel('Ψ or State')
plt.legend(); plt.grid(True)

plt.savefig('../figures/sim14_q_gate_coherence_logic.png', dpi=300)
plt.show()
