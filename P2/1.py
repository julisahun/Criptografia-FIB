#https://github.com/pts/chacha20/blob/master/chacha20_python3.py
import struct
import binascii

ejeY = [0] * 512

c1 = []

uh = lambda x: binascii.unhexlify(bytes(x, 'ascii'))
ciphertext = uh('76b8e0ada0f13d90405d6ae55386bd28bdd219b8a08ded1aa836efcc8b770dc7da41597c5157488d7724e03fb8d84a376a43b8f41518a11cc387b669')
iv = uh('0000000000000000')


def toBin(x):
    converted = []
    for c in x:
        binary = bin(c).replace('0b', '')
        while len(binary) < 32:
            binary = '0' + binary
        converted.append(binary)
    return converted

def compareState(x):
    global ejeY
    global c1
    binary = toBin(x)
    for i in range(16):
        for b in range(32):
            if binary[i][b] != c1[i][b]:
                ejeY[i*32+b] += 1
            

    
def yield_chacha20_xor_stream(key, iv, position=0):

  global ejeY
  
  """Generate the xor stream with the ChaCha20 cipher."""
  if not isinstance(position, int):
    raise TypeError
  if position & ~0xffffffff:
    raise ValueError('Position is not uint32.')
  if not isinstance(key, bytes):
    raise TypeError
  if not isinstance(iv, bytes):
    raise TypeError
  if len(key) != 32:
    raise ValueError
  if len(iv) != 8:
    raise ValueError

  def rotate(v, c):
    return ((v << c) & 0xffffffff) | v >> (32 - c)

  def quarter_round(x, a, b, c, d):
    x[a] = (x[a] + x[b]) & 0xffffffff
    x[d] = rotate(x[d] ^ x[a], 16)
    x[c] = (x[c] + x[d]) & 0xffffffff
    x[b] = rotate(x[b] ^ x[c], 12)
    x[a] = (x[a] + x[b]) & 0xffffffff
    x[d] = rotate(x[d] ^ x[a], 8)
    x[c] = (x[c] + x[d]) & 0xffffffff
    x[b] = rotate(x[b] ^ x[c], 7)
  global c1
  ctx = [0] * 16
  ctx[:4] = (1634760805, 857760878, 2036477234, 1797285236)
  ctx[4 : 12] = struct.unpack('<8L', key)
  ctx[12] = ctx[13] = position
  ctx[14 : 16] = struct.unpack('<LL', iv)
  while position < 4096:
    x = list(ctx)
    for i in range(10):
      quarter_round(x, 0, 4,  8, 12)
      quarter_round(x, 1, 5,  9, 13)
      quarter_round(x, 2, 6, 10, 14)
      quarter_round(x, 3, 7, 11, 15)
      quarter_round(x, 0, 5, 10, 15)
      quarter_round(x, 1, 6, 11, 12)
      quarter_round(x, 2, 7,  8, 13)
      quarter_round(x, 3, 4,  9, 14)
    if position == 0:
        c1 = toBin(x)
    else:
        compareState(x)
    ctx[12] = (ctx[12] + 1) & 0xffffffff
    if ctx[12] == 0:
      ctx[13] = (ctx[13] + 1) & 0xffffffff
    position += 1


def chacha20_encrypt(data, key, iv=None, position=0):
  """Encrypt (or decrypt) with the ChaCha20 cipher."""
  if not isinstance(data, bytes):
    raise TypeError
  if iv is None:
    iv = b'\0' * 8
  if isinstance(key, bytes):
    if not key:
      raise ValueError('Key is empty.')
    if len(key) < 32:
      key = (key * (32 // len(key) + 1))[:32]
    if len(key) > 32:
      raise ValueError('Key too long.')
  
  yield_chacha20_xor_stream(key, iv, position)


def run_tests():
    key = uh('0000000000000000000000000000000000000000000000000000000000000000')
    chacha20_encrypt(b'\0' * len(ciphertext), key, iv)

run_tests()

import matplotlib.pyplot as mpl

fig = mpl.figure()
ax = fig.add_axes([0,0,1,1])
ax.bar(range(512), ejeY)
mpl.show()
