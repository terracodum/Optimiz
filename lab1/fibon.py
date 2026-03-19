import math
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

def FibonaciMethod(func: function,
    a: float, 
    b:float, 
    eps: float, 
    iter_count: int
    ) -> list:

    table = PrettyTable()
    table.field_names = ["iter_num", "a", "b", "length", "x_1", "x_2", "f(x_1)", "f()x_2"]
    fib(func, a, b, eps, iter_count, table)

def fib(func: callable, a: float, b: float, eps: float, iter_count: float, table: PrettyTable):
    return None