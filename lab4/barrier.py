import numpy as np
from scipy.optimize import minimize
from prettytable import PrettyTable


def _P_barrier(x, r, func, constraints):
    g_vals = [g(x) for g in constraints]
    if any(gv <= 1e-12 for gv in g_vals):
        return 1e10
    return func(x) + r * sum(-np.log(gv) for gv in g_vals)


def barrier_method(func, constraints, x0, eps, r0=1.0, decay=0.1):
    print("\nМетод барьерных функций")
    table = PrettyTable()
    table.field_names = ["iter", "r", "x1", "x2", "f(x)", "r·barrier"]

    x = np.array(x0, dtype=float)
    r = r0

    for k in range(50):
        res = minimize(_P_barrier, x, args=(r, func, constraints), method='Nelder-Mead', options={'xatol': 1e-10, 'fatol': 1e-10, 'maxiter': 10000})
        x = res.x

        g_vals = [g(x) for g in constraints]
        barrier_val = sum(-np.log(max(gv, 1e-12)) for gv in g_vals)
        r_barrier = r * barrier_val

        table.add_row([k + 1, f"{r:.6f}", f"{x[0]:.6f}", f"{x[1]:.6f}", f"{func(x):.6f}", f"{r_barrier:.6f}"])

        if abs(r_barrier) < eps:
            break

        r *= decay

    print(table)
    print(f"Оптимальное решение: x1 = {x[0]:.4f}, x2 = {x[1]:.4f}, f(x) = {func(x):.4f}")
    return x.tolist()
