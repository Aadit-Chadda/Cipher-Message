import random


def generate_key_stream(n):
    return bytes(random.randrange(0, 256) for i in range(n))


def xor_bytes(key_stream, message):
    lenght = min(len(key_stream), len(message))
    return bytes(key_stream[i] ^ message[i] for i in range(lenght))


message = input("Enter your message here: ")
message = message.encode()

key_stream = generate_key_stream(len(message))
cipher = xor_bytes(key_stream, message)

print(key_stream)
print(cipher)
print(xor_bytes(key_stream, cipher))
