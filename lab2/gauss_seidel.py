import math
from prettytable import PrettyTable
from typing import Callable


def gauss(func: Callable, eps: float) -> list:
    print("\nМетод Гаусса-Зейделя")
    table = PrettyTable()
    table.field_names = ["iter_num", "x", "y", "step", "dist", "f()"]

    step = 0.1
    itter = 0
    x = 0
    y = 0
    dist =  100

    table.add_row([f"{itter}", f"{x:.4f}", f"{y:.4f}", f"{step:.4f}", f"{dist:.4f}", f"{func(x, y):.4f}"])

    while dist > eps:
        itter += 1
        x_old, y_old = x, y

        while func(x + step, y) < func(x, y):
            x += step
        while func(x - step, y) < func(x, y):
            x -= step

        # Поиск по Y
        while func(x, y + step) < func(x, y):
            y += step
        while func(x, y - step) < func(x, y):
            y -= step

        dist = math.sqrt((x - x_old) ** 2 + (y - y_old) ** 2)
        if dist < step: # Если сдвиг меньше шага, значит пора уточняться
            step /= 2

        table.add_row([f"{itter}", f"{x:.4f}", f"{y:.4f}", f"{step:.4f}", f"{dist:.4f}", f"{func(x, y):.4f}"])\
        
    print(table)
    print(f"Минимальный x = {x}, Минимальный y = {y}")
    return [x, y]