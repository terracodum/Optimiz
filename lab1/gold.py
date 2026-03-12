## Метод золотого сечения

import math
from prettytable import PrettyTable


def GRM(func: function, a: float, b:float, eps: float, iter_count: int, max=False) -> float:
    table = PrettyTable()
    table.field_names = ["iter_num", "a", "b", "length", "x_1", "x_2", "f(x_1)", "f()x_2"]
    goldenRatioMethod(func, a, b, eps, iter_count, table)

def goldenRatioMethod(func: function, a: float, b:float, eps: float, iter_count: int, table: PrettyTable, max=False) -> float:

    if (max == True):
        tau = ((math.sqrt(5) - 1)/2)
    else:
        tau = 1-((math.sqrt(5) - 1)/2)
    l = b - a 
    x_1 = a + l * tau
    x_2 = b - l * tau
    f1 = func(x_1)
    f2 = func(x_2)

    if (l < eps):
        table.add_row([f"{iter_count}", f"{a:.4f}", f"{b:.4f}", f"{l:.4f}", f"{x_1:.4f}", f"{x_2:.4f}", f"{f1:.4f}", f"{f2:.4f}"])
        print("Метод Золотого Сечения")
        midx = (x_1 + x_2)/2
        print(table)
        print(f"Точка минимума:{midx}\nЗначение:{func(midx)}\nИттерация:{iter_count}\n")
        return[midx, func(midx), iter_count]
    if (f1 < f2):
        table.add_row([f"{iter_count}", f"{a:.4f}", f"{b:.4f}", f"{l:.4f}", f"{x_1:.4f}", f"{x_2:.4f}", f"{f1:.4f}", f"{f2:.4f}"])
        return goldenRatioMethod(func, a, x_2, eps, iter_count + 1, table)
    
    if (f1 > f2):
        table.add_row([f"{iter_count}", f"{a:.4f}", f"{b:.4f}", f"{l:.4f}", f"{x_1:.4f}", f"{x_2:.4f}", f"{f1:.4f}", f"{f2:.4f}"])
        return goldenRatioMethod(func, x_1, b, eps, iter_count + 1, table)