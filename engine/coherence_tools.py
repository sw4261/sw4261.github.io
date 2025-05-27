# File: C:\Users\Shane\EonSystem\Factory\apps\aenternova\URFT-Simulations\engine\coherence_tools.py

import numpy as np
from .constants import Q_THRESHOLD

def compute_gradients(field):
    """
    Computes spatial gradients along all axes.
    Returns array of shape (dim, ...)
    """
    dim = field.ndim
    return np.array([np.gradient(field, axis=i) for i in range(dim)])

def compute_coherence_density(R_mu):
    """
    Compute coherence density ρ = |R_mu| (magnitude of resonance vector)
    Assumes R_mu shape: (dim, ...)
    """
    return np.sqrt(np.sum(R_mu**2, axis=0))

def compute_Q_index(rho, phi, grad_phi):
    """
    Compute coherence quotient Q = ρ / |∇φ|
    """
    grad_phi_mag = np.sqrt(np.sum(grad_phi**2, axis=0))
    with np.errstate(divide='ignore', invalid='ignore'):
        Q = np.where(grad_phi_mag > 0, rho / grad_phi_mag, 0.0)
    return Q

def Q_stable_mask(Q):
    """
    Boolean mask where coherence identity is preserved (Q > Q_threshold)
    """
    return Q > Q_THRESHOLD
