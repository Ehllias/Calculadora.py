import math
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Erro: divisão por zero não é permitida."
        else:
            return a / b

    def sqrt(self, a):
        if a < 0:
            return "Erro: raiz quadrada de números negativos não é permitida."
        else:
            return math.sqrt(a)

calculator = Calculator()

print("Adição:")
print(calculator.add(1, 2))

print("\nSubtração:")
print(calculator.subtract(10, 5))

print("\nMultiplicação:")
print(calculator.multiply(10, 5))

print("\nDivisão:")
print(calculator.divide(10, 2))

print("\nRaiz quadrada:")
print(calculator.sqrt(4))
print(calculator.sqrt(9))

import sympy as sp

def integral_calculator(f, x, a, b):
    return sp.integrate(f, (x, a, b))

def derivative_calculator(f, x):
    return sp.diff(f, x)

def power_calculator(base, exponent):
    return base ** exponent

def square_root_calculator(number):
    return sp.sqrt(number)

def quadratic_equation_solver(a, b, c):
    return sp.solve(a*sp.Symbol('x')**2 + b*sp.Symbol('x') + c, sp.Symbol('x'))

print("Integral:", integral_calculator(sp.Symbol('x')**2, sp.Symbol('x'), 0, 1))
print("Derivative:", derivative_calculator(sp.Symbol('x')**3, sp.Symbol('x')))
print("Power:", power_calculator(2, 3))
print("Square Root:", square_root_calculator(4))
print("Quadratic Equation Solutions:", quadratic_equation_solver(1, -3, 2))