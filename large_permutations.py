import random
abc = "abcdefghijklmnopqrstuvwxyz"


def random_key():
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_list = list(letters)
    key = {}
    for i in letters:
        key[i] = random.choice(letter_list)
        letter_list.remove(key[i])
    return key


key = random_key()
print(key)


def encryption(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher


def decryption(key):
    de_key = {}
    for i in key:
        de_key[key[i]] = i
    return de_key

message = input("Encrypt your message here: ").upper()

cipher = encryption(key, message)
print(cipher)

de_key = decryption(key)
message = encryption(de_key, cipher)
print(message)
