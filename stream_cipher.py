import base64


class KeyStream:
    def __init__(self, key=1):
        self.next = key

    def rand(self):
        self.next = (1103515245*self.next + 12345) % 2**31
        return self.next

    def get_key_byte(self):
        return self.rand() % 256


def encrypt(key, message):
    return bytes(message[i] ^ key.get_key_byte() for i in range(len(message)))


key = KeyStream(10)
print("Your Key: ", key)
message = input("Enter message here: ")
message = message.encode()
cipher = encrypt(key, message)
cipher = base64.b64encode(cipher)
print(cipher)

key = KeyStream(10)
cipher = input("Enter cipher here: ")
cipher = cipher.encode()
cipher = base64.b64decode(cipher)
message = encrypt(key, cipher)
print(message)
