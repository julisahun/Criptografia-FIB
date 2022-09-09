cripted = ''
with open('text1.txt') as f:
    lines = f.readlines()
    for line in lines:
        cripted = cripted + line

length = len(cripted)
for i2 in range (100, 200):
    st = ''
    j = 0
    k = 0
    c = 0
    while(c < 20):
        if (i2*j+k) >= length:
            j = 0
            k = k + 1
        else:
            st = st + cripted[(i2*j+k)]
            j += 1
            c += 1
    print(i2, st)
    print()



