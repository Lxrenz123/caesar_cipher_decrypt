
alphabet = "abcdefghijklmnopqrstuvwxyz"


ciphertext = "wpjvJAM{jhlzhy_k3jy9wa3k_86kl32k2}"

decrypted = ""
key = 1

while key <= 25:

    print(" KEY: " + str(key))   
  
    for j in ciphertext:
        if j.isalpha():

            a = alphabet.upper() if j.isupper() else alphabet.lower()
            
            index = a.index(j)
       
            decrypted += a[(index - key) % len(a)]

        else:
            
            decrypted += j
            
            
    print(decrypted)
    decrypted = ""
    key += 1
   
   