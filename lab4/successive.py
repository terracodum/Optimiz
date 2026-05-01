import numpy as np
from scipy.optimize import minimize
from prettytable import PrettyTable


def successive_pareto(funcs, n_points=10):
    f1, f2, f3 = funcs
    print("\nМетод последовательных уступок")
    table = PrettyTable()
    table.field_names = ["#", "delta1", "delta2", "x1", "x2", "f1", "f2", "f3"]

    # Шаг 1: безусловный минимум f1
    res1 = minimize(f1, [0.0, 0.0], method='Nelder-Mead', options={'xatol': 1e-9})
    x1_star = res1.x
    f1_star = f1(x1_star)

    # 10 точек: меняем уступки delta1 (для f1) и delta2 (для f2)
    # Пять значений delta1 × два значения delta2 = 10 точек
    delta1_vals = np.linspace(5, 200, 5)
    delta2_vals = [30, 120]

    points = []
    idx = 1
    for d1 in delta1_vals:
        # Шаг 2: минимум f2 при ограничении на f1
        c1 = [{'type': 'ineq', 'fun': lambda x, d=d1, f=f1_star: d - (f1(x) - f)}]
        res2 = minimize(f2, [0.0, 0.0], method='SLSQP', constraints=c1,
                        options={'ftol': 1e-9})
        f2_star = f2(res2.x)

        for d2 in delta2_vals:
            # Шаг 3: минимум f3 при ограничениях на f1 и f2
            c2 = c1 + [{'type': 'ineq', 'fun': lambda x, d=d2, f=f2_star: d - (f2(x) - f)}]
            res3 = minimize(f3, [0.0, 0.0], method='SLSQP', constraints=c2,
                            options={'ftol': 1e-9})
            x = res3.x
            points.append(x.tolist())
            table.add_row([idx,
                           f"{d1:.1f}", f"{d2:.1f}",
                           f"{x[0]:.4f}", f"{x[1]:.4f}",
                           f"{f1(x):.4f}", f"{f2(x):.4f}", f"{f3(x):.4f}"])
            idx += 1

    print(table)
    return points
