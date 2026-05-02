import numpy as np
from scipy.optimize import minimize
from prettytable import PrettyTable


def discriminant_pareto(funcs, n_points=10):
    n = len(funcs)
    print("\nДискриминационный метод")

    # Безусловные минимумы всех функций кроме последней
    f_mins = []
    for fi in funcs[:-1]:
        res = minimize(fi, [0.0, 0.0], method='Nelder-Mead')
        f_mins.append(fi(res.x))

    # Диапазоны ограничений: от жёстких до мягких
    lim_ranges = [np.linspace(fmin + 20, fmin + 500, n_points) for fmin in f_mins]

    table = PrettyTable()
    table.field_names = (["#"] + [f"lim_f{i+1}" for i in range(n - 1)] + ["x1", "x2"] + [f"f{i+1}" for i in range(n)])

    points = []
    for i in range(n_points):
        constraints = [
            {'type': 'ineq', 'fun': lambda x, fi=funcs[j], l=lim_ranges[j][i]: l - fi(x)}
            for j in range(n - 1)
        ]
        res = minimize(funcs[-1], [0.0, 0.0], method='SLSQP', constraints=constraints, options={'ftol': 1e-9, 'maxiter': 1000})
        x = res.x
        points.append(x.tolist())
        table.add_row([i + 1] + [f"{lim_ranges[j][i]:.1f}" for j in range(n - 1)] + [f"{x[0]:.4f}", f"{x[1]:.4f}"] + [f"{funcs[j](x):.4f}" for j in range(n)])

    print(table)
    return points
