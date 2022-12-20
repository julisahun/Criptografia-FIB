p = int(input("p: "))
g = int(input("g: "))
a = int(input("a: "))
b = int(input("b: "))

alfa = (g**a) % p
beta = (g**b) % p

A = (beta**a) % p
B = (alfa**b) % p

print("A genera alfa y la envia a B:", alfa)
print("B genera beta y la envia a A:", beta)
print("Clave secreta de A:",A)
print("Clave secreta de B:",B)
