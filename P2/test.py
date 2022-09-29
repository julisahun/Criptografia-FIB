from pydoc import plain
from Crypto.Cipher import AES
import json
import base64
import sys
import functools
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import chardet

def addPadding(s):
    remaining = 16 - len(s) % 16
    byte = remaining.to_bytes(1,'big')
    while remaining > 0:
        s += byte
        remaining -= 1
    return s

ciphertext = open('./files/AES_juli.sahun_2022_09_20_16_59_27.enc', "rb").read()
ciphertext = pad(ciphertext, AES.block_size)
# ciphertext = b'\xd2\x12\xf9"_\xbd8\xb4Z:\xca$\xa1\x14V\x13'

key = open("./files/AES_juli.sahun_2022_09_20_16_59_27.key", "rb").read()
# key = b'\x83\x83\xafj\x0b\xf1\x07\xbd?\x8b\x9dTE\x8b\xf9\x81'

iv = open("./files/AES_juli.sahun_2022_09_20_16_59_27.iv", "rb").read()
iv = pad(iv, AES.block_size)
# iv = b'U\x82\xc4\x9f4\xd2\x08-L\x04\tZ\xb3K\x85l'

cipher = AES.new(key, AES.MODE_CBC, iv)
pt = cipher.decrypt(ciphertext)

# try:
print("The message is authentic:",pt)
# except ValueError:

#     print("Key incorrect or message corrupted")

# data = b"secret"
# key = get_random_bytes(16)
# cipher = AES.new(key, AES.MODE_CBC)
# ct_bytes = cipher.encrypt(pad(data, AES.block_size))
# iv = base64.b64encode(cipher.iv).decode('utf-8')
# ct = base64.b64encode(ct_bytes).decode('utf-8')
# # result = json.dumps({'iv':cipher.iv, 'ciphertext':ct_bytes})
# print(cipher.iv, ct_bytes, key)
# '{"iv": "bWRHdzkzVDFJbWNBY0EwSmQ1UXFuQT09", "ciphertext": "VDdxQVo3TFFCbXIzcGpYa1lJbFFZQT09"}'
