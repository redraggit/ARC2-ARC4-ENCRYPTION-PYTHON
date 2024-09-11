from Crypto.Cipher import ARC4
from Crypto.Hash import SHA
from Crypto import Random
import base64

def Encrypt(msg):
    key = Random.new().read(16)
    iv = Random.new().read(16)
    tempkey = SHA.new(iv+key).digest()
    c = ARC4.new(tempkey)
    data = [tempkey, base64.b64encode(c.encrypt(msg.encode('ascii')))]
    return data

def Decrypt(tempkey, encrypted_message):
    d = ARC4.new(tempkey)
    return d.decrypt(base64.b64decode(encrypted_message))
c = Encrypt('HELLO YPUR FILES ARE ENCRYPTED') 
d = Decrypt (c[0], c[1])
print(c)
print(d)
