import math
from prettytable import PrettyTable
from typing import Callable

def get_numerical_gradient(func, x, y, delta=1e-7):
    df_dx = (func(x + delta, y) - func(x, y)) / delta
    df_dy = (func(x, y + delta) - func(x, y)) / delta
    return df_dx, df_dy

def steep(func: Callable, eps: float) -> list:
    print("\nМетод наискорейшего спуска")
    table = PrettyTable()
    table.field_names = ["iter_num", "x", "y", "step", "||Grad||", "f()"]
    
    x, y = 0.0, 0.0
    step = 0.1
    itter = 0
    
    while itter <= 1000:
        dx, dy = get_numerical_gradient(func, x, y)
        grad_norm = math.sqrt(dx**2 + dy**2)
        
        table.add_row([itter, f"{x:.4f}", f"{y:.4f}", f"{step:.4f}", f"{grad_norm:.6f}", f"{func(x, y):.4f}"])
        
        if grad_norm < eps:
            break
            
        # Проверка шага (Чтобы не улететь в 22.0)
        new_x = x - step * dx
        new_y = y - step * dy
        
        # Если шаг плохой (f стала больше), уменьшаем его в 2 раза
        while func(new_x, new_y) >= func(x, y) and step > 1e-10:
            step /= 2
            new_x = x - step * dx
            new_y = y - step * dy
            
        # Если шаг хороший, фиксируем точку и чуть-чуть ускоряемся (на 20%)
        if func(new_x, new_y) < func(x, y):
            x, y = new_x, new_y
            step *= 1.2 
        
        itter += 1
        
    print(table)
    print(f"Минимальный x = {x:.4f}, Минимальный y = {y:.4f}")
    return [x,y]