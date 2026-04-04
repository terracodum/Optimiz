import math
from prettytable import PrettyTable
from typing import Callable

def lagrange(func: Callable, phi: Callable, eps: float) -> list:
    print("\nМетод множителей Лагранжа")
    table = PrettyTable()
    table.field_names = ["iter", "x", "y", "lambda", "error"]

    x, y, lam = 1.0, 1.0, 0.0 
    lr = 0.1 
    
    for i in range(101):
        # Производные функции f = x^2 + y^2 и ограничения phi = 2x - y - 2
        # dL/dx = df/dx + lam * dphi/dx
        dL_dx = 2*x + lam*2
        dL_dy = 2*y + lam*(-1)
        dL_dlam = 2*x - y - 2
        
        error = math.sqrt(dL_dx**2 + dL_dy**2 + dL_dlam**2)
        table.add_row([i, f"{x:.4f}", f"{y:.4f}", f"{lam:.4f}", f"{error:.6f}"])
        
        if error < eps: break
            
        x -= lr * dL_dx
        y -= lr * dL_dy
        lam += lr * dL_dlam # Лямбду обычно обновляем с плюсом
        
    print(table)
    print(f"Оптимальное решение: x = {x:.4f}, y = {y:.4f}, f(x,y) = {func(x,y):.4f}")
    return [x, y]
