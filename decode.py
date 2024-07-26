from cryptography.fernet import Fernet
import base64
import string

def decrypter():
    # import the encoded credentials
    f_in = open("creds.enc", "rb")
    creds = f_in.read()
    f_in.close()
    print(creds)
    
    # import the key
    f_in = open("key.txt", "rb")
    key = f_in.read()
    f_in.close()
    print(key)
    key = base64.b64encode(key)
    print(key)

    # create the encoder and decrypt
    encoder = Fernet(key)
    decrypted_creds = encoder.decrypt(creds)
    print(decrypted_creds)

    return decrypted_creds
