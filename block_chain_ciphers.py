from pyDes import *

message = input("Enter message here: ")
key = "DESCRYPT"
iv = bytes([0]*8)
k = des(key, ECB, iv, pad=None, padmode=PAD_PKCS5)

print()
cipher = k.encrypt(message)
print("cipher: ", cipher)
print("length of cipher: ", len(cipher))
print("encrypted: ", cipher[0:8])
print("encrypted: ", cipher[8:16])
print("encrypted: ", cipher[16:])
print()
message = k.decrypt(cipher)
print("message: ", message)
