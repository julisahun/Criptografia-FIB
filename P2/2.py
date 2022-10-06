from ast import While
from cgi import print_arguments
import functools
import numpy as np
from threading import local

m = [1,1,0,0,0,1,0,1,1]
m2 = [1,0,0,0,1,0,1,1]

def suma(poly1, poly2):
    for i, val in enumerate(poly2):
        print(val, i)
        poly1[i] = (poly1[i] + val) % 2

def multX(poly):
    poly.append(0)
    val = poly.pop(0)
    if val == 1:
        suma(poly, m2)
    
    

a = [1,0,1,0,0,0,0,0]
multX(a)
print(a)
