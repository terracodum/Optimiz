import math
from prettytable import PrettyTable
from typing import Callable

def lagrange(func: Callable, phi: Callable, eps: float, maximize: bool = False) -> list:
    mode = "максимум" if maximize else "минимум"
    print(f"\nМетод множителей Лагранжа — {mode}")
    table = PrettyTable()
    table.field_names = ["iter", "x", "y", "lambda", "error"]

    x, y, lam = 1.0, 1.0, 0.0
    lr = 0.1
    delta = 1e-6

    for i in range(101):
        df_dx = (func(x + delta, y) - func(x, y)) / delta
        df_dy = (func(x, y + delta) - func(x, y)) / delta
        dphi_dx = (phi(x + delta, y) - phi(x, y)) / delta
        dphi_dy = (phi(x, y + delta) - phi(x, y)) / delta

        dL_dx = df_dx + lam * dphi_dx
        dL_dy = df_dy + lam * dphi_dy
        dL_dlam = phi(x, y)

        error = math.sqrt(dL_dx**2 + dL_dy**2 + dL_dlam**2)
        table.add_row([i, f"{x:.4f}", f"{y:.4f}", f"{lam:.4f}", f"{error:.6f}"])

        if error < eps: break

        # При maximize=True знак по y переворачивается (Гессиан по y отрицательный)
        y_sign = 1 if maximize else -1
        x -= lr * dL_dx
        y += y_sign * lr * dL_dy
        lam += lr * dL_dlam
        
    print(table)
    print(f"Оптимальное решение: x = {x:.4f}, y = {y:.4f}, f(x,y) = {func(x,y):.4f}")
    return [x, y]
