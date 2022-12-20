import math

p = int(input("p: "))

l = p + 1 - 2*math.sqrt(p)
d = p + 1 + 2*math.sqrt(p)

print(l,"<= orden >=",d)
