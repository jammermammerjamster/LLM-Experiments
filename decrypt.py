#!/usr/bin/env python3
from cryptography.fernet import Fernet
import base64
import sys 
import os
sys.path.append(os.path.abspath("/home/jamster/Repos/LLM-Experiments/"))

def decrypter():
    # import the encoded credentials
    f_in = open("creds.enc", "rb")
    creds = f_in.read()
    f_in.close()
    
    # import the key
    f_in = open("key.txt", "rb")
    key = f_in.read()
    f_in.close()
    key = base64.b64encode(key)

    # create the encoder and decrypt
    encoder = Fernet(key)
    decrypted_creds = encoder.decrypt(creds)

    return decrypted_creds.decode("utf8")

if __name__ == "__main__":
    print("decrypted")
    print(decrypter)
