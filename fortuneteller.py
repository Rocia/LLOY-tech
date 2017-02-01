import random
havequest='y'
while havequest=='y':
    question=input("Would You like to Know your future?\n")
    print("\n You answered",question,"...")
    rand_num=random.randint(1,9)
    if rand_num==1:
        print("You shall prosper")
    elif rand_num==2:
        print("You shall bear great riches")
    elif rand_num==3:
        print("You shall find your true love")
    elif rand_num==4:
        print("You shall face hardships at work")
    elif rand_num==5:
        print("Luck will smile upon you")
    elif rand_num==6:
        print("A great endevor is coming your way")
    elif rand_num==7:
        print("You shall emass an empire")
    elif rand_num==8:
        print("You shall be crowned Queen")
    elif rand_num==9:
        print("You shall turn into a frog!!!!!!")
    havequest=input("\n Do You have Another Question?,(y/n)")
while havequest=='n':
    print("Goodbye and may fortune smile over you")
    break
        
'''
Would You like to Know your future?
y

 You answered y ...
You shall find your true love

 Do You have Another Question?,(y/n)y
Would You like to Know your future?
y

 You answered y ...
You shall be crowned Queen

 Do You have Another Question?,(y/n)n
Goodbye and may fortune smile over you
'''