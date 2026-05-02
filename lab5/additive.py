import numpy as np
from scipy.optimize import minimize
from prettytable import PrettyTable


def additive_pareto(funcs, n_points=10):
    n = len(funcs)
    print("\nМетод аддитивной свертки")

    # n угловых точек (один критерий с весом 1), остаток — случайные Дирихле
    rng = np.random.default_rng(42)
    weights = np.zeros((n_points, n))
    for i in range(min(n, n_points)):
        weights[i][i] = 1.0
    if n_points > n:
        weights[n:] = rng.dirichlet(np.ones(n), size=n_points - n)

    table = PrettyTable()
    table.field_names = (["#"] + [f"a{i+1}" for i in range(n)] + ["x1", "x2"] + [f"f{i+1}" for i in range(n)])

    points = []
    for i, w in enumerate(weights):
        F = lambda x, w=w: sum(w[j] * funcs[j](x) for j in range(n))
        res = minimize(F, [0.0, 0.0], method='Nelder-Mead', options={'xatol': 1e-8, 'fatol': 1e-8, 'maxiter': 10000})
        x = res.x
        points.append(x.tolist())
        table.add_row([i + 1] + [f"{w[j]:.2f}" for j in range(n)] + [f"{x[0]:.4f}", f"{x[1]:.4f}"] + [f"{funcs[j](x):.4f}" for j in range(n)])

    print(table)
    return points
