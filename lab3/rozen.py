import math
from prettytable import PrettyTable
from typing import Callable

def rozen(func: Callable, phi: Callable, eps: float, maximize: bool = False) -> list:
    mode = "максимум" if maximize else "минимум"
    print(f"\nМетод проекции градиента (Розена) — {mode}")
    table = PrettyTable()
    table.field_names = ["iter", "x", "y", "step", "f()", "phi()"]

    x, y = 1.0, 0.0
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

        norm_s = math.sqrt(sx**2 + sy**2)
        if norm_s < eps:
            break

        sign = 1 if maximize else -1
        nx, ny = x + sign * step * sx, y + sign * step * sy

        improved = func(nx, ny) > func(x, y) if maximize else func(nx, ny) < func(x, y)
        if not improved:
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
