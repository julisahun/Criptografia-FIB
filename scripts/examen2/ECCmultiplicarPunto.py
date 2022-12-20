import tinyec.ec as ec

x = int(input("Coordenada x del punto: "))
y = int(input("Coordenada y del punto: "))
p = int(input("Zp: "))
a = int(input("a: "))
b = int(input("b: "))
orden = int(input("orden: "))
mult = int(input("multiplicar por: "))

field = ec.SubGroup(p, (x, y), orden, 1)
curve = ec.Curve(a, b, field)

p = ec.Point(curve,x,y)
result = mult*p

print("Resultat: (",result.x,",",result.y,")")
