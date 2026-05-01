import math
from prettytable import PrettyTable
from typing import Callable

def rozen(func: Callable, phi: Callable, eps: float) -> list:
    print("\nМетод проекции градиента (Розена)")
    table = PrettyTable()
    table.field_names = ["iter", "x", "y", "step", "f()", "phi()"]
    
    x, y = 1.0, 0.0 # Точка на линии
    step = 0.1
    itter = 0
    delta = 1e-6

    while itter < 100:
        gx = (func(x + delta, y) - func(x, y)) / delta
        gy = (func(x, y + delta) - func(x, y)) / delta

        # Проекция градиента на касательную к линии 2x - y - 2 = 0, направление [1, 2]
        proj_s = (gx * 1 + gy * 2) / 5
        sx, sy = proj_s * 1, proj_s * 2

        # Условие остановки: проекция градиента мала — уже в минимуме
        norm_s = math.sqrt(sx**2 + sy**2)
        if norm_s < eps:
            break

        nx, ny = x - step * sx, y - step * sy

        if func(nx, ny) >= func(x, y):
            step /= 2
            if step < eps * 0.01:
                break
            continue

        table.add_row([itter, f"{x:.4f}", f"{y:.4f}", f"{step:.6f}", f"{func(x, y):.4f}", f"{phi(x, y):.4f}"])
        x, y = nx, ny
        itter += 1

    print(table)
    print(f"Оптимальное решение: x = {x:.4f}, y = {y:.4f}, f(x,y) = {func(x,y):.4f}")
    return [x, y]
