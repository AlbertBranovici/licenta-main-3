from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import json, os, hashlib, base64

def generate_salt():
    return os.urandom(16)
def generate_hash(masterKey, salt):
    return hashlib.pbkdf2_hmac('sha256', masterKey, salt,100000)

def validate_masterKey(inputKey, stored_salt, stored_hash):
    new_hash = generate_hash(inputKey, stored_salt)
    return new_hash == stored_hash
def criptare(key, text):
    cipher = AES.new(key, AES.MODE_CBC)
    cipherText = cipher.encrypt(pad(text, AES.block_size))
    iv = cipher.iv
    return cipherText, iv

def decriptare(key, cipherText, iv):
    decrypt_cipher = AES.new(key, AES.MODE_CBC, iv)
    originalText = unpad(decrypt_cipher.decrypt(cipherText), AES.block_size)
    return originalText

def validate_masterKey(inputKey, stored_salt, stored_hash):
    new_hash = generate_hash(inputKey, stored_salt)
    return new_hash == stored_hash
def read_and_decrypt(file_path, masterKey):
    with open(file_path, 'r') as file:
        encrypted_data = json.load(file)

    encrypted_bytes = encrypted_data[0]
    stored_hash = base64.b64decode(encrypted_bytes[0].encode('utf-8'))
    stored_salt = base64.b64decode(encrypted_bytes[1].encode('utf-8'))

    masterKey = masterKey.encode('utf-8')

    if not validate_masterKey(masterKey, stored_salt, stored_hash):
        return None

    decrypted_data = []
    for item in encrypted_data[1:]:
        cipher_hex = item["cipherText"]
        iv_hex = item["iv"]

        cipherTextBytes = bytes.fromhex(cipher_hex)
        ivBytes = bytes.fromhex(iv_hex)

        decryptedBytes = decriptare(masterKey, cipherTextBytes, ivBytes)

        decryptedRow = decryptedBytes.decode('utf-8').split('||')

        decrypted_data.append(decryptedRow)
    return decrypted_data

def encrypt_and_save(data,masterKey,file_path):

    masterKey = masterKey.encode("utf-8")
    salt = generate_salt()
    hash = generate_hash(masterKey,salt)
    storedHash = [hash,salt]
    encoded_list = [base64.b64encode(data).decode('utf-8') for data in storedHash]

    encryptedData = []
    encryptedData.append(encoded_list)
    print("data : ", data)

    for list in data:
        print("list: ", list)
        row_str = '||'.join(list)
        encryptedRow, iv = criptare(masterKey, row_str.encode('utf-8'))
        encryptedData.append({
            "cipherText": encryptedRow.hex(),
            "iv": iv.hex()
        })
        print(row_str)
    with open(file_path, "w") as file:
        json.dump(encryptedData, file)




#     de completat cu functie de hasing pt a asigura lungimea de 16 bytes pentru cryptare--------