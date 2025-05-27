# File: C:\Users\Shane\EonSystem\Factory\apps\aenternova\URFT-Simulations\engine\constants.py

import numpy as np

# Fundamental URFT Constants (from Appendix E, H)
ALPHA = 1 / 137.035999  # Fine-structure constant (CODATA match)
H_BAR = 1.054571817e-34  # Planck constant / 2π [J·s]
C = 299792458           # Speed of light [m/s]
G = 6.67430e-11         # Gravitational constant [m^3/kg/s^2]

# URFT-Specific Field Constants (from Appendix E.12)
LAMBDA = 3.91e-3        # Phase tension coefficient
GAMMA = 1.42e2          # Frequency variance coupling
KAPPA_0 = 7.54e6        # Base wavenumber for trap quantization

# Collapse Thresholds (from Appendix L)
Q_THRESHOLD = 1.5       # Minimum coherence for stable identity
PSI_CRITICAL = 0.17     # Collapse potential threshold (normalized)

# Useful Math Constants
PI = np.pi
TWO_PI = 2 * np.pi
