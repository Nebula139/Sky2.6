#!/usr/bin/venv python3
# -*- coding: utf-8 -*-

def decorator(func):
    def decorator1(x):
        c = "Площадь круга"
        ret = func(x)
        print(f'{c} = {ret}')
        return ret
    return decorator1


@decorator
def add(x):
    pi = 3.14
    return x * x * pi


if __name__ == "__main__":
    r = float(input("Введите значение радиуса:"))
    add(r)
