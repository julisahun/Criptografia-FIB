from doctest import master
from pydoc import plain
from Crypto.Cipher import AES
import functools
import filetype
import hashlib
from IPython.display import HTML
from base64 import b64encode

name = "juli"

ciphertext = open("./files/" + name + "/AES_juli.sahun_2022_09_29_11_10_34.enc", "rb").read()

key = open("./files/" + name + "/AES_juli.sahun_2022_09_29_11_10_34.key", "rb").read()

iv = open("./files/" + name + "/AES_juli.sahun_2022_09_29_11_10_34.iv", "rb").read()

cipher = AES.new(key, AES.MODE_CBC, iv)
pt = cipher.decrypt(ciphertext)
print(filetype.guess(pt))


# b


def toBinary(list):
    ret = bytearray()
    for i in list:
      ret = ret + chr(i).encode('utf-8')
    return bytes(ret)

def pad(key):
    ret = bytearray(key)
    p = 16 - len(ret) or 16
    for i in range(p):
        ret.append(p)
    return bytes(ret)

name = "juli"
ciphertext = open("./files/" + name + "/AES_juli.sahun_2022_09_20_16_59_27.puerta_trasera.enc", "rb").read()
files = {}
for i in range(96, 97):
    print(i)
    for j in range(256):
        a = toBinary([i,i,i,i,i,i,i,i,j,j,j,j,j,j,j,j])
        h = hashlib.sha256(a).digest()
        finalKey = h[:16]

        iv = h[16:]

        cipher = AES.new(finalKey, AES.MODE_CBC, iv)
        pt = cipher.decrypt(ciphertext)
        t = str(filetype.guess(pt))
        if t != 'None':
            print(t)
            if t not in files:
                files[t] = []
            files[t].append(pt)

video = None
for key in files.keys():
  if 'Mp4' in key:
    video = files[key][0]
data_url = "data:video/mp4;base64," + b64encode(video).decode()
HTML("""
<video width=400 controls>
      <source src="%s" type="video/mp4">
</video>
""" % data_url)                                   
            



