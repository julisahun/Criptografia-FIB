text = open('text.txt').read()
chars = {}
i = 0
while len(chars) < 26:
    if ord(text[i]) < 1000 or text[i] == '\ufeff':
        i += 1
        continue
    chars[text[i]] = ord(text[i])
    i += 1
alphabet = 'abcdefghijklmnopqrstuvwxyz'
i = 0
translator = {}
chars = dict(sorted(chars.items(), key=lambda item: item[1]))

for entry in chars.keys():
    translator[entry] = alphabet[i]
    i += 1

for i in range(26):
    plain = ''
    for c in range(20):
        if ord(text[c]) < 1000 or text[c] == '\ufeff':
            plain += text[c]
            continue
        plain += alphabet[(alphabet.index(translator[text[c]]) + i) % 26]
    print(plain)