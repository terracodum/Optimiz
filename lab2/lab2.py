import math

print("Вариант 1\n f(x,y)=A-(x-a)e^-(x-a)-(y-b)e^-(x-b) \n")
print("A = 20 ; a = 1 ; b = 2")
def func(x, y, A, a, b):
    return A - (x-a) * math.pow(math.e, -(x-a)) - (y-b) * math.pow(math.e, -(y-b))

print(func(2, 3, 20, 1, 2))