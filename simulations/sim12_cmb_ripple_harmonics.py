"""
Simulation 12: CMB Ripple Harmonics
Domain: Cosmology
Source: URFT Whitepaper — Section 6.7, Appendix E.23, Simulation Index p.57
Key Principle: FFT of radial density ripple
Expected Result: CMB peaks ℓ = 2–5; Δρ_ripple = 0.013
"""

import numpy as np
import matplotlib.pyplot as plt

# Radial ripple burst
r = np.linspace(0, 10, 1024)
rho = np.sin(2 * np.pi * r / 2.5) * np.exp(-r / 3)  # phase burst decay

# FFT for harmonic spectrum
fft_rho = np.abs(np.fft.rfft(rho))
freqs = np.fft.rfftfreq(len(r), d=(r[1]-r[0]))

# Plot
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(r, rho)
plt.title('Radial Coherence Ripple')
plt.xlabel('r'); plt.ylabel('ρ(r)')

plt.subplot(1, 2, 2)
plt.plot(freqs, fft_rho)
plt.title('Fourier Spectrum (CMB Harmonics)')
plt.xlabel('Frequency'); plt.ylabel('Amplitude')

plt.tight_layout()
plt.savefig('../figures/sim12_cmb_ripple_harmonics.png', dpi=300)
plt.show()
