import sympy

e = int(input("Exponent public: "))
n = int(input("Modul: "))

factors = list(sympy.factorint(n).keys())
phi = (factors[0]-1) * (factors[1]-1)

d = sympy.mod_inverse(e,phi)
print("Exponent privat:",d)
