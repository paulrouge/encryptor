from cryptography.fernet import Fernet


# To keep the version control of the cryptography library correct use pipenv and run "pipenv install pipfile"
# Important; In case for some reason in the future the encryption algoritm of the library gets changed.

# To generate the encryption key run generate_key function. This generates OR OVERWRITES (if there is a file 
# with that name already) the filekey.key file
# you can name this file key different, just make sure it's a .key file.

# To ENCRYPT a file run the encrypt function. Change the filename in the file you want to encrypt.
# and change the OUTPUT file name if you want

# To DECRYPT a file run the decrypt function. Change the filename in the file you want to decrypt.
# and change the OUTPUT file name if you want


def generate_key():
    # key generation
    key = Fernet.generate_key()
    
    # string the key in a file
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

def encrypt():

    # opening the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
    
    # using the generated key
    fernet = Fernet(key)
    
    #INPUT
    # opening the original file to encrypt
    with open('example_secret.txt', 'rb') as file:
        original = file.read()
        
    # encrypting the file
    encrypted = fernet.encrypt(original)
    
    # OUTPUT
    # opening the file in write mode and writing the encrypted data
    # if filename DOESNT already exists, file will be created, 
    # if it DOES already exists it will be overwritten
    with open('example_encrypted.txt', 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decrypt():
    # opening the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()
    
    # using the key
    fernet = Fernet(key)
    
    # INPUT
    # opening the encrypted file
    with open('example_encrypted.txt', 'rb') as enc_file:
        encrypted = enc_file.read()
    
    # decrypting the file
    decrypted = fernet.decrypt(encrypted)
    
    # OUTPUT
    # opening the file in write mode and writing the decrypted data
    # if filename DOESNT already exists, file will be created, 
    # if it DOES already exists it will be overwritten
    with open('example_decrypted.txt', 'wb') as dec_file:
        dec_file.write(decrypted)



#generate_key()
#decrypt()
#encrypt()
