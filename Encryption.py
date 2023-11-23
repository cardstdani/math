#File Encryption
from cryptography.fernet import Fernet
import base64

inFile = open("FilePath/File.png", "rb")
data = inFile.read()
inFile.close()
print(data)

key = base64.b64encode(("a"*32).encode())
print(key)

f = Fernet(key)
encryptedBytes = f.encrypt(data)
print("Encrypted: " + str(token))

with open ("FilePath/EncryptedFile.png", 'wb') as encryptedFile:
    encryptedFile.write(encryptedBytes)

decryptedBytes = f.decrypt(encryptedBytes)
print("Decrypted: " + str(decryptedBytes))

with open ("FilePath/DecryptedFile.png", 'wb') as encryptedFile:
    encryptedFile.write(decryptedBytes)


#Text Encryption
from cryptography.fernet import Fernet
import base64

message = "Hello world!"
print(message, message.encode())

key = Fernet.generate_key()
print(key)

key = base64.b64encode(("a"*32).encode())
print(key)

token = Fernet(key).encrypt(message.encode())
print("Encrypted: " + str(token))

print("Decrypted: " + str(Fernet(key).decrypt(token)))
