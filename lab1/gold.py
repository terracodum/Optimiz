## Метод золотого сечения

import math


def goldenRatioMethod(func: function, a: float, b:float, eps: float, iter_count: int, max=False) -> float:

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
        midx = (x_1 + x_2)/2
        return[midx, func(midx), iter_count]
    if (f1 < f2):
        return goldenRatioMethod(func, a, x_2, eps, iter_count + 1)
    
    if (f1 > f2):
        return goldenRatioMethod(func, x_1, b, eps, iter_count + 1)