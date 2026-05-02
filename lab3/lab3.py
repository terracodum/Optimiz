import math
from rozen import rozen
from lagran import lagrange
from zoidec import zoutendijk

def f(x, y):
    return math.pow(x, 2) + math.pow(y, 2)

def phi(x, y):
    return 2 * x - y - 2

eps = 0.1

rozen(f, phi, eps)
lagrange(f, phi, eps)
zoutendijk(f, phi, eps)
