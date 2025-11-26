'''#write the program to chect the character if the character is uppercase then convert to lowercase,
#if it is in lowercase then convert it into uppercase,
#if the character is numeric then print the next character,
#if it is special character then print as it is
ch=input("enter the character:-")
if 97<=ord(ch)<=122:    ##'a'<='z'
    print(chr(ord(ch)-32))
elif 65<=ord(ch)<=90:   ##'A'<='Z'
    print(chr(ord(ch)+32))
elif 48<=ord(ch)<=57:   ##'0<='9'
    print(chr(ord(ch)+1))
else:
    print(ch)

# write a program to check wheather the given number is divisible by 5 or not
n=int(input("Enter the number:-"))
if num%5==0:
    print("it is divisible by 5")
else:
    print("it is divisible by 5")

### write a program to illustrate an instagram login page.
un=input("Enter the username:-")
uname='kalyankumar'
password='kumarkalyan@1603'
if un==uname:
    print(f'welcome to the {un}')
    pd=input("Enter the password:-")
    if pd==password:
          print('successful login')
    else:
        print('password is incorrect')
else:
    print(f'{un} usename is wrong')'''
# WRITE A PROGRAM TO CHECK THE GIVEN DATA IS LIST OR NOT
#IF THE GIVEN DATA IS LIST THEN CHECK WHEATHER THE LIST IS HAVING MIDDLE VALUE OR NOT
#IF IT IS HAVING  IDDLE VALUE THEN CHECK WHEATHER IT IS STRING OR NOT
#IF IT IS STRING THEN PRINT THE LENGTH OF THE STRING
#IF IT NOT STRING THEN PRINT THE LAST VALUE OF THE LIST.
dt=eval(input('enter the value:-'))
if type(dt)==list:
    print('is is a list datatype')
    if len(dt)%2!=0:
        print('it having the middle value')
        if type(a[len((dt)//2])==str:
            print(len(a[len(a))//2])
         else:
             print('it is not a string')
    else:
        print('it iod not having the middle value')
else:
    print('it is not a list datatype')

