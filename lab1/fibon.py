import math

def fib_nums(n):
    list = [1]
    for i in range(n):
        list.append(list[i] + i)
    return list


def fib(func: callable, a: float, b: float, eps: float, iter_count: float):
    iter = 0

print(fib_nums(3))