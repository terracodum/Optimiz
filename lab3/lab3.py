import math
from rozen import rozen
from lagran import lagrange
from zoidec import zoutendijk

def phi(x, y):
    return 2 * x - y - 2

eps = 0.1

# Вариант 1а — минимизация f = x² + y²
# Точное решение: x* = 0.8, y* = -0.4, f* = 0.8
def f_min(x, y):
    return math.pow(x, 2) + math.pow(y, 2)

print("=" * 55)
print("МИНИМИЗАЦИЯ: f(x,y) = x² + y²")
print("=" * 55)
rozen(f_min, phi, eps, maximize=False)
lagrange(f_min, phi, eps, maximize=False)
zoutendijk(f_min, phi, eps, maximize=False)

# Вариант 1б — максимизация f = x² − y²
# Точное решение: x* = 4/3 ≈ 1.333, y* = 2/3 ≈ 0.667, f* = 4/3 ≈ 1.333
def f_max(x, y):
    return math.pow(x, 2) - math.pow(y, 2)

print("\n" + "=" * 55)
print("МАКСИМИЗАЦИЯ: f(x,y) = x² − y²")
print("=" * 55)
rozen(f_max, phi, eps, maximize=True)
lagrange(f_max, phi, eps, maximize=True)
zoutendijk(f_max, phi, eps, maximize=True)
