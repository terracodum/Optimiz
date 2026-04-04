import math
from prettytable import PrettyTable
from typing import Callable

def hook(func: Callable, eps: float) -> list:
    print("\nМетод Хука и Дживса")
    table = PrettyTable()
    table.field_names = ["iter_num", "x", "y", "step", "f()", "type"]

    x, y = 0.0, 0.0
    step = 0.5
    itter = 0

    def explore(cx, cy, h):
        bx, by = cx, cy
        # Проверка по X
        if func(cx + h, cy) < func(bx, by):
            bx = cx + h
        elif func(cx - h, cy) < func(bx, by):
            bx = cx - h

        # Проверка по Y (относительно нового bx)
        if func(bx, cy + h) < func(bx, by):
            by = cy + h
        elif func(bx, cy - h) < func(bx, by):
            by = cy - h
        return bx, by
    
    table.add_row([f"{itter}", f"{x:.4f}", f"{y:.4f}", f"{step:.4f}", f"{func(x, y):.4f}", "Start"])

    while step > eps:
        itter += 1
        x_old, y_old = x, y
        
        x_res, y_res = explore(x, y, step)

        if func(x_res, y_res) < func(x_old, y_old):
            x_pattern = x_res + (x_res - x_old)
            y_pattern = y_res + (y_res - y_old)
            
            x_after_p, y_after_p = explore(x_pattern, y_pattern, step)
            
            if func(x_after_p, y_after_p) < func(x_res, y_res):
                x, y = x_after_p, y_after_p
                move_type = "Jump+Exp"
            else:
                x, y = x_res, y_res
                move_type = "Explore"
        else:
            step /= 2
            move_type = "StepDown"
            
        table.add_row([f"{itter}", f"{x:.4f}", f"{y:.4f}", f"{step:.4f}", f"{func(x, y):.4f}", move_type])
        
        if itter > 500: break

    print(table)
    print(f"Минимальный x = {x}, Минимальный y = {y}")
    return [x, y]
