
import random
import math


# n= p.q
#phi(n) = phi(p.q)=phi(p).phi(q) = (p-1). (q-1)
#phi(n) = (p-1.q-1)

# is_prime function check if a num is a prime  
def is_prime (number):
    if number < 2:
        return False
    for i in range (2, number // 2 +1):
        if number % i == 0:
            return False
    return True

# generate_prime function generate prime number
def generate_prime (min_value, max_value):
    prime = random.randint (min_value, max_value)
    while not is_prime(prime):
        prime = random.randint(min_value, max_value)
    return prime


def mod_inverse(e, phi):
    for d in range (3, phi):
        if (d * e) % phi == 1:
            return d 
    raise ValueError ("Mod_inverse does not exist!")


# Chouse two different prime nums p and q 
p, q = generate_prime(100, 5000), generate_prime ( 100, 5000)
while p==q:
    q= generate_prime(100, 5000)

#Calculate n = p*q module of privet and public keys
n = p * q

#Calculate oilers function phi_n = (p-1)(q-1).
phi_n = (p-1) * (q-1)

#Chouse num e: 3<3<phi_n, and e and phi)n to not have common denometer.
e = random.randint (3, phi_n-1)
while math.gcd(e, phi_n) != 1: #gcd=greater common denometer     != not equal
     e = random.randint (3, phi_n - 1)


#Calculate d: de≡1 (mod φ(n)). in which follows e*d-1 to bi dividable of (p-1)(q-1) 
d = mod_inverse(e, phi_n)

#Read ours message
message = input("Enter your message to Encrypt ")

#Info for algorythm components
print ("Prime number P: ", p)
print ("Prime number q: ", q)
print ("Public Key: ", e)
print ("Private Key: ", d)
print ("n: ", n)
print ("Phi of n: ", phi_n, " Secret")



#convert a single Unicode character into its integer representation
message_encoded = [ord(ch) for ch in message]
print ("Message in ASCII code: ", message_encoded)

# pow(x, y, z) function returns x to the power of y, modulus z ( x y % z ) 
# in our case (ord(ch) ^ e) mod n
ciphertext = [pow(ch, e, n) for ch in message_encoded]
print (message," Ciphered in: ", ciphertext)

#Decode message with d Private key
Decodemsg = [pow(ch, d, n) for ch in ciphertext] 
print ("back to ASCII: ", Decodemsg)

#back to readable text
msg = "".join (chr(ch) for ch in Decodemsg)
print("from ASCII to TEXT: ", msg)