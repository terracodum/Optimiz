import math
from prettytable import PrettyTable

def func(x, y):
    A = 20
    a = 1
    b = 2
    return A - (x-a) * math.pow(math.e, -(x-a)) - (y-b) * math.pow(math.e, -(y-b))
step = 0.1 
eps = 0.0001 
def gauss(func, eps):
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

        if func(x + step, y) < func(x, y):
            x += step
        elif func(x - step, y) < func(x, y):
            x -= step

        if func(x, y + step) < func(x, y):
            y += step
        elif func(x, y - step) < func(x, y):
            y -= step

        dist = math.sqrt((x - x_old) ** 2 + (y - y_old) ** 2)
        if dist == 0:
            step /= 2
            dist = 100 # Чтобы не выйти из цикла, пока шаг велик
            if step < eps: # Предохранитель
                break

        table.add_row([f"{itter}", f"{x:.4f}", f"{y:.4f}", f"{step:.4f}", f"{dist:.4f}", f"{func(x, y):.4f}"])\
        
    print(table)
    return f"Минимальный x = {x}, Минимальный y = {y}"

print(gauss(func, 0.01))