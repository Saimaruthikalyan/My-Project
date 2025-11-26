#------------------------------06-09-2025--------------------------------------

# 1a. i/p:- apples are red
#     o/p:-{'ae':'apples','ae':'are','e':'red'}
'''
a=input("Enter the string:").split()
d={}
i=0
while i<len(a):
    v='aeiouAEIOU'
    j=0
    s=''
    while j<len(a[i]):
        if a[i][j] in v:
            s=s+a[i][j]
        j+=1
    d[s]=a[i]
    i+=1
print(d)
'''
## 1b. i/p:- apples are red
#     o/p:-{'apples':'e','are':'e','red':'e'}
'''
a=input("Enter the string:").split()
d={}
i=0
while i<len(a):
    v='aeiouAEIOU'
    j=0
    while j<len(a[i]):
        if a[i][j] in v:
            s=a[i][j]
        j+=1
    d[a[i]]=s
    i+=1
print(d)
'''
# 1b. i/p:- apples are red
#     o/p:-{'apples':'ea','are':'ea','red':'e'}
'''
a=input("Enter the string:").split()
d={}
i=0
while i<len(a):
    v='aeiouAEIOU'
    j=0
    s=''
    while j<len(a[i]):
        if a[i][j] in v:
            s=s+a[i][j]
        j+=1
    d[a[i]]=s[::-1]
    i+=1
print(d)
'''
# 2a. i/p:- reddy's heart is in java class.
##    o/p:- {"reddy's":5,'heart':3,'is':1,'in':1,'java':2,'class':4}
'''
a=input("Enter the Sring:").split()
d={}
i=0
while i<len(a):
    v='aeiouAEIOU'
    j=0
    c=0
    while j<len(a[i]):
        if a[i][j] not in v:
            if 'a'<=a[i][j]<='z' or 'A'<=a[i][j]<='Z':
                c+=1
        j+=1
    d[a[i]]=c
    i+=1
print(d)
'''
# 2a. i/p:- reddy attending is java mock.
##    o/p:- {"reddy":'ry','attending':'ag','is':'is','in':'in','java':'ja','mock':'mk'}
'''
a=input("Enter the Sring:").split()
d={}
i=0
while i<len(a):
    s=''
    j=0
    while j<len(a[i]):
        s=a[i][0]
        s+=a[i][-1]
        j+=1
    d[a[i]]=s
    i+=1
print(d)
'''
# 2b. i/p:- reddy attending is java mock.
##    o/p:- {"reddy":'ry','attending':'ag','is':'is','in':'in','java':'ja','mock':'mk'}
'''
a=input("Enter the String:").split()
d={}
i=0
while i<len(a):
    d[a[i]]=a[i][0]+a[i][-1]
    i+=1
print(d)
'''
#-------------------------------------10-09-2025----------------------------------------

# 1a. i/p:- reddy is attending java mock.
#     o/p:-{'Reddy':'d','is':'is','attending':'n','java':'java','mock':'mock'}
'''
a=input("Enter the String:").split()
d={}
i=0
while i<len(a):
    if len(a[i])%2==0:
        d[a[i]]=a[i]
    else:
        d[a[i]]=a[i][len(a[i])//2]
    i+=1
print(d)
'''
# 2a. i/p:- reddy is attending java mock.
#     o/p:-{'Reddy':'14','is':'11','attending':'36','java':'22','mock':'13'}
'''
a=input("Enter the String:").split()
d={}
i=0
while i<len(a):
    j=0
    v,c=0,0
    while j<len(a[i]):
        if a[i][j] in 'aeiouAEIOU':
            v+=1
        elif a[i][j] not in 'aeiouAEIOU' and a[i][j].isalpha():
            c+=1
        j+=1
    d[a[i]]=str(v*10+c)
    i+=1
print(d)
'''
# 3a. check the given number is a strong or not.
'''
a=int(input("Enter the Number:"))
n=a
s=0
while a>0:
    ld=a%10
    f=1
    while 0<ld:
        f=f*ld
        ld=ld-1
    s=s+f
    a=a//10
if n==s:
    print("It is Strong Number.")
else:
    print("IT is Not A Strong Number")
'''
# 4a. check given number is aamstrong or not.
'''
a=int(input("Enter the Number:"))
l=0
b,c=a,a
while a>0:
    l=l+1
    a=a//10
s=0
while b>0:
    ld=b%10
    s+=ld**l
    b=b//10
if c==s:
    print("It is Strong Number.")
else:
    print("IT is Not A Strong Number")
'''
# 5a. perfect number.
'''
a=int(input("Enter the Number:"))
s=0
i=1
while i<a:
    if a%i==0:
        s+=i
    i+=1
if s==a:
    print("It's a Perfect Number.")
else:
    print("It's Not a Perfect Number.")
'''

#-----------------------------------------------10-09-2025---------------------------------------------

# ------------------------------------Intermediate Termination of Loop---------------------------------

# 1a. execute the program upto n ntural number but stop the iteration when multiple of 7 is found.
'''
n=int(input("Enter the Number:"))
i=1
while i<=n:
    if i%7==0:
        break
    print(i)
    i+=1
'''
# 2a. print n natural numbers in reverse but stop the iteration when a multiple of 8 is found.
'''
n=int(input("Enter the Number:"))
while n>0:
    if n%8==0:
        break
    print(n)
    n-=1
'''
# 3a. print all the natural number upto n skipping only multile od 4.
'''
n=int(input("Enter the Number:"))
i=1
while i<=n:
    if i%4==0:
        i+=1
        continue
    print(i)
    i+=1
'''
# 4a. from a given string print only the consonents
'''
a=input("Enter the String:")
i=0
while i<len(a):
    if a[i] in 'aeiouAEIOU' and a[i].isalpha:
        i+=1
        continue
    print(a[i],end=' ')
    i+=1
'''
#-------------------------------11/09/2025--------------------------------

# 1a. reverse a integer without type casting.
'''
a=int(input("Enter the String:"))
b=0
while a>0:
    b=b*10+a%10
    a//=10
print(b)
'''
# 2a. count number of vowels, number of consonents ,number of digits seperately i++++++++++n a given string.
'''
a=input("Enter the String:")
v,c,d=0,0,0
i=0
while i<len(a):
    if a[i] in "AEIOUaeiou":
        v+=1
    if a[i] not in "AEIOUaeiou" and a[i].isalpha():
        c+=1
    if '0'<=a[i]<='9':
        d+=1
    i+=1
print("No.Of Vowels:",v,"\nNo.Of Consonents:",c,"\nNo.Of Digits:",d)
'''
# 3a. check given sting is palindrome or not without slicing.
'''
a=input("Enter the String:")
rs=''
i=0
while len(a)>i:
    rs=a[i]+rs
    i+=1
if a==rs:
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")
'''
# 4a. toogle a sring
'''
n=input("enter the string:")
i=0
while i<len(n):
    if  'A'<=n[i]<='Z':
        print(chr(ord(n[i])+32),end='')
    elif 'a'<=n[i]<='z':
        print(chr(ord(n[i])-32),end='')
    else:
        print(n[i],end='')
    i+=1
'''
# 5a.find a factorial of a given number.
'''
a=int(input("Enter the Number:"))
s=1
while a>0:
    s=a*s
    a-=1
print(s)
'''
#---------------------------------------15-09-2025-------------------------------------------

# 1a.check given list is homogenous or heterogenous list.
'''
a=eval(input("Enter the List:"))
i=0
while i<len(a):
    if type(a[0])!=type(a[i]):
        print("This is an Heterogenous List")
        break
    i+=1
else:
    print("This is an Homogenous List")
'''
# 1b.check the given tuple is homogenous or heterogenous tuple.
'''
a=eval(input("Enter the List:"))
i=0
while i<len(a):
    if type(a[0])!=type(a[i]):
        print("This is an Heterogenous Tuple")
        break
    i+=1
else:
    print("This is an Homogenous Tuple")
'''
# 2a. check given number is prime number or not.
'''
a=int(input("Entet the Number:"))
if a<2:
    print("It is Not a Prime Number")
else:
    i=2
    while i<a:
        if a%i==0:
            print("It is Not a Prime Number")
            break
        i+=1
    else:
        print("It is a Prime Number")
'''
# 3a. print only the even number present at odd indexing from a list.
'''
a=eval(input("Enter the List:"))
i=0
while i<len(a):
    if i%2!=0 and a[i]%2==0 and type(a[i])==int:
        print(a[i], end=',')
    i+=1
'''
# 4a. from a given list, find all the values which are divisible by 4 present at odd index position.
'''
a=eval(input("Enter the List:"))
i=0
while i<len(a):
    if i%2!=0 and a[i]%4 ==0 and type(a[i])==int:
        print(a[i], end=',')
    i+=1
'''
# 5a. find the sum of all the ASCII values from a given string.
'''
s=input("Enter the String:")
i=0
m=0
while i<len(s):
    m=m+ord(s[i])
    i+=1
print(m)
'''
# 6a. WAP to print the sum of ASCII values of all uppercase alphabets from the string which are present at odd index position.
'''
s=input("Enter the String:")
i=0
m=0
while i<len(s):
    if i%2!=0 and 'A'<=s[i]<='Z':
        m=m+ord(s[i])
    i+=1
print(m)
'''
#--------------------------------------------16-09-2025-----------------------------------------------

# 1a. print 'python' for 5 times.
'''
a=input("Enter the Word:")
i=1
while i<=5:
    print(i,a)
    i+=1
'''
# 2a. print username for 8 times.
'''
a=input("Enter the Username:")
i=1
while i<=8:
    print(i,a)
    i+=1
'''
# 3a. reverse a string without slicing.
'''
a=input("Enter the String:")
i=0
r=''
while i<len(a):
    r=a[i]+r
    i+=1
print(r)
'''
# 4a.remove duplicate from a given string.
'''
a=input("Enter the String:")
i=0
r=''
while i<len(a):
    if a[i] not in r:
        r+=a[i]

    i+=1
print(r)
'''
# 5a. find the sum of first n natural numbers.
'''
a=int(input("Enter the Number:"))
s=0
while a>0:
    s+=a
    a-=1
print(s)
'''
# 6a. find the product of first n natural numbers.
'''
a=int(input("Enter the Number:"))
p=1
while a>0:
    p*=a
    a-=1
print(p)
'''
# 7a. find the no of vowels present in string.
'''
a=input("Enter the String:")
i=0
v=0
while i<len(a):
    if a[i] in "AEIOUaeiou" and a.isalpha():
        v+=1
    i+=1
print("Sum of Vowels:",v)
'''
# 8a. find the total no of capital letters presnt in a string.
'''
a=input("Enter the String:")
i=0
v=0
while i<len(a):
    if "A"<=a[i]<="Z":
        v+=1
    i+=1
print("Sum of Capitals:",v)
'''
# 9a. convert uppercase alphabet to lowercase in string.
'''
a=input("Enter the String:")
i=0
while i<len(a):
    if "A"<=a[i]<="Z":
        print(chr(ord(a[i])+32),end='')
    else:
        print(a[i],end='')
    i+=1
'''
# 10a. toogle a string.
'''
n=input("enter the string:")
i=0
while i<len(n):
    if  'A'<=n[i]<='Z':
        print(chr(ord(n[i])+32),end='')
    elif 'a'<=n[i]<='z':
        print(chr(ord(n[i])-32),end='')
    else:
        print(n[i],end='')
    i+=1
'''
# 11a. find no of 'a' present in given message.
'''
a=input("Enter the String:")
n=0
i=0
while i<len(a):
    if a[i]=='a':
        n+=1
    i+=1
print("No.Of a's in a given String:",n)
'''
# 12a. replace ' ' with '*' in a given message.
'''
a=input("Enter the String:")
i=0
while i<len(a):
    if a[i]==' ':
        print('*',end='')
    else:
        print(a[i],end='')
    i+=1
'''
# 13a. find sum of all the integers from given list.
'''
a=eval(input("Enter the List:"))
i=0
s=0
while i<len(a):
    if type(a[i])==int:
        s+=a[i]
    i+=1
print(s)
'''
#-----------------------------------17-09-2025--------------------------------------------------

# 1a. Mobile Lock Screen.
'''
import time
while True:
    i=1
    while i<=3:
        password=input("Enter the Password:")
        if password=="Kalyan16@":
            print("Mobile Unlocked")
            break
        print(f"Incorrect Password, attempts Left {3-i}")
        i+=1
    if password=="Kalyan16@":
        break
    else:
        print("Mobile Freezed For 30 Seconds")
        time.sleep(5)
'''
# 2a. Guessing a Number.
'''
import random
n=random.randint(0,100)
while True:
    un=int(input("Enter the Number Between 0-100:"))
    if un==n:
        print("You Guessed the Correct Number")
        break
    else:
        if n<un:
            print(f"{un} is Greater Than the Guessed Number.")
        elif n>un:
            print(f"{un} is Smaller Than the Guessed Number.")
        else:
            print("You Have Guessed the Lesser Number !!!")
'''
# 3a. check the given number is amstrong number.
'''
n=int(input("Enter the Number:"))
l,s=0,0
a,b=n,n
while n>0:
    l+=1
    n//=10
while a>0:
    s=s+(a%10)**l
    a//=10
print(s)
if b==s:
    print("It is a Amstrong number")
else:
    print("It is not a Amstrong Number")
'''
# 4a. I/P:-'Reddy is busy'
#     O/P:-{'busy':'Reddy','is':'is','Reddy':'busy'}
'''
n=input("Enter the String:").split()
i=0
d={}
while i<len(n):
    d[n[-1-i]]=n[i]
    i+=1
print(d)
'''
# 4a(i). I/P:-'Reddy is busy'
#     O/P:-{'busy':'Reddy','is':'is','Reddy':'busy'}
'''
a=input("Enter the String:").split()
b=a[::-1]
d={}
i=0
while i<len(a):
    d[b[i]]=a[i]
    i+=1
print(d)
'''
# 4b. I/P:-'Reddy is busy'
#     O/P:-{'busy':'Ry','is':'is','Reddy':'by'}
'''
n=input("Enter the String:").split()
i=0
d={}
while i<len(n):
    d[n[-1-i]]=n[i][0]+n[i][-1]
    i+=1
print(d)
'''
# 4b(i). I/P:-'Reddy is busy'
#     O/P:-{'busy':'edd','is':'is','Reddy':'us'}
'''
n=input("Enter the String:").split()
i=0
d={}
while i<len(n):
    d[n[-1-i]]=n[i][1:-1:1]
    i+=1
print(d)
'''
# 5a.  reverse key and value pairs.
'''
a=eval(input("Enter the Dictionary:"))
i=0
l=list(a)
rv={}
while i<len(l):
    rv[a[l[i]]]=l[i]
    i+=1
print(rv)
'''
# 6a. list all the keywords, where key should be the word and value should be its length.
'''
import keyword
k=keyword.kwlist
i=0
d={}
while i<len(k):
    d[k[i]]=len(k[i])
    i+=1
print(d)
'''
# 7a. list all the keywords, where key should be the word and value should be vowels from words.
'''
import keyword
k=keyword.kwlist
i=0
d={}
while i<len(k):
    v=''
    j=0
    while j<len(k[i]):
        if k[i][j] in 'aeiouAEIOU':
            v+=k[i]
        j+=1
    d[k[i]]=v
    i+=1
print(d)
'''
