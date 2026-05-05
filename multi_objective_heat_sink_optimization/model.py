import numpy as np
from scipy.optimize import brentq, root_scalar

# Constants
k = 201.0
h = 70.0
T_inf = 25.0
rho = 2700.0
P_loss = 110.0


def solve_temperature(t_mm, L_mm, n, W_mm, Y_mm):
    t = t_mm / 1000
    L = L_mm / 1000
    W = W_mm / 1000

    Ac = t * W
    P = 2 * (t + W)
    m = np.sqrt(h * P / (k * Ac + 1e-16))

    A_nofin = (Y_mm * W_mm - n * t_mm * W_mm) / 1e6

    fin_factor = np.sqrt(h * P * k * Ac)

    num = np.sinh(m * L) + (h / (m * k)) * np.cosh(m * L)
    den = np.cosh(m * L) + (h / (m * k)) * np.sinh(m * L)

    def Qfin(T):
        return (T - T_inf) * fin_factor * (num / (den + 1e-16))

    def Qnofin(T):
        return (T - T_inf) * h * A_nofin

    def balance(T):
        return n * Qfin(T) + Qnofin(T) - P_loss

    Tlo, Thi = T_inf + 0.1, 500

    try:
        return brentq(balance, Tlo, Thi)
    except:
        sol = root_scalar(balance, x0=80, method='secant')
        return sol.root if sol.converged else np.inf


def compute_cost(t_mm, L_mm, n, Y_mm):
    return 0.019 * (n * L_mm * np.sqrt(max(t_mm, 0)) + Y_mm)


def compute_constraints(t, L, n, W, Y):
    V_base = (W * Y * 1.0) / 1e9
    V_fin = (t * L * W) / 1e9
    mass = rho * (V_base + n * V_fin)

    if Y <= n * t:
        gap = -1e6
    else:
        gap = (Y - n * t) / (n - 1)

    return [
        mass - 0.685,
        4 * t - gap,
        gap - 8 * t
    ]