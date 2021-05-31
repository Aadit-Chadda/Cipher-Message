def generate_key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXVZ"
    key = {}
    count = 0
    for c in letters:
        key[c] = letters[(count+n) % len(letters)]
        count += 1
    return key


def encrypt(key, message):
    cipher = ""
    for c in message:
        if c in key:
            cipher += key[c]
        else:
            cipher += c
    return cipher


key = generate_key(26+3)
print(key)

message = input("Enter your message: ").upper()
cipher = encrypt(key, message)
print(cipher)

print("*"*50)
# Decrypting the cipher
print("*"*50)


def decrypt(key):
    de_key = {}
    for c in key:
        de_key[key[c]] = c
    return de_key


de_key = decrypt(key)
message = encrypt(de_key, cipher)
print(message)
