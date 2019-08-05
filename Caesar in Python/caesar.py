from cs50 import get_string
from sys import argv


if len(argv) != 2:
    exit("Format: python caesar.py n")

key=int(argv[1])

plain=get_string("plaintext: ")

print("ciphertext:", end="")
for x in plain:
    if x.islower() and (ord(x) + (key % 26) > 122):
        x=chr(ord(x) - (26 - (key % 26)))
        print(f"{x}", end="")
    elif x.islower() and (ord(x) + (key % 26) < 122):
        x=chr(ord(x) + (key % 26))
        print (f"{x}", end="")
    elif  x.isupper() and (ord(x) + (key % 26) > 90):
        x=chr(ord(x) - (26 - (key % 26)))
        print(f"{x}", end="")
    elif  x.isupper() and (ord(x) + (key % 26) < 90):
        x=chr(ord(x) + (key % 26))
        print(f"{x}", end="")
    else:
        print(f"{x}", end="")
print()