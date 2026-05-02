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

        # Градиент phi численно → касательная к phi=0: перпендикуляр (-dpy, dpx)
        dpx = (phi(x + delta, y) - phi(x, y)) / delta
        dpy = (phi(x, y + delta) - phi(x, y)) / delta
        tx, ty = -dpy, dpx
        norm_t = tx**2 + ty**2
        proj_s = (gx * tx + gy * ty) / norm_t
        sx, sy = proj_s * tx, proj_s * ty

        # Условие остановки: проекция градиента мала — достигнут экстремум на ограничении
        norm_s = math.sqrt(sx**2 + sy**2)
        if norm_s < eps:
            break

        # Идём в сторону РОСТА f (ищем максимум, т.к. f=x²-y² — седло)
        nx, ny = x + step * sx, y + step * sy

        if func(nx, ny) <= func(x, y):
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
