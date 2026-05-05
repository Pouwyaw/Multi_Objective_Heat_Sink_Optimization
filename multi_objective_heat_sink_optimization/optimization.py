import numpy as np
from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.algorithms.soo.nonconvex.ga import GA
from pymoo.optimize import minimize
from pymoo.termination import get_termination

from model import solve_temperature, compute_cost, compute_constraints


class HeatSinkProblem(ElementwiseProblem):
    def __init__(self):
        xl = np.array([1.0, 10.0, 3.0, 80.0, 100.0])
        xu = np.array([5.0, 100.0, 10.0, 100.0, 150.0])
        super().__init__(n_var=5, n_obj=2, n_constr=3, xl=xl, xu=xu)

    def _evaluate(self, x, out, *args, **kwargs):
        t, L, n, W, Y = x
        n = int(np.clip(np.rint(n), 3, 10))

        T = solve_temperature(t, L, n, W, Y)
        Z = compute_cost(t, L, n, Y)

        out["F"] = [T, Z]
        out["G"] = compute_constraints(t, L, n, W, Y)


def run_nsga2():
    problem = HeatSinkProblem()

    algorithm = NSGA2(pop_size=200)
    termination = get_termination("n_gen", 200)

    res = minimize(problem, algorithm, termination, seed=42, verbose=True)
    return res


def run_weighted(weights):
    results = []

    for w1, w2 in weights:
        class WeightedProblem(HeatSinkProblem):
            def _evaluate(self, x, out, *args, **kwargs):
                t, L, n, W, Y = x
                n = int(np.clip(np.rint(n), 3, 10))

                T = solve_temperature(t, L, n, W, Y)
                Z = compute_cost(t, L, n, Y)

                out["F"] = w1 * T + w2 * Z
                out["G"] = compute_constraints(t, L, n, W, Y)

        res = minimize(WeightedProblem(), GA(pop_size=200), ("n_gen", 200), seed=1)
        results.append(res)

    return results