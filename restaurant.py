tax=0.15
p1star=(int)(input(print("Enter the cost of starter")))
p1mc=(int)(input(print("Enter the cost of Main cOurse")))
p1des=(int)(input(print("Enter the cost of Desert")))
p1coupon=(int)(input(print("Enter coupon amount")))

bill=p1star+p1mc+p1des
print(bill,"without tax")

print("You have entered coupon amount",p1coupon)
if p1coupon>bill:
    credit=p1coupon-bill
    print ("Total amount credited",credit)
elif p1coupon<bill:
    pay=bill-p1coupon
    print ("Total amount payable",pay,"bill=",pay+(pay*0.15))
else:
    print("Your total was exactly equal to your coupon amount","bill=",bill+(bill*0.15))
    
    
'''
Enter the cost of starter
None200
Enter the cost of Main cOurse
None500
Enter the cost of Desert
None700
Enter coupon amount
None150000
1400 without tax
You have entered coupon amount 150000
Total amount credited 148600
'''
'''p2star=(int)(input(print("Enter the cost of starter")))
p2mc=(int)(input(print("Enter the cost of Main cOurse")))
p2des=(int)(input(print("Enter the cost of Desert")))
p2coupon=(int)(input(print("Enter coupon amount")))

p3star=(int)(input(print("Enter the cost of starter")))
p3mc=(int)(input(print("Enter the cost of Main cOurse")))
p3des=(int)(input(print("Enter the cost of Desert")))
p3coupon=(int)(input(print("Enter coupon amount")))'''