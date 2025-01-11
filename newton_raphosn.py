import numpy as np
import math


def func(x):
    return x-10**(1/3)

def dfunc(x):
    return 1

def error_cnt(x_1, x_2):
    return abs(100.0*(x_1-x_2)/x_2)

def nraphson(ini, err):
    e1=0
    e2 = ini
    e = 100
    i=0
    while(e>err):
        i+=1
        print(f"{i}      {round(e2,6)}        {round(e,6)}")

        e1 = e2
        e2 = e2 - (func(e2)/dfunc(e2))
        e = error_cnt(e1,e2)
    i+=1
    print(f"{i}      {round(e2,6)}        {round(e,6)}")

    return e2

r = nraphson(3,.00000000000001)
print('\n\n')
print(r)
print('y=',func(r))