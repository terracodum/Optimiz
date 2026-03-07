import math

def dih(func: callable, a: float, b: float, eps: float, iter_count: int) -> float:
    mid = (a + b)/2
    x1 = mid - eps/2
    x2 = mid + eps/2
    f1 = func(x1)
    f2 = func(x2)

    if b - a < 2 * eps:
        return (mid, func(mid), iter_count)
    
    if (f1 > f2):
        return dih(func, x1, b, eps, iter_count+1)
    else:
        return dih(func, a, x2, eps, iter_count+1)

sin = math.sin
def x_sq(x): return (x-2)**2 
print(dih(math.sin, -math.pi, math.pi/2, 0.01, 0))
print(dih(x_sq, 0, 3, 0.01, 0))