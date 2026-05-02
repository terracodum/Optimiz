import numpy as np
from prettytable import PrettyTable
from barrier import barrier_method
from penalty import penalty_method

# Вариант 1
# f(x) = x1² + x2² + 4x2 - 1
# g1: x1² + x2  <= 0  →  -x1² - x2  >= 0
# g2: x1 - 2x2  <= 8  →  -x1 + 2x2 + 8 >= 0
# Старт: (0.5, -1.5), eps = 0.05

def f(x):
    return x[0]**2 + x[1]**2 + 4*x[1] - 1

def g1(x): return -x[0]**2 - x[1]
def g2(x): return -x[0] + 2*x[1] + 8

constraints = [g1, g2]
x0 = [0.5, -1.5]
eps = 0.05

# Точное решение: grad f = 0 → x1=0, x2=-2, оба ограничения выполнены
x_exact = [0.0, -2.0]
f_exact = f(x_exact)

print("Точное решение (безусловный минимум лежит внутри допустимой области):")
print(f"  x1* = {x_exact[0]},  x2* = {x_exact[1]},  f* = {f_exact}")
print(f"  g1(x*) = {g1(x_exact):.4f} >= 0 ✓")
print(f"  g2(x*) = {g2(x_exact):.4f} >= 0 ✓")

x_bar = barrier_method(f, constraints, x0, eps)
x_pen = penalty_method(f, constraints, x0, eps)

print("\n" + "=" * 52)
print("Сравнение результатов")
print("=" * 52)
t = PrettyTable()
t.field_names = ["Метод", "x1*", "x2*", "f*", "|Δf|"]
t.add_row(["Точное",    "0.0000",          "-2.0000",          f"{f_exact:.4f}", "—"])
t.add_row(["Барьерный", f"{x_bar[0]:.4f}", f"{x_bar[1]:.4f}", f"{f(x_bar):.4f}", f"{abs(f(x_bar)-f_exact):.4f}"])
t.add_row(["Штрафной",  f"{x_pen[0]:.4f}", f"{x_pen[1]:.4f}", f"{f(x_pen):.4f}", f"{abs(f(x_pen)-f_exact):.4f}"])
print(t)
