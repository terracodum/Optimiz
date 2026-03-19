from prettytable import PrettyTable

def DihotomMethod(func: callable, a: float, b: float, eps: float, iter_count: int):
    table = PrettyTable()
    table.field_names = ["iter_num", "a", "b", "length", "x_1", "x_2", "f(x_1)", "f()x_2"]
    dih(func, a, b, eps, iter_count, table)


def dih(func: callable, a: float, b: float, eps: float, iter_count: int, table: PrettyTable) -> float:
    mid = (a + b)/2
    l = b - a
    x1 = mid - eps/2
    x2 = mid + eps/2
    f1 = func(x1)
    f2 = func(x2)

    if l < (2 * eps):   
        table.add_row([f"{iter_count}", f"{a:.4f}", f"{b:.4f}", f"{l:.4f}", f"{x1:.4f}", f"{x2:.4f}", f"{f1:.4f}", f"{f2:.4f}"])
        print("Метод Дихотомии")
        midx = (x1 + x2)/2
        print(table)
        print(f"Точка минимума:{midx}\nЗначение:{func(midx)}\nИттерация:{iter_count}\n")
        return midx
    
    if (f1 > f2):
        table.add_row([f"{iter_count}", f"{a:.4f}", f"{b:.4f}", f"{l:.4f}", f"{x1:.4f}", f"{x2:.4f}", f"{f1:.4f}", f"{f2:.4f}"])
        return dih(func, x1, b, eps, iter_count+1, table)
    if (f1 < f2):
        table.add_row([f"{iter_count}", f"{a:.4f}", f"{b:.4f}", f"{l:.4f}", f"{x1:.4f}", f"{x2:.4f}", f"{f1:.4f}", f"{f2:.4f}"])
        return dih(func, a, x2, eps, iter_count+1, table)