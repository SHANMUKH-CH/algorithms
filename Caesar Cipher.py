def encryption(plain_text, key):
      lower=[chr(i) for i in range(ord('a'),ord('z')+1)]
      upper=[chr(i) for i in range(ord('A'),ord('Z')+1)]
      chipertxt=""
      for i in plain_text:
          #STEP-3: If the key is positive then encrypt the text by adding the key with each character in the plain text.
          #STEP-4: Else subtract the key from the plain text.
            if i in lower:chipertxt+=lower[(lower.index(i)+key)%26]
            elif i in upper:chipertxt+=upper[(upper.index(i)+key)%26]
            else:chipertxt+=i
      return chipertxt
def Encrypted_cipher_decryption(ciphertext, key):
    lower=[chr(i) for i in range(ord('a'),ord('z')+1)]
    upper=[chr(i) for i in range(ord('A'),ord('Z')+1)]
    decryptedtxt=""
    for i in ciphertext:
          if i in lower:decryptedtxt+=lower[(lower.index(i)-key)%26]
          elif i in upper:decryptedtxt+=upper[(upper.index(i)-key)%26]
          else:decryptedtxt+=i
    return decryptedtxt
if __name__=='__main__':
    #STEP-1: Read the plain text from the user.
    #STEP-2: Read the key value from the user.
    Text, key = input(), int(input())
    print('\n')
    #plain_text
    print("Plain_text_message:\n",Text)
    print('\n')
    #encryption
    ciphertext = encryption(Text,key)
    #STEP-5: Display the cipher text obtained above.
    print("Encrypted_Ctext:\n", ciphertext)
    print('\n')
    #decryption
    #STEP-6: Decrypt the message to get the plain text back
    print('Decrypted msg:\n',Encrypted_cipher_decryption(ciphertext,key))
    
    
    
