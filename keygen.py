import string
import random
 
# initializing size of string
N = 16
 
# using random.choices()
# generating random strings
res = ''.join(random.choices(string.printable.strip(' \t\n\r\x0b\x0c'), k=N))

with open('key.txt', 'wb') as f:
    f.write(res.encode("utf8"))
