def encryption(plain_text, key):
    Encrypted=""
    for every_element in plain_text:
        if every_element.isupper(): #check uppercase character
            every_element_index=ord(every_element)-ord('A')
            # shift the curr char by key pos
            every_elemet_shifted=(every_element_index + key)%26+ord('A')
            every_element_aftershit=chr(every_elemet_shifted)
            Encrypted+=every_element_aftershit
        elif every_element.islower(): #check lowecase character
            every_element_index=ord(every_element)-ord('a') 
            every_elemet_shifted=(every_element_index+key)%26+ord('a')
            every_element_aftershit=chr(every_elemet_shifted)
            Encrypted+=every_element_aftershit
        elif every_element.isdigit():
            every_element_aftershit=(int(every_element)+key)%10 #if the element is a number, its shifts the digits
            Encrypted+=str(every_element_aftershit)
        else:
            Encrypted += every_element #special characters
    return Encrypted
def Encrypted_cipher_decryption(ciphertext, key):
    Decrypted = ""
    for every_element in ciphertext:
        if every_element.isupper(): 
            ever_element_index=ord(every_element) - ord('A')
            # shift the current character to left by key positions to get its original position
            every_element_original_pos=(ever_element_index - key) % 26 + ord('A')
            every_element_original=chr(every_element_original_pos)
            Decrypted+=every_element_original
        elif every_element.islower(): 
            ever_element_index=ord(every_element)-ord('a') 
            every_element_original_pos=(ever_element_index - key) % 26 + ord('a')
            every_element_original=chr(every_element_original_pos)
            Decrypted+=every_element_original
        elif every_element.isdigit():
            # if it's a number,shift its actual value 
            every_element_original=(int(every_element)-key)%10
            Decrypted+=str(every_element_original)
        else:
            # if its neither alphabetical nor a number, just leave it like that
            Decrypted+=every_element
    return Decrypted
