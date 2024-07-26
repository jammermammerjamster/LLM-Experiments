import json
from cryptography.fernet import Fernet
import base64 
  
#sample_string_bytes = sample_string.encode("ascii") 
  
#base64_bytes = base64.b64encode(sample_string_bytes) 
#base64_string = base64_bytes.decode("ascii") 

# read in key
f_in = open("key.txt", "rb")
key = f_in.read()
f_in.close()
print(key)
key = base64.b64encode(key)

# read in credential to be encrypted
f_in = open("creds.txt", "rb")
creds = f_in.read()
f_in.close()
print(creds)

# create the encoder and encrypt the key
encoder = Fernet(key)
encrypted_creds = encoder.encrypt(creds)
print(encrypted_creds)

# write the encrypted key to a file
with open("creds.enc", "wb") as f:
    f.write(encrypted_creds)
