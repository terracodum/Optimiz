import math
from prettytable import PrettyTable
from typing import Callable

def zoutendijk(func: Callable, phi: Callable, eps: float) -> list:
    print("\nМетод Зойтендейка")
    table = PrettyTable()
    table.field_names = ["iter", "x", "y", "step", "f()", "phi()"]
    
    x, y = 1.0, 0.0
    step = 0.1
    delta = 1e-6
    
    for i in range(101):
        df_dx = (func(x + delta, y) - func(x, y)) / delta
        df_dy = (func(x, y + delta) - func(x, y)) / delta
        
        # Направление вдоль линии [1, 2]
        sx, sy = 1.0, 2.0
        
        # Выбираем направление спуска по линии
        if (df_dx * sx + df_dy * sy) > 0:
            sx, sy = -sx, -sy
            
        nx, ny = x + step * sx, y + step * sy
        
        table.add_row([i, f"{x:.4f}", f"{y:.4f}", f"{step:.4f}", f"{func(x,y):.4f}", f"{phi(x,y):.4f}"])
        
        if func(nx, ny) > func(x, y):
            step /= 2
            if step < eps: break
            continue

        if math.sqrt((nx - x)**2 + (ny - y)**2) < eps: break
        x, y = nx, ny
        
    print(table)
    print(f"Оптимальное решение: x = {x:.4f}, y = {y:.4f}, f(x,y) = {func(x,y):.4f}")
    return [x, y]
