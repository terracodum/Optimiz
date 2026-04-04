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
        # Численный градиент f
        gx = (func(x + delta, y) - func(x, y)) / delta
        gy = (func(x, y + delta) - func(x, y)) / delta
        
        # Проекция на линию 2x - y - 2 = 0 (направление s = [1, 2])
        proj_s = (gx * 1 + gy * 2) / (1**2 + 2**2)
        sx, sy = proj_s * 1, proj_s * 2

        nx, ny = x - step * sx, y - step * sy

        table.add_row([itter, f"{x:.4f}", f"{y:.4f}", f"{step:.4f}", f"{func(x, y):.4f}", f"{phi(x, y):.4f}"])

        # АДАПТАЦИЯ: если стало хуже — дробим шаг
        if func(nx, ny) > func(x, y):
            step /= 2
            if step < eps: break
            continue 
            
        if math.sqrt((nx - x)**2 + (ny - y)**2) < eps: break
            
        x, y = nx, ny
        itter += 1

    print(table)
    print(f"Оптимальное решение: x = {x:.4f}, y = {y:.4f}, f(x,y) = {func(x,y):.4f}")
    return [x, y]
