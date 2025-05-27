# File: C:\Users\Shane\EonSystem\Factory\apps\aenternova\URFT-Simulations\engine\collapse_potential.py

import numpy as np
from .constants import PSI_CRITICAL

def compute_collapse_potential(rho, phi, grad_phi):
    """
    Compute collapse potential Ψ = |∇φ|² / ρ
    where:
        rho — coherence density field
        phi — phase field
        grad_phi — precomputed gradient of phase field
    Returns:
        Ψ field array, same shape as rho
    """
    grad_phi_sq = np.sum(grad_phi**2, axis=0)  # sum over spatial dims
    with np.errstate(divide='ignore', invalid='ignore'):
        psi = np.where(rho > 0, grad_phi_sq / rho, 0.0)
    return psi

def collapse_mask(psi):
    """
    Returns a boolean mask where collapse occurs (Ψ > Ψ_critical)
    """
    return psi > PSI_CRITICAL

def collapse_probability(psi):
    """
    Optional: Soft collapse probability model (e.g., logistic or exponential)
    """
    return 1.0 / (1.0 + np.exp(-(psi - PSI_CRITICAL) * 10))
