#RSA_ENCRYPTION_&_DECRYPTION
import Crypto, libnum, sys
from Crypto.Util.number import bytes_to_long as BTL
from Crypto.Util.number import  long_to_bytes as LTB
from Crypto.Random import get_random_bytes as GRB
bitss=60
message_to_encrypt=input("ENTER A MESSAGE TO BE ENCRYPTED: ")
#STEP-1: Select two co-prime numbers as p and q.
p = Crypto.Util.number.getPrime(bitss, randfunc=GRB)
q = Crypto.Util.number.getPrime(bitss, randfunc=GRB)
#STEP-2: Compute n as the product of p and q.
n = p*q
#STEP-3: Compute (p-1)*(q-1) and store it in z.
z=(p-1)*(q-1)
#STEP-4: Select a random prime number e that is less than that of z.
e=65537
#STEP-5: Compute the private key, d as e * mod-1(z).
d=libnum.invmod(e,z)
m=BTL(message_to_encrypt.encode('utf-8'))
#STEP-6: The cipher text is computed as messagee * mod n.
c=pow(m,e,n)
#STEP-7: Decryption is done as cipherdmod n.
res=pow(c,d,n)
print(f'p (1st.co-pime)={p}\n')
print(f'q (2nd.co-prime)={q}\n')
print(f'n (product of p,q)={n}\n')
print(f'e (less_than_z)={e}\n')
print(f'd (private-key e,z)={d}\n')
print (f'Message={message_to_encrypt}\n')
print(f'cipher_text ={c}\n')
print(f'decrypted_message:{LTB(res)}')