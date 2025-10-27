
alphabet = "abcdefghijklmnopqrstuvwxyz"


ciphertext = "fcwkgqrcp"

decrypted = ""
key = 1

while key <= 25:

    print(" KEY: " + str(key))   
  
    for j in ciphertext:

        index = alphabet.index(j)
        decrypted += alphabet[(index - key) % len(alphabet)]
        
    print(decrypted)
    decrypted = ""
    key += 1
   
   