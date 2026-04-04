import math
from typing import Callable
from prettytable import PrettyTable

def fib_nums(l: float, eps: float) -> list:
    fn = l / eps
    fibList = [1, 1]
    isNotNeedNumber = True  
    itter = 1
    while isNotNeedNumber: 
        itter += 1
        fibList.append(fibList[-1]+ fibList[-2])
        if fibList[-1] > fn:
            isNotNeedNumber = False

    return [itter, fibList]        

def FibonaciMethod(func: Callable, a: float, b: float, eps: float, iter_count: int):
    table = PrettyTable()
    table.field_names = ["iter_num", "a", "b", "length", "x_1", "x_2", "f(x_1)", "f(x_2)"]
    
    n_needed, fib_list = fib_nums(b - a, eps)
    n = max(iter_count, n_needed)

    while len(fib_list) - 1 < n:
        fib_list.append(fib_list[-1] + fib_list[-2])

    print("Метод Фибоначчи")
    fib(func, a, b, eps, n, 1, fib_list, table)

def fib(func: Callable, a: float, b: float, eps: float, n: int, k: int, fib_list: list, table: PrettyTable) -> None:

    length = b - a
    
    idx = n - k + 1          # = n-k+1, соответствует F_{n-k+1}
    x1 = a + (fib_list[n - k - 1] / fib_list[idx]) * length
    x2 = a + (fib_list[n - k]     / fib_list[idx]) * length
    f1 = func(x1)
    f2 = func(x2)
    
    # Добавляем строку в таблицу
    table.add_row([f"{k}", f"{a:.6f}", f"{b:.6f}", f"{length:.6f}",
                   f"{x1:.6f}", f"{x2:.6f}", f"{f1:.6f}", f"{f2:.6f}"])
    
    # Условие остановки: если остался последний шаг (k == n-1)
    if k == n - 1:
        # Финальное сужение с использованием eps
        if f1 < f2:
            b = x2
        else:
            a = x1
        x_opt = (a + b) / 2
        f_opt = func(x_opt)

        print(table)
        print(f"Точка минимума: {x_opt:.6f}\nЗначение: {f_opt:.6f}\nИтераций: {n}\n")
        return
    
    # Рекурсивный шаг: сужаем отрезок
    if f1 < f2:
        # Минимум левее, отбрасываем правую часть
        fib(func, a, x2, eps, n, k + 1, fib_list, table)
    elif f1 > f2:
        # Минимум правее, отбрасываем левую часть
        fib(func, x1, b, eps, n, k + 1, fib_list, table)
    else:
        # f1 == f2 – можно отбросить оба крайних интервала
        fib(func, x1, x2, eps, n, k + 1, fib_list, table)