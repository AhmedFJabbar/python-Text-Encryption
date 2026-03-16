from random import randint
from ProjectFunctions import *

print('"welcom to my program"\n')
print("you could Encrypt any text or Decrypt any text you have take it from here :\n")

while True :
     print("\nyou here to Encrypt or Decrypt  a text ?\n")
     
     choce = int(input("\nPress 1 to Encrypt or Press 2 to Decrypt : "))
     
     
     if  choce == 1 :
         text = input("\nplease enter the text to encrypt it : ")
         key = randint(100, 999)
         EncryptedText = TextEncryption(text, key)
         print("\nyour text after Encryption : ",EncryptedText)
         print ("\nyour Decryption key = ",key)

     elif choce == 2 :
         text = input("\nplease enter the text to decrypt it : ")
         key = int(input("\nplease enter your Decryption key : "))
         DecryptedText = TextDecryption(text, key)
         print("\nyour text after Decryption : ",DecryptedText)

     else:
         print('\nthe input should be ethir "1" or "2" : ')
    
     choce = input("\n do you want to continue 'y' for 'yes' and 'n' for 'no' : ")
     
     if choce == "n":
         print("\nwelcome any time and take care :) ")
         break
     else:
         continue

     
