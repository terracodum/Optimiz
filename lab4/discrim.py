import numpy as np
from scipy.optimize import minimize
from prettytable import PrettyTable


def discriminant_pareto(funcs, n_points=10):
    f1, f2, f3 = funcs
    print("\nДискриминационный метод")
    table = PrettyTable()
    table.field_names = ["#", "lim_f1", "lim_f2", "x1", "x2", "f1", "f2", "f3"]

    # Минимальные значения функций в их безусловных минимумах
    x1_min = minimize(f1, [0.0, 0.0], method='Nelder-Mead').x
    x2_min = minimize(f2, [0.0, 0.0], method='Nelder-Mead').x
    f1_min = f1(x1_min)
    f2_min = f2(x2_min)

    # Меняем уступки (ограничения) на f1 и f2, минимизируем f3
    # От жёстких до мягких — получаем разные точки Парето
    lim1_vals = np.linspace(f1_min + 20, f1_min + 500, n_points)
    lim2_vals = np.linspace(f2_min + 15, f2_min + 300, n_points)

    points = []
    for i in range(n_points):
        lim1 = lim1_vals[i]
        lim2 = lim2_vals[i]
        constraints = [
            {'type': 'ineq', 'fun': lambda x, l=lim1: l - f1(x)},
            {'type': 'ineq', 'fun': lambda x, l=lim2: l - f2(x)},
        ]
        res = minimize(f3, [0.0, 0.0], method='SLSQP',
                       constraints=constraints,
                       options={'ftol': 1e-9, 'maxiter': 1000})
        x = res.x
        points.append(x.tolist())
        table.add_row([i + 1,
                       f"{lim1:.1f}", f"{lim2:.1f}",
                       f"{x[0]:.4f}", f"{x[1]:.4f}",
                       f"{f1(x):.4f}", f"{f2(x):.4f}", f"{f3(x):.4f}"])

    print(table)
    return points
