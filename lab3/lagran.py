import math
from prettytable import PrettyTable
from typing import Callable

def lagrange(func: Callable, phi: Callable, eps: float) -> list:
    print("\nМетод множителей Лагранжа")
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
            
        x -= lr * dL_dx
        y += lr * dL_dy  # y: знак перевёрнут, т.к. f вогнута по y (Гессиан < 0)
        lam += lr * dL_dlam
        
    print(table)
    print(f"Оптимальное решение: x = {x:.4f}, y = {y:.4f}, f(x,y) = {func(x,y):.4f}")
    return [x, y]
