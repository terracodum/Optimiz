import math
from gauss_seidel import gauss
from steepest_descent import steep
from hooke_jeeves import hook
from rosenbrock import rosen

print("Вариант 1:\n\nf(x,y)=20-(x-1)e^-(x-1)-(y-2)e^-(y-2) \n")
print("A = 20 ; a = 1 ; b = 2")

def safe_exp(x):
    if x > 700:
        return math.exp(700) # Максимально возможное число для Python
    return math.exp(x)
eps = 0.01
def var1(x, y):
    A = 30
    a = 2
    b = 2
    c = 1
    d = 2
    r = 3
    return A - safe_exp((-1/(10-r**2))* ((((x-a)**2)/c**2) - (2*r*(x-a)*(y-b)/(c*d)) + ((y-b)**2)))

gauss(var1, eps)
steep(var1, eps)
hook(var1, eps)
rosen(var1, eps)