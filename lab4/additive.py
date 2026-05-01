import numpy as np
from scipy.optimize import minimize
from prettytable import PrettyTable


def additive_pareto(funcs, n_points=10):
    f1, f2, f3 = funcs
    print("\nМетод аддитивной свертки")
    table = PrettyTable()
    table.field_names = ["#", "a1", "a2", "a3", "x1", "x2", "f1", "f2", "f3"]

    # 10 наборов весов — варьируем чтобы получить разные точки Парето
    weights = [
        (1.00, 0.00, 0.00),
        (0.00, 1.00, 0.00),
        (0.00, 0.00, 1.00),
        (0.50, 0.50, 0.00),
        (0.50, 0.00, 0.50),
        (0.00, 0.50, 0.50),
        (0.33, 0.33, 0.34),
        (0.60, 0.30, 0.10),
        (0.10, 0.60, 0.30),
        (0.30, 0.10, 0.60),
    ]

    points = []
    for i, (a1, a2, a3) in enumerate(weights):
        F = lambda x, a1=a1, a2=a2, a3=a3: a1 * f1(x) + a2 * f2(x) + a3 * f3(x)
        res = minimize(F, [0.0, 0.0], method='Nelder-Mead',
                       options={'xatol': 1e-8, 'fatol': 1e-8, 'maxiter': 10000})
        x = res.x
        points.append(x.tolist())
        table.add_row([i + 1,
                       f"{a1:.2f}", f"{a2:.2f}", f"{a3:.2f}",
                       f"{x[0]:.4f}", f"{x[1]:.4f}",
                       f"{f1(x):.4f}", f"{f2(x):.4f}", f"{f3(x):.4f}"])

    print(table)
    return points
