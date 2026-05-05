import numpy as np
import matplotlib.pyplot as plt
import os


def plot_pareto(F):
    os.makedirs("results", exist_ok=True)

    plt.figure()
    plt.scatter(F[:, 0], F[:, 1])
    plt.xlabel("Temperature (°C)")
    plt.ylabel("Cost (Z)")
    plt.title("Pareto Front")
    plt.grid(True)

    plt.savefig("results/pareto.png", dpi=300)
    plt.close()


def find_knee(F):
    Fmin, Fmax = F.min(axis=0), F.max(axis=0)
    Fn = (F - Fmin) / (Fmax - Fmin + 1e-12)

    ideal = Fn.min(axis=0)
    d = np.linalg.norm(Fn - ideal, axis=1)

    return F[np.argmin(d)], F.min(axis=0)