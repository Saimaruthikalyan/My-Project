#-----------------------01-09-2025---------------------------------

###------------------Looping Statements----------------------------

####--------------------while loop---------------------------------

# 01.Print first five natural numbers.
'''
a=1
while a<=5: #i<6,1<=5
    print(a) #1,2,3,4,5
    a+=1   #a=a+1,,i=1,i=2,i=3,i=4,i=5
'''

# 02.print first five natural numbers in a reverse order.
'''
a=5
while a>=1:
    print(a)
    a-=1
'''
# 03.print first n natural numbers.
'''
a=int(input("Enter the Number:"))
i=1
while i<=a:
    print(a)
    a+=1
'''
# 04.print first n natural numbers in a reverse order.
'''
a=int(input("Enter the Number:"))
i=1
while a>=i:
    print(a)
    a-=1
'''
# 05. print first n even numbers(consider 0 as even without using conditional statements).
'''
a=int(input("Enter the Number:"))
i=0
while i<a: #i<n*2
    print(i*2) #i
    i+=1 #i+=2
'''
# 06. print first n even numbers(consider 0 as even, using conditional statements).
'''
a=int(input("Enter the Number:"))
i=0
while i<a*2:
    if i%2==0:
        print(i)
    i+=1
'''
# 07. print n natural numbers in list.
'''
a=int(input("Enter the Number:"))
i=1
l=[]
while i<=a:
   l.append(i)
   i+=1
print(l)
'''
# 08. print n natural numbers in list (without using built in function).
'''
a=int(input("Enter the Number:"))
i=1
l=[]
while i<=a:
    l=l+[i]
    i+=1
print(l)
'''
# 09. print n natural numbers in tuple.
'''
a=int(input("Enter the Number:"))
i=1
l=()
while i<=a:
   l=l+(i,)
   i+=1
print(l)
'''
# 10. print n natual numbers in set.
'''
a=int(input("Enter the Number:"))
i=1
s=set()
while i<=a:
    s=s|{i}
    i+=1
print(s)
'''
# 11.print sum of first n natural numbers.
'''
a=int(input("Enter the Number:"))
i=1
s=0
while i<=a:
    s+=i
    i+=1
print(s)
'''
# 12. print the product of first n natural number.
'''
a=int(input("Enter the Number:"))
i=1
p=1
while i<=a:
    p*=i
    i+=1
print(p)
'''
# 13a. multiplication table.
#7=7*7=7,..........,7*10=70
'''
a=int(input("Enter the Number:"))
i=1
while i<=10:
    print(f"{a} X {i} = {a*i}")
    i+=1
'''
# 13b.mutiplication table reverse
'''
a=int(input("Enter the Number:"))
i=10
while i>=1:
    print(f"{a} X {i} = {a*i}")
    i-=1
'''
#---------------------02-09-2025------------------------

#-----------------Collection DataType-------------------

#-------------------Looping Statement-------------------

#-------------------while loop--------------------------

# 01a. print all the characters present in a given str.
'''
st=input("enter the string:")
i=0
while i<len(st):
    print(st[i])
    i+=1
'''
# 01b. reverse the string.
'''
n=input("enter the string:")
i=len(n)-1
while i>=0:
    print(n[i])
    i=i-1
'''
# 02a. extract only vowels from given string.
'''
n=input("enter the string:")
i=0
while i<len(n):
    if n[i] in 'AEIOUaeiou':
        print(n[i])
    i+=1
'''
# 03a. check no of vowels present in the string.
'''
n=input("enter the string:")
i=0
v=0
while i<len(n):
    if n[i] in 'AEIOUaeiou':
        v+=1
    i+=1
print(v)
'''
# 04a. print all the characters from a str where character is alphabet then print its acsii value otherwise print the character.
'''
n=input("enter the string:")
i=0
while i<len(n):
    if 'a'<=n[i]<='z' or 'A'<=n[i]<='Z':
        print(ord(n[i]))
    else:
        print(n[i])
    i+=1
'''
# 05a. in a given string, if found alphabet toggle it.
'''
n=input("enter the string:")
i=0
while i<len(n):
    if  'A'<=n[i]<='Z':
        print(chr(ord(n[i])+32))
    elif 'a'<=n[i]<='z':
        print(chr(ord(n[i])-32))
    else:
        print(n[i])
    i+=1
'''
# 06a. from a given message print all vowel and consonats seperately
'''
n=input("enter the string:")
i=0
v=''
c=''
while i<len(n):
    if n[i] in 'AEIOUaeiou':
        v+=n[i]
    elif n[i] not in 'AEIOUaeiou':
        c+=n[i]
    i+=1
print("vowels:",v)
print("consonats:",c)
'''
# 07a. reverse the srting slicing (use only indexing).
'''
n=input("enter the string:")
i=len(n)-1  #i=0  ,s=''
while i>=0:  #i<len(n)  s=n[i]+s
    print(n[i])
    i-=1 # i=i+1  #print(s)
''' 
# 08a. toggle string
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
# 09a. reverse the list.
'''
n = eval(input("Enter the list: "))
i = len(n) - 1
r = []
while i >= 0:
    r.append(n[i])
    i -= 1
print("Reversed list:", r)
'''
# 10a.from a list print only integers.
'''
n = eval(input("Enter the list: "))   
i = 0
r = []
while i < len(n):
    if type(n[i]) == int:
        r.append(n[i])
    i += 1
print("Only Integers:", r)
'''
# 11a. reverse a list only if second value is complex number.
'''
n = eval(input("Enter the list: "))   
i = len(n) - 1
r = []
while i >= 0:
    if type(n[1]) == complex:   
        r.append(n[i])
    i -= 1

if r:
    print("Reversed list:", r)
else:
    print("Second element is not a complex number. Original list:", n)
'''
# 12a. reverse a string only in it not palindrome and not starting with vowel. 

'''
s = input("Enter a string: ")

i = len(s) - 1
r = ""

while i >= 0:
    if s != s[::-1] and s[0].lower() not in "aeiou":
        r += s[i]
    i -= 1

if r:
    print("Reversed string:", r)
else:
    print("Condition not satisfied. Original string:", s)
'''
#------------------------------03-09-2025---------------------------------------

# 01a. find the sum of all the ascii characters from string.
'''
n=input("Enter The String:")
i=0
s=0
while i<=len(n)-1:
    s=ord(n[i])+s ##s+=ord(n[i])
    i+=1
print(s)
'''
# 02a. remove duplicate chatacters from a string.
'''
n=input("Enter The String:")
i=0
s=''
while i<=len(n)-1:
    if n[i] not in s:
        s+=n[i]
    i+=1
print(s)
'''
# 3a. reverse duplicate character from a string.
'''
n=input("Enter The String:")
i=0
s,p='',''
while i<=len(n)-1:
    if n[i] not in s:
        s+=n[i]
    else:
        p+=n[i]
    i+=1
print(p)
'''
# 4a. print duplicate character along with index number from a string.
'''
n=input("Enter The String:")
i=0
s=''
p=''
while i<len(n):
    if n[i] not in s:
        s+=n[i]
    else:
        p+=n[i]
        print(f"{n[i]} is repeating at index {i} ")
    i+=1
'''
# 4b. print duplicate character along with negative index from a string
'''
n=input("Enter The String:")
i=0
s=''
p=''
c=0
while i<=len(n)-1: #i<len(n)
    c+=1
    if n[i] not in s:
        s+=n[i]
    else:
        p+=n[i]
        print(f"{n[i]} is repeating at index {-c} ") #{(-i-1)}
    i+=1
'''
# 4c. reverse of str.
'''
n=input("Enter The String:")
i=0
s,l='',[]
while i<=len(n)-1: #i<len(n)
    if n[i] not in s:
        s+=n[i]
    else:
        l+=[f'{n[i]} is repeating at index {-(len(n)-(i))}']
    i+=1
j=-1
while j>=-len(l):
    print(l[j])
    j-=1
'''
# 5a. check given character is present in a given message.
#     if it is present ,print it's index position where it is present.
'''
n=input("Enter The Message:")
m=input("Enter The Character")
if m in n:
    i=0
    while i<len(n):
        cm=0
        if n[i]==m and cm==0:
            print(f"The Given Character {m} is present at {i}")
            cm+=1
        i+=1
'''
#---------------------------04-09-2025-----------------------------

#--------------------Single value datatypes------------------------

# 1a. Find the sum of all the digits from given integer.
# 108 ---> 1+0+8=9
'''
n=int(input("Enter the Number:"))
s=0
while n>0:
    l=n%10
    s+=l
    n=n//10
print(s)
'''
# 2a. Find the reverse of given integer without typecastig.
# 1234 ----> 4321
'''
n=int(input("Enter the Number:"))
r=0
while n>0:
    l=n%10
    r=r*10+l
    n=n//10
print(r)
'''
# 3a. Check given integer is palindrome number or not.
'''
n=int(input("Enter the Number:"))
r=0
s=n
while n>0:
    l=n%10
    r=r*10+l
    n=n//10
if s==r:
    print("The Given Number is Palindrome Number")
else:
    print("The Given Number is not Palindrome Number")
'''
# 4a. Check the given number are not SPY number or not.
#123---> 1+2+3=1*2*3
'''
n=int(input("Enter the Number:"))
a=0
e=1
while n>0:
    l=n%10
    a+=l
    e*=l
    n=n//10
if a==e:
    print("The Given number is a SPY Number")
else:
    print("The Given number is NOT a SPY Number")
'''
# 5a. Find the factorial of given number.
'''
n=int(input("Enter the Number:"))
e=1
while n>=1:
    e=e*n
    n-=1
print(e)
'''
# 6a. Find the first digit of a given number.
## 3456---> 3
'''
n=int(input("Enter the Number:"))
while n>10:
    n//=10
print(n)
'''
# 7a. Check the given number is prime number or not.####***********itq
'''
n=int(input("Enter the Number:"))
if n<2:
    print("It is not a Prime Number")
else:
    i=2
    f=1
    while i<n:
        if n%i==0:
            f+=1
        i+=1
    else:
        if f==1:
            print("It is a Prime Number")
        else:
            print("It is not a Prime Number")
        
'''
# 7b. Check the given number is prime number or not.####***********itq
'''
n=int(input("Enter the Number:"))
i=1
c=0
while i<=n:
    if n%i==0:
        c+=1
    i+=1
if c==2:
    print("It is a Prime Number")
else:
    print("It is not a Prime Number")
'''
# 8a. i/p:- python is easy
#     o/p:- {'python':6,'is':2,'easy':4}
'''
s=input("Enter the String:").split()
d={}
i=0
while i<=len(s)-1:
    d[s[i]]=len(s[i])
    i=i+1
print(d)
'''
# 8b. i/p:- python is easy
#     o/p:- {'python':6,'is':2,'easy':4}(without using len function)
'''
s=input("Enter the String:").split()
d={}
i=0
while i<=len(s)-1:
    l=0
    j=0
    while j<=len(s[i])-1:
        j+=1
        l+=1
    d[s[i]]=j
    i=i+1
print(d)
'''

#-------------------------------05-09-2025-----------------------------------

# 1a. i/p:- python is easy
#     o/p:- {'python':6,'is':2,'easy':4}(without using split function)
'''
s=input("Enter the String:")
d=[]
i=0
l=''
while i<len(s):
    if s[i]!=' ':
        l+=s[i]
        #if i==len(s)-1:
            #d.append(ld)
    else:
        d.append(l)
        l=''
    i+=1
d+=[l]
print(d)
'''
#- 2a. i/p:- apples are red
#     o/p:- {'apples':'selppa','are':'era','red':'der'}
'''
a=input("Enter the String:")
d={}
i=0
s=''
while i<len(a):
    if a[i]!=' ':
        s+=a[i]
        #if i==len(s)-1:
            #d.append(ld)
    else:
        d[s]=s[::-1]
        s=''
    i+=1
d[s]=s[::-1]
print(d)
'''
# 2b.i. i/p:- apples are red
#     o/p:- {'apples':'ae','are':'ae','red':'e'}
'''
a=input("Enter the String:") 
d={}
#l,b='',''
i=0
while i<len(a):
    if a[i]!=' ': 
        l+=a[i]
        if a[i] in 'aeiouAEIOU':
            b+=a[i]
    else:
        d[l]=b
        l,b='',''
    i+=1
d[l]=b
print(d)
'''
# 2b.ii. i/p:- apples are red
#     o/p:- {'apples':'ae','are':'ae','red':'e'}
'''
a=input("Enter the String:").split
d={}
i=0
while i<len(a):
    v="aeiouAEIOU"
    s=''
    j=0
    while j<len(a[i]):
        if a[i][j] in v:
            s+=a[i][j]
        j+=1
    d[a[i]]=s
    i+=1
print(d)
'''
'''programmingbyraj@gmail.com'''

