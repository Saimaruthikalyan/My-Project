#largest of 3 numbers
'''a=int(input("enter the val1:-"))
b=int(input("enter the val2:-"))
c=int(input("enter the val3:-"))
if a>b:
    if a>c:
        print(f"{a} first number is greater")
elif b>a:
    if b>c:
        print(f"{b} second number is greater")
else:
    print(f"{c} third number is greater")'''
# largest of 4 numbers
'''a=int(input("enter the val1:-"))
b=int(input("enter the val2:-"))
c=int(input("enter the val3:-"))
d=int(input("enter the val4:-"))
if a>b:
    if a>c:
        if a>d:
            print(a,"is greater")
        else:
            print(d,"is greater")
    else:
        if c>d:
            print(c,"is greater")
        else:
            print(d,"is greater")
else:
    if b>c:
        if b>d:
            print(b,"is greater")
        else:
            print(d,"is greater")
    else:
        if c>d:
            print(c,"is greater")
        else:
             print(d,"is greater")'''

#largest of 5 numbers 
#check given year is perfect leap year or not
year=int(input("Enter The Year:"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(year,"is a perfect leap year")
        else:
            print(year,"is not a perfect leap year")
    else:
        print(year,"it is only a leap year")
else:
    print(year,"is not a perfect leap year")
