import re

def encrypt(key,plaintext):
    plaintext = plaintext.split(',')
    k1,k2 = genkey(key)
    plaintext = plaintext[:-1]
  
    for i in range(len(plaintext)):
        plaintext[i] = re.findall(r"([^b])", plaintext[i])
        plaintext[i].pop(0)
        if len(plaintext[i]) != 8:
            for j in range(8-len(plaintext[i])):
                plaintext[i].insert(0,'0')   
    for i in  range(len(plaintext)):
        plaintext[i]= IP(plaintext[i])
        plaintext[i] = fk(plaintext[i],k1)
        plaintext[i] = switchF(plaintext[i])
        plaintext[i] = fk(plaintext[i],k2)
        plaintext[i]= IP_inverse(plaintext[i])
    return plaintext

def permutation(n,bit):
    result = []
    position =[]
    if bit == 10:
        position = [3,5,2,7,4,10,1,9,8,6]
    elif bit == 8:
        position = [6,3,7,4,8,5,10,9]
    else:
        position = [2,4,3,1]  
    for i in position:
        result.append(n[i-1]) 
        
    return result
    
def EP(n):
    result = []
    position =[4,1,2,3,2,3,4,1]
    for i in position:
        result.append(n[i-1]) 
    return result

def shiftbit(n):
    n1 = n[0:5]
    n2 = n[5:10]
    n1.append(n1.pop(0))
    n2.append(n2.pop(0))
    n = n1 + n2
    return n

def sbox(n,s):
    
    
    row = int(str(n[0])+str(n[3]),2)
    col = int(str(n[1])+str(n[2]),2)
    
    sbox = []
    if s == 0:
        sbox = [[['0','1'],['0','0'],['1','1'],['1','0']],[['1','1'],['1','0'],['0','1'],['0','0']],
            [['0','0'],['1','0'],['0','1'],['1','1']],[['1','1'],['0','1'],['1','1'],['1','0']]]
    else:
        sbox = [[['0','0'],['0','1'],['1','0'],['1','1']],[['1','0'],['0','0'],['0','1'],['1','1']],
            [['1','1'],['0','0'],['0','1'],['0','0']],[['1','0'],['0','1'],['0','0'],['1','1']]]
    return sbox[row][col]

def switchF(n):
    for x in range(4):
        n.append(n.pop(0))
    return n

def IP(n):
    result = []
    position =[2,6,3,1,4,8,5,7]
    for i in position:
        result.append(n[i-1]) 
    return result

def IP_inverse(n):
    result = []
    position =[4,1,3,5,7,2,8,6]
    for i in position:
        result.append(n[i-1]) 
    return result

def XOR(n0,n1):
    result = []
    for i in range(len(n0)):
        if n0[i] == n1[i]:
            result.append('0')   
        else:
            result.append('1')
    return result

def genkey(key):
    k = permutation(key,10)
    k = shiftbit(k)
    k1 = permutation(k,8)
    k = shiftbit(shiftbit(k))
    k2 = permutation(k,8)
    return k1,k2

def fk(n,k):
    fk = EP(n[4:8])
    fk1 = XOR(k,fk)
    fk2 = sbox(fk1[0:4],0)
    fk3 = sbox(fk1[4:8],1)
    fk4 = fk2 + fk3
    fk4 = permutation(fk4,4)
    fk = XOR(n[0:4],fk4)
    result = fk+n[4:8]
    return result




def binaryToDecimal(binary): 
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal


def decrypt(key,ciphertext):
    
    ciphertext = ciphertext.split(',')
   
    k1,k2 = genkey(key)
   
    ciphertext = ciphertext[:-1]
    for i in range(len(ciphertext)):
        ciphertext[i] = re.findall(r"([^b])", ciphertext[i])
        ciphertext[i].pop(0)
        if len(ciphertext[i]) != 8:
            for j in range(8-len(ciphertext[i])):
                ciphertext[i].insert(0,'0')  
    
    for i in  range(len(ciphertext)):
        ciphertext[i]= IP(ciphertext[i])
        ciphertext[i] = fk(ciphertext[i],k2)
        ciphertext[i] = switchF(ciphertext[i]) 
        ciphertext[i] = fk(ciphertext[i],k1)
        ciphertext[i]= IP_inverse(ciphertext[i])
    return ciphertext


keyss = []
Ciphertext = '0b10011101,0b1110011,0b11001101,0b1100011,0b11000,0b11001101,0b1100011,0b1001000,0b1100011,0b110,0b1100011,0b10010110,0b1100011,0b10010110,0b10011101,0b10010110,0b11000011,0b10011101,0b10010110,0b10010110,0b11010011,0b11000,0b1110011,0b11000,0b110,0b11001101,0b1100011,0b10011101,0b11010011,0b10011101,0b11001101,0b11001101,0b10011101,0b11000011,0b110,0b11000011,0b11001101,0b110,0b11001101,0b1110011,0b1110011,0b11000011,0b1110011,0b1100011,0b1110011,0b110,0b10011101,0b1100011,0b1110011,0b11010011,0b1001000,0b11001101,0b11001101,0b11010011,0b11000011,0b10010110,0b11010011,0b1110011,0b10011101,0b10011101,0b11001101,0b11000,0b110,0b1110011,0b11000,0b10010110,0b11000011,0b1110011,0b1001000,0b11000,0b10010110,0b1001000,0b110,0b11001101,0b1110011,0b11000011,0b11010011,'
for i in range(1024):
    
    key = str(bin(i))[2:]
    keyarr = re.findall(r"\d", key)
    
    if len(keyarr) != 10:
        for j in range(10-len(keyarr)):
            keyarr.insert(0,'0') 
    decrypttext = decrypt(keyarr,Ciphertext)
    
    for j in range(len(decrypttext)):
        decrypttext[j]=decrypttext[j][0] + decrypttext[j][1] + decrypttext[j][2] + decrypttext[j][3] + decrypttext[j][4] + decrypttext[j][5] + decrypttext[j][6] + decrypttext[j][7]
    
    if(binaryToDecimal(int(decrypttext[0])) == ord('5') and binaryToDecimal(int(decrypttext[1])) ==  ord('9') and binaryToDecimal(int(decrypttext[2])) == ord('0') and binaryToDecimal(int(decrypttext[3])) == ord('6') and binaryToDecimal(int(decrypttext[4])) == ord('1') and binaryToDecimal(int(decrypttext[5])) == ord('0') and binaryToDecimal(int(decrypttext[6])) == ord('6') and binaryToDecimal(int(decrypttext[7])) == ord('4') and binaryToDecimal(int(decrypttext[8])) == ord('6') ):
        keyss.append(decrypttext)
        keyss.append(key)
plaintext = ''
for i in range(len(keyss[0])):
    keyss[0][i] = '0b' +  keyss[0][i]
    plaintext += keyss[0][i] + ','
print("key=",keyss[1])    
print("plaintext=",plaintext)








