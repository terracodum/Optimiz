from gold import GRM
from fibon import FibonaciMethod 
from dih import DihotomMethod
import math

print("Вариант 1\nf(x) = sin(x) на отрезке [ -pi ; pi/2 ]\n")

def func(x):
    return (x-2) ** 2
GRM(func, 0, 3, 0.01, 0)
DihotomMethod(func, 0, 3, 0.01, 0)
FibonaciMethod(func, 0, 3, 0.01, 0)