def TextEncryption(text, key):
   """ this function is used to encrypt a text with the value of the key """
   
   t = 0
   EncryptedText = ""
   for i in text:
       t = ord(i) + key
       EncryptedText+= chr(t)

   return EncryptedText


def TextDecryption(text, key):
   """ this function Decrypt a text with the value of the key """
   char = 0
   DecryptedText = ""
   for ch in text:
       char = ord(ch) - key
       DecryptedText+= chr(char)

   return DecryptedText


def Key_Encryption(key):
     """ this function userd to Encrypt the Encryption key """


     # array1 = [ '£', '€', '¥', '©', '®', '™', '¿', '¶', '§', '°' ]
     # array2 = ['9', '8', '5', '2', '1', '4', '7', '3', '0', '6' ]
     # array3 = [ '@', '%', '!', '$', '&', ':', '#', '*', '&', '_' ]
     array1 = [ '0','1','2','3','4','5','6','7','8','9' ]
     array2 = [ '@','!','#','&','%','^','_','$','(','*' ]
     array3 = [ 'ب','ض','ش','ء','ع','ف','ث','ص','ة','لا' ]

     count, first, second, third, reminder, code = 0,0,0,0,0,0

     while key :
    
        reminder = key % 10
        if count == 0:
            first = reminder

        elif count == 1:
            second = reminder

        else:
            third = reminder

        key = key / 10;
        count+=1

     first =int( array1[first])
     second = int(array2[second])
     third =int( array3[third])

     code = first + third % second;


     return code;


