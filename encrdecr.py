'''
problem statement: define encryption Key
'''
from doctest import OutputChecker
passOut=""
case_changer=ord('a')-ord('A')
encKey=(('A', 'E'),('B', 'F'),('C', 'G'),('D', 'H'),('E', 'I'),('F', 'J'),('G', 'K'),('H', 'L'),('I', 'M'),('J', 'N'),('K', 'O'),('L', 'P'),('M', 'Q'),('N', 'R'),('O', 'S'),('P', 'T'),('Q','U'),('R', 'V'),('S', 'W'),('T', 'X'),('U', 'Y'),('V', 'Z'),('W', 'A'),('X', 'B'),('Y', 'C'),('Z', 'D'),('a', 'e'),('b', 'f'),('c', 'g'),('d', 'h'),('e', 'i'),('f', 'j'),('g', 'k'),('h', 'l'),('i', 'm'),('j', 'n'),('k', 'o'),('l', 'p'),('m', 'q'),('n', 'r'),('o', 's'),('p', 't'),('q','u'),('r', 'v'),('s', 'w'),('t', 'x'),('u', 'y'),('v', 'z'),('w', 'a'),('x', 'b'),('y', 'c'),('z', 'd'))
print("this prog will encrypt and decrypt th users password")
which= input("Enter (e) to  encrypt the password and (d) to decrypt the password ")
while which != 'e' and which !='d':
    which=input("invalid input")
encp=(which=='e')
pswd=input("enter pswd")

if encp:
    from_index=0
    to_index=1
else:
    from_index=1
    to_index=0
    
case_changer=ord('a')-ord('A')

for ch in pswd:
    letter_found=False
    
    for t in encKey:
        if ('A'<=ch and ch<='Z' or 'a'<=ch and ch<='z') and ch==t[from_index]:
            passOut=passOut+t[to_index] 
            letter_found=True
        elif ('A'<=ch and ch<='Z' or 'a'<=ch and ch<='z') and chr(ord(ch)+32)==t[from_index]:
            passOut=passOut+chr(ord(t([to_index])))-case_changer
            letter_found=True
    if not letter_found:
            passOut=passOut+ch
if encp:
        
    print("your encypted password is:",passOut)
else:
    print("your decrypted password is:",passOut)  
'''                        
cont = input("Would you like to continue? (y/n)")
while which != 'y' and which !='n':
    which=input("invalid input")
    
cont=(which=='y')
pswd=input("enter pswd")

cont=(which=='n')
break 
'''
'''Output:
this prog will encrypt and decrypt th users password
Enter (e) to  encrypt the password and (d) to decrypt the password e
enter pswdastaroth
your encypted password is: ewxevsxl
'''