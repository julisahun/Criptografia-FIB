from ast import While
from cgi import print_arguments
import functools
from threading import local
m = "110001011"

def mod(a,b):
  result = restore('0')
  return restore(result)

# OK
def nextPolynomial(a):
  newPolynomial = ''
  carry = True
  for i in reversed(range(len(a))):
    if carry == True:
      if a[i] == '1':
        newPolynomial += '0'
      else:
        newPolynomial += '1'
        carry = False
    else:
      newPolynomial += a[i]
  return restore(newPolynomial[::-1])

# OK
def xor(v1,v2):
    return restore(''.join([str(ord(a) ^ ord(b)) for a,b in zip(v1, v2)]))
    
# len(a) <= 8
# OK
def restore(a):
    if len(a) > 8:
        return a[len(a)-8:]
    elif len(a) < 8:
        return ('0'*(8-len(a))) + a
    else:
        return a

# xor
# OK
def suma(a,b):
    return restore(xor(a,b))

#seems OK
def multX(a):
    a = a + '0'
    if a[0] == '1':
        a = suma(a[1:],'10001011')   
    else: 
        a = a[1:] 
    return restore(a)

#seems OK
def mult(a, b):
    res = '00000000'
    i = 7
    for val in a:
        if val == '1':
            localres = b
            for j in range(i):
                localres = multX(localres)
            res = suma(res, localres)
        i -= 1
    return restore(res)
  

def mod(a,b):
    res = '0'
    return restore(res)

# entrada:
# salida: lista de polinomios binarios irreducibles de grado 8 representados como enteros entre 256 (= 28) y 511 (= 28+1 − 1).
def irreducible_polynomials():
    result = []
    a = '10000000'
    while a != '00000000':
        b = '10000000'
        while b < a:
            if mod(a,b) == '00000000':
                result.append(a) 
            b = nextPolynomial(b)
        a = nextPolynomial(a)
    return result

# entrada: a y b elementos del cuerpo representados por enteros entre 0 y 255;
# salida: un elemento del cuerpo representado por un entero entre 0 y 255 que es el producto en el cuerpo de a y b calculado usando la definici´on en t´erminos de polinomios.
def GF_product_p(a,b):
    return None
    
# entrada: a elemento del cuerpo representado por un entero entre 0 y 255;
# salida: True si a es generador del cuerpo, False si no lo es.
def GF_es_generador(a):
    return None
    
# entrada:
# salida: dos tablas (exponencial y logaritmo), la primera tal que en la posici´on i tenga a = g i y la segunda tal que en la posici´on a tenga i tal que a = g i . (g generador del cuerpo finito representado por el menor entero entre 0 y 255.)
def GF_tables():
    return None
    
# entrada: a y b elementos del cuerpo representados por enteros entre 0 y 255;
# salida: un elemento del cuerpo representado por un entero entre 0 y 255 que es el producto en el cuerpo de a y b calculado usando las tablas exponencial y logaritmo.
def GF_product_t(a,b):
    return None

# entrada: a elemento del cuerpo representado por un entero entre 0 y 255;
# salida: 0 si a=0x00, inverso de a en el cuerpo si a6=0x00 representado por un entero entre 1 y 255.
def GF_invers(a):
    return None

irreducible_polynomials()