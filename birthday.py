#casestudyno1 age in numbers and seconds
import datetime

day_birth=(int(input("Enter the day you were born")))
month_birth=(int(input("Enter the mon you were born")))
year_birth=(int(input("Enter the year you were born")))


current_day=datetime.date.today().day
current_month=datetime.date.today().month
current_year=datetime.date.today().year

#for the no of days
d=current_day-day_birth
print("day",d)
day=24*3600
e=d*day
print("final day",e)
#months
f=current_month-month_birth
print("month",f)
z=12*f
y=f*e
print("final momtn",y)
#years
b=current_year-year_birth
print("years",b)
x=y*b
print("final years",x)


print("Age in seconds")
print("actual age")
#output
'''
Enter the day you were born20
Enter the mon you were born03
Enter the year you were born1990
day -4
final day -345600
month 4
final momtn -1382400
years 26
final years -35942400
'''

