from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
# private key
# 128 bits or 16 bytes
# key = b'mysecretpassword' #are 16 caractere = 16 bytes
# generare key random
# key2 = get_random_bytes(16)

# cipher = AES.new(key, AES.MODE_CBC)
# ask for a password and then use a SHa (hasking) 16 bytes -> private key must be 16 bytes
# plaintext = b'This is a message'
# print(pad(plaintext, AES.block_size))

# cipherText = cipher.encrypt(pad(plaintext,AES.block_size))
# iv = cipher.iv
# print(cipherText)
#
# decrypt_cipher = AES.new(key, AES.MODE_CBC, iv)
# originalText = unpad(decrypt_cipher.decrypt(cipherText), AES.block_size)
#
# print(originalText.decode())


def criptare(key, text):
    cipher = AES.new(key, AES.MODE_CBC)
    cipherText = cipher.encrypt(pad(text, AES.block_size))
    iv = cipher.iv
    return cipherText, iv

def decriptare(key, cipherText, iv):
    decrypt_cipher = AES.new(key, AES.MODE_CBC, iv)
    originalText = unpad(decrypt_cipher.decrypt(cipherText), AES.block_size)
    return originalText

key = b'mysecretpassowrd'  # Make sure this is 16, 24, or 32 bytes long
l = [b'maicata', b'maicata']
ciphers = []
deciphers = []
ivs = []  # Store IVs for each encrypted item

for item in l:
    cipherText, iv = criptare(key, item)
    ciphers.append(cipherText)
    ivs.append(iv)  # Save the IV for later

print(ciphers)

for cipherText, iv in zip(ciphers, ivs):  # Use the corresponding IV for each cipherText
    originalText = decriptare(key, cipherText, iv)
    deciphers.append(originalText)

print(deciphers)




