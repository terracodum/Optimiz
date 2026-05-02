import numpy as np
from scipy.optimize import minimize
from prettytable import PrettyTable


def penalty_method(func, constraints, x0, eps, r0=1.0, growth=10.0):
    """
    Метод штрафных функций (внешняя точка).
    constraints: список функций g_i(x) >= 0
    alpha(x) = sum(max(0, -g_i(x))^2)
    r растёт каждую итерацию
    """
    print("\nМетод штрафных функций")
    table = PrettyTable()
    table.field_names = ["iter", "r", "x1", "x2", "f(x)", "r·alpha"]

    x = np.array(x0, dtype=float)
    r = r0

    for k in range(50):
        def alpha(x):
            return sum(max(0.0, -g(x)) ** 2 for g in constraints)

        def P(x, r=r):
            return func(x) + r * alpha(x)

        res = minimize(P, x, method='Nelder-Mead',
                       options={'xatol': 1e-10, 'fatol': 1e-10, 'maxiter': 10000})
        x = res.x

        r_alpha = r * alpha(x)

        table.add_row([k + 1, f"{r:.2f}", f"{x[0]:.6f}", f"{x[1]:.6f}",
                       f"{func(x):.6f}", f"{r_alpha:.6f}"])

        if r_alpha < eps:
            break

        r *= growth

    print(table)
    print(f"Оптимальное решение: x1 = {x[0]:.4f}, x2 = {x[1]:.4f}, f(x) = {func(x):.4f}")
    return x.tolist()
