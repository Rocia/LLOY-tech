# encryption key (a,z),(b,y) 
passwordOut=""
case_changer=ord('a')-ord('A')
encryption_key=(('a','z'),('b','y'),('c','x'),('d','w'),('e','v'),('f','u'),('g','t'),('h','s'),('i','k'),('j','q'),('k','p'),('l','o'),('m','n'),('n','m'),('o','l'),('p','k'),('q','j'),('r','i'),('s','h'),('t','g'),('u','f'),('v','e'),('w','d'),('x','c'),('y','b'),('z','a'))
print("this programwill encrypt and decrypt the passward")
which=input('enter(e) to encrypt the passward and (d) to decrypt ')

while  which!='d' and which!='e':
    which=input('\n invalid, enter valid details- Enter (E) to encrypt the passward and (d) to decrypt')
encrypting= (which=='e')
passward_in=input("enterpassward")
if encrypting :
    from_index=0
    to_index=1 
else:
     from_index=1
     to_index=0
case_changer=ord('a')-ord('A')
for ch in passward_in:
    letter_found= False
    
    for t in encryption_key:
        if ('a'<=ch and ch<='z') and ch==t[from_index]:
            passwordOut=passwordOut+t[to_index] 
            letter_found=True
        elif ('a'<=ch and ch<='z') and chr(ord(ch)+32)==t[from_index]:
            passwardOut=passwordOut+chr(ord(t([to_index])))-case_changer
            letter_found=True

    if not letter_found:
        passwardOut=passwardOut+ch
        
if encrypting:
    print('passward is:',passwordOut) 
else:
    print('passward is:', passwordOut)