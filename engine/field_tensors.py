# File: C:\Users\Shane\EonSystem\Factory\apps\aenternova\URFT-Simulations\engine\field_tensors.py

import numpy as np
from .constants import ALPHA

def compute_R_mu(rho, grad_phi):
    """
    Resonance vector field R_mu = ∇φ * ρ
    """
    return grad_phi * rho

def compute_F_mu_nu(R_mu):
    """
    Antisymmetric resonance field tensor:
    F_{μν} = ∂_μ R_ν - ∂_ν R_μ
    Assumes R_mu is an array of shape (dim, ...)
    """
    dim = R_mu.shape[0]
    F = np.zeros((dim, dim) + R_mu.shape[1:])
    for mu in range(dim):
        for nu in range(dim):
            F[mu, nu] = np.gradient(R_mu[nu], axis=mu) - np.gradient(R_mu[mu], axis=nu)
    return F

def compute_C_mu_nu(rho, R_mu):
    """
    Coherence curvature tensor:
    C_{μν} = ∂_μ ∂_ν ρ + α (∂_μ R_ν - ∂_ν R_μ)
    """
    dim = R_mu.shape[0]
    C = np.zeros((dim, dim) + rho.shape)
    for mu in range(dim):
        for nu in range(dim):
            second_derivative = np.gradient(np.gradient(rho, axis=nu), axis=mu)
            F_mu_nu = np.gradient(R_mu[nu], axis=mu) - np.gradient(R_mu[mu], axis=nu)
            C[mu, nu] = second_derivative + ALPHA * F_mu_nu
    return C
