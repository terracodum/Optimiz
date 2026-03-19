from gold import GRM
from fibon import fib 
from dih import DihotomMethod
import math

print("Вариант 1\nf(x) = sin(x) на отрезке [ -pi ; pi/2 ]\n")

GRM(math.sin, -math.pi, math.pi/2, 0.01, 0)
DihotomMethod(math.sin, -math.pi, math.pi/2, 0.01, 0)