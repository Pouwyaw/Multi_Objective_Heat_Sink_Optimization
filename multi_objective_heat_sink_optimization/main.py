from optimization import run_nsga2, run_weighted
from utils import plot_pareto, find_knee


def main():
    res = run_nsga2()
    F = res.F

    plot_pareto(F)

    knee, ideal = find_knee(F)

    print("Ideal:", ideal)
    print("Knee:", knee)

    weights = [(0.1,0.9), (0.5,0.5), (0.7,0.3)]
    weighted_results = run_weighted(weights)

    print("\nWeighted Results:")
    for r in weighted_results:
        print(r.F)


if __name__ == "__main__":
    main()