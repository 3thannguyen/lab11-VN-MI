# https://github.com/3thannguyen/lab11-VN-MI
# Partner 1: Ethan Nguyen
# Partner 2: Mahir Isic

import math 
def square_root(a):
    if a < 0:
        raise ValueError()
    try:
        return math.sqrt(a)
    except: print("Something is wrong.")
        
def hypotenuse(a, b):
    try:        
        return math.hypot(a, b)
    except: print("I'm not sure what happened.")

def add(a, b): 
    return a + b

def subtract(a, b): return a - b

def mul(a, b): return a * b

def logarithm(a, b):
    if b <= 0:
        raise ValueError("A logarithm cannot be negative or zero.")
    return math.log(b, a)

def exp(a, b):
    return a ** b

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b / a

def log(a, b):
    if b <= 0:
        raise ValueError
    return math.log(a, b)

def exp(a, b):
    return a ** b

