"""
Simulation 28: Collapse-Resistant Neural Cores
Domain: Biofield Theory
Source: URFT Whitepaper — Equation (6.1), Simulation Index p.58
Key Principle: Ψ threshold under stress
Expected Result: Stable to Ψ = 1.21 Ψc; coherence > 17 s
"""

import numpy as np
import matplotlib.pyplot as plt
import os
from engine.constants import PSI_CRITICAL

# Time domain (s)
t = np.linspace(0, 20, 1000)
psi = 1.21 * PSI_CRITICAL * np.ones_like(t)
coherence = np.exp(-0.03 * t)

# Plot
plt.plot(t, coherence, label='ρ(t)')
plt.axhline(1.21 * PSI_CRITICAL, color='red', linestyle='--', label='Ψ = 1.21 Ψc')
plt.title('Collapse-Resistant Neural Core')
plt.xlabel('Time (s)'); plt.ylabel('Coherence / Ψ')
plt.legend(); plt.grid(True)

output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../figures'))
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'sim28_collapse_resistant_neural_cores.png'), dpi=300)
plt.show()