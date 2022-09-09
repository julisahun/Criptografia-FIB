cripted = []


with open('text1.txt') as f:
    lines = f.readlines()
    for line in lines:
        cripted = cripted + [int(s) for s in line if s.isdigit()]

for i in range(1, 32):
    number = str(i)
    if i < 10:
        number = '0' + str(i)
    with open('textos/wells_' + number + '.txt') as f:
        lines = f.readlines()
        d = []
        for line in lines:
            d = d + [int(s) for s in line if s.isdigit()]
        if d == cripted:
            print(i)
