import numpy as np
from scipy.optimize import minimize
from prettytable import PrettyTable


def successive_pareto(funcs, n_points=10):
    n = len(funcs)
    print("\nМетод последовательных уступок")

    # Шаг 1: безусловный минимум первого критерия
    res0 = minimize(funcs[0], [0.0, 0.0], method='Nelder-Mead', options={'xatol': 1e-9})
    f_stars = [funcs[0](res0.x)]
    constraints = []

    # Шаги 2..n-1: фиксируем промежуточные уступки (delta_default),
    # строим цепочку ограничений, запоминаем f*_i
    delta_default = 50.0
    for k in range(1, n - 1):
        constraints.append({
            'type': 'ineq',
            'fun': lambda x, fi=funcs[k - 1], f=f_stars[k - 1]: delta_default - (fi(x) - f)
        })
        res_k = minimize(funcs[k], [0.0, 0.0], method='SLSQP',
                         constraints=constraints, options={'ftol': 1e-9})
        f_stars.append(funcs[k](res_k.x))

    # Последний шаг: варьируем уступку для funcs[-2] → n_points точек Парето
    last_delta_vals = np.linspace(5, 300, n_points)

    table = PrettyTable()
    table.field_names = (["#", "delta_last"]
                         + ["x1", "x2"]
                         + [f"f{i+1}" for i in range(n)])

    points = []
    for idx, d_last in enumerate(last_delta_vals):
        final_constraints = constraints + [{
            'type': 'ineq',
            'fun': lambda x, fi=funcs[-2], f=f_stars[-1]: d_last - (fi(x) - f)
        }]
        res = minimize(funcs[-1], [0.0, 0.0], method='SLSQP',
                       constraints=final_constraints, options={'ftol': 1e-9})
        x = res.x
        points.append(x.tolist())
        table.add_row([idx + 1, f"{d_last:.1f}"]
                      + [f"{x[0]:.4f}", f"{x[1]:.4f}"]
                      + [f"{funcs[j](x):.4f}" for j in range(n)])

    print(table)
    return points
