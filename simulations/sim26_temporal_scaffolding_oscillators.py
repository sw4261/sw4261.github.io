"""
Simulation 26: Temporal Scaffolding Oscillators
Domain: Time Memory
Source: URFT Whitepaper — Equation (4.1), Simulation Index p.58
Key Principle: Recurrent φ loop timing
Expected Result: Δφ = 2π at ω = 2230 rad/s; reset lag = 18 ms
"""

import numpy as np
import matplotlib.pyplot as plt
import os

# Time domain
t = np.linspace(0, 50, 1000)  # ms
omega = 2230  # rad/s
phi = np.mod(omega * t * 1e-3, 2 * np.pi)  # convert ms to s

# Detect reset lag
reset_lag = 18  # ms
reset_trigger = (t % reset_lag) < 1  # spike at every lag

# Plot
plt.plot(t, phi, label='ϕ(t)')
plt.plot(t[reset_trigger], phi[reset_trigger], 'ro', label='Reset Points')
plt.title('Temporal Scaffolding Oscillators')
plt.xlabel('Time (ms)'); plt.ylabel('ϕ(t)')
plt.legend(); plt.grid(True)

output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../figures'))
os.makedirs(output_dir, exist_ok=True)
plt.savefig(os.path.join(output_dir, 'sim26_temporal_scaffolding_oscillators.png'), dpi=300)
plt.show()