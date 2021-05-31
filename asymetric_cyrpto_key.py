import math
import random


def is_prime(p):
    for i in range(2, math.isqrt(p)):
        if p % i == 0:
            return False
    return True


# Generate a random prime number under the given size restriction
def get_prime(size):
    while True:
        p = random.randrange(size, size*2)
        if is_prime(p):
            break
    return p


def lcm(a, b):
    return (a*b)//math.gcd(a, b)


def get_e(lambda_n):
    for e in range(2, lambda_n):
        if math.gcd(e, lambda_n) == 1:
            return e
    return False


def get_d(e, lambda_n):
    for d in range(2, lambda_n):
        if d*e % lambda_n == 1:
            return d
    return False


# Generating 2 distinct prime numbers
p = get_prime(300)
while True:
    q = get_prime(300)
    if q == p:
        continue
    else:
        break

print("Distinct prime numbers: ")
print(p, "\t", q)

# compute n = p*q
n = p*q
print("modulus, n: ", n)

# compute lambda(n)
lambda_n = lcm(p-1, q-1)
print('lambda', lambda_n)

# Getting value of e
e = get_e(lambda_n)
print('Public Exponent: ', e)

# calculate the value of d
d = get_d(e, lambda_n)
print('Secret exponent: ', d)

# key generated
print('Public Key: (e, n): ', e, n)
print('Secret Key: (d): ', d)

# Bob sending an encrypted message
message = 123
cipher = message**e % n
print('Bob sends: ', cipher)

# Alice decrypting the message
message = cipher**d % n
print('Alice receives: ', message)
