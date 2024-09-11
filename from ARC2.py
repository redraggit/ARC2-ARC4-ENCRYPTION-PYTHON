from Crypto.Cipher import ARC2 
from Crypto import Random
import base64


def Encrypt(msg):
    padding ="$"
    p = lambda s:s + (block_size - len(s) % block_size) * padding
    block_size = ARC2.block_size
    iv = Random.new().read(block_size)
    key = Random.new().read(16)
    e = ARC2.new(key, ARC2.MODE_CBC, iv)
    Encrypted_message = e.encrypt(p(msg).encode('ascii'))
    data = [key, base64.b64encode(iv + Encrypted_message)]
    return data


def Decrypt(key, Encrypted_message):
    iv = base64.b64decode(Encrypted_message)[:8]
    Encrypted_message = base64.b64decode(Encrypted_message)[8:]
    d = ARC2.new(key, ARC2.MODE_CBC, iv)
    plain_text = d.decrypt(Encrypted_message)
    plain_text = plain_text.decode('ascii')
    return plain_text

e = Encrypt('hy algeria')
d = Decrypt (e[0], e[1])
print(e)
print(d)