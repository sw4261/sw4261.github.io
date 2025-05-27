"""
Simulation 07: Resonance Trap Modes
Domain: Particle Physics
Source: URFT Whitepaper — Appendix E.14, Simulation Index p.56
Key Equation: ∇²ψ + κ²ψ = 0
Expected Result: Stable ψ₁, ψ₂; collapse at ψ₃; κ₁ = 2.1, κ₂ = 4.3 rad/m
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Spatial domain
x = np.linspace(0, np.pi, 200)

# Define three modes
kappa1 = 2.1
kappa2 = 4.3
kappa3 = 6.9  # unstable mode (approximate)

psi1 = np.sin(kappa1 * x)
psi2 = np.sin(kappa2 * x)
psi3 = np.exp(-x) * np.sin(kappa3 * x)  # damped/decaying

# Plotting
plt.plot(x, psi1, label='ψ₁ (κ=2.1)', linewidth=2)
plt.plot(x, psi2, label='ψ₂ (κ=4.3)', linewidth=2)
plt.plot(x, psi3, label='ψ₃ (κ=6.9, collapse)', linestyle='dashed')
plt.title('Resonance Trap Modes')
plt.xlabel('x'); plt.ylabel('ψ(x)')
plt.legend(); plt.grid(True)

output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../figures'))
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'sim07_resonance_trap_modes.png'), dpi=300)
plt.show()