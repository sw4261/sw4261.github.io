## File: C:\Users\Shane\EonSystem\Factory\apps\aenternova\URFT-Simulations\engine\rk4_solver.py

import numpy as np

def rk4_step(func, y, t, dt, **kwargs):
    """
    Perform a single Runge-Kutta 4th order step.
    
    Parameters:
        func: callable, the derivative function dy/dt = f(y, t)
        y: np.ndarray, current state vector
        t: float, current time
        dt: float, time step
        **kwargs: additional arguments passed to func

    Returns:
        y_next: np.ndarray, updated state after time step
    """
    k1 = func(y, t, **kwargs)
    k2 = func(y + 0.5 * dt * k1, t + 0.5 * dt, **kwargs)
    k3 = func(y + 0.5 * dt * k2, t + 0.5 * dt, **kwargs)
    k4 = func(y + dt * k3, t + dt, **kwargs)
    return y + (dt / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)
 RK4 integrator for field evolution
