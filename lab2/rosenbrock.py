import math
from prettytable import PrettyTable
from typing import Callable

def rosen(func: Callable, eps: float) -> list:
    print("\nМетод Розенброка")
    table = PrettyTable()
    table.field_names = ["iter_num", "x", "y", "step_x", "step_y"]

    x, y = 0.0, 0.0
    steps = [0.1, 0.1]
    itter = 0
    
    d = [[1.0, 0.0], [0.0, 1.0]]
    
    table.add_row([f"{itter}", f"{x:.4f}", f"{y:.4f}", f"{steps[0]:.4f}", f"{steps[1]:.4f}"])

    while max(abs(steps[0]), abs(steps[1])) > eps:
        itter += 1
        x_before, y_before = x, y

        for i in range(2):
            nx = x + steps[i] * d[i][0]
            ny = y + steps[i] * d[i][1]
            
            if func(nx, ny) < func(x, y):
                x, y = nx, ny
                steps[i] *= 2.0  
            else:
                steps[i] *= -0.5
        
        dx = x - x_before
        dy = y - y_before
        dist = math.sqrt(dx**2 + dy**2)
        
        if dist > eps:
            d[0][0], d[0][1] = dx / dist, dy / dist
            d[1][0], d[1][1] = -d[0][1], d[0][0]

        table.add_row([f"{itter}", f"{x:.4f}", f"{y:.4f}", f"{steps[0]:.6f}", f"{steps[1]:.6f}"])
        
        if itter > 500: break

    print(table)
    print(f"Минимальный x = {x}, Минимальный y = {y}")
    return [x, y]
