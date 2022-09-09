cripted = ''

print(int(" "))
print(int("﻿ "))


with open('text1.txt') as f:
    lines = f.readlines()
    for line in lines:
        cripted = cripted + line
    print(cripted)

for i2 in range (100, 205):
    st = ''
    for j in range(0,20):
        if cripted[i2*j] == '\n':
            st = st + ' '
        else:
            st = st + cripted[i2*j]
    print(i2, st)
    print()
    #for i in range(1, 32):
        #number = str(i)
        #if i < 10:
            #number = '0' + str(i)
        #with open('textos/wells_' + number + '.txt') as f:
            #lines = f.readlines()
            #d = ''
            #for line in lines:
                #d = d + line
            #if st in d:
                #print(i)



