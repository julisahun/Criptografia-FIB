from queue import PriorityQueue
d = {}

with open('text.txt') as f:
    lines = f.readlines()
    i = 0
    terna = ''
    for char in lines[0]:
        if i == 3:
            d[terna] = d.get(terna, 0) + 1
            terna = ''
            i = 0
        terna += char
        i += 1

most_common = PriorityQueue()

for terna in d:
    most_common.put((d[terna], terna))
    if most_common.qsize() > 10:
        most_common.get()

while not most_common.empty():
    print(most_common.get())
