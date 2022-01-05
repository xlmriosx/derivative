import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import math
from math import *
import sympy as sp

def derivada(expr):
    x = sp.Symbol('x')
    funcion = sp.Derivative(expr,  evaluate=True)
    print(f'La derivada de f(x) es:     {funcion}')

if __name__ == '__main__':
    print('\n la ecuacion debe estar en funcion de (x)')
    expr = input("Funcion a evaluar:    f(x)=")
    derivada(expr)