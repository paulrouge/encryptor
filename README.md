# A scrypt to encrypte files.



### Version Control
To keep the version control of the cryptography library correct use pipenv and run "pipenv install pipfile"
_Version control is important! In case for some reason in the future the encryption alogrythm of the cryptpgraphy library gets changed._



### Generate encryption key
To generate the encryption key run generate_key function. This generates OR OVERWRITES (if there is a file with that name already) the filekey.key file. You can name this file key different, just make sure it's a '.key' file.



### Encrypt a file
To ENCRYPT a file run the encrypt function. Change the filename in the file you want to encrypt. Change the OUTPUT file name if you want.



### Decrypt a file
To DECRYPT a file run the decrypt function. Change the filename in the file you want to decrypt. Change the OUTPUT file name if you want.



### remarks
*You (or anyone) can only decrypt an encrypted file with the key used to encrypt that file. If you loose your key you can never decrypt the file, or if some else has the key and the encrypted file he/she can encrypt the file. So don't loose your key and do not store your key at the same place as the encrypted file!*



