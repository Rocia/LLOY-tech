from random import randint
terminate=False
empty_str=' '

while  not terminate:
    amount=randint(1,99)
    print("Enter coins that add up to ",amount,"cents 1 per line \n")
    game_over=False
    total=0
    
    while not game_over:
        valid_entry=False
        
        while not valid_entry:
            if total==0:
                entry=input("Enter 1st coin")
            else:
                entry=input("Enter next coin")    
        
            if entry in (empty_str,'1','5','10','25'):
                valid_entry=True
            else:
                print("Invalid Entry")
        if entry==empty_str:
            if total==amount:
                print("correct")
            else:
                print("you only entered",total,"cents.")
                game_over= True
        else:
            total=total+int(entry)
            if total >amount:
                print("sorry! total exceeds",amount,"cents.")
                game_over=True
            if game_over:
                entry=input("try again(y/n)")
            
                if entry=='n':
                    terminate=True
print("Thanks for playing :) :) :)")
            #elif entry=='y':
            #    terminate= False
            #elif entry!='y' and entry!='n':
            #   print("invalid input... plzzz enter (y/n):")
                
             
            