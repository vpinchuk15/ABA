
# import required module
from cryptography.fernet import Fernet

# key generation
key = Fernet.generate_key()

# using the generated key
fernet = Fernet(key)
  
# opening the original file to encrypt
with open('datacomFile.txt', 'rb') as file:
    original = file.read()
      
# encrypting the file
encrypted = fernet.encrypt(original)
  
# opening the file in write mode and 
# writing the encrypted data
with open('datacomFile.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)





# opening the encrypted file
with open('datacomFile.txt', 'rb') as enc_file:
    encrypted = enc_file.read()
  
# decrypting the file
decrypted = fernet.decrypt(encrypted)
  
# opening the file in write mode and
# writing the decrypted data
with open('datacomFile.txt', 'wb') as dec_file:
    dec_file.write(decrypted)