TERMINATE=False
while not TERMINATE:
    if position == length:
        return 1
    num=(int(input("Enter the number to be grouped:")))
    res=0
    Summation=0
    for i = position; i<length; i++:
        Summation += (num[i] - '0')
        if  (Summation >= prev_sum)
        res += 
    cycle_num=(birth_year-1990)%5
    print("Your Chinese Zodiac is",zodiac_animal[cycle_num],'\n')
    print("Your Personal Charachteristics are")
    print(characteristics[cycle_num])
    response=print("Would You like to give a new input?(y/n)")
    while response!="y" and response!= "n":
        response=input("y or n")
        if response=="n":
            TERMINATE=True