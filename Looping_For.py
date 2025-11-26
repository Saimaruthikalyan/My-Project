#--------------------------------------------------------------------------------
#                                For Loop
#--------------------------------------------------------------------------------

# 1a. print all the values given in a list.
'''
l=eval(input("Enter the List:"))
for q in l:
    print(q)
'''
# 2a. print all the vowels present in a given string.
'''
s=input("Enter the String:")
for q in s:
    if q in "AEIOUaeiou":
        print(q)
'''
# 3a. print all the cosonents present in a given string.
'''
s=input("Enter the String:")
for q in s:
    if q not in "AEIOUaeiou" and q.isalpha():
        print(q)
'''
# 4a. find sum of all the ASCII value from a given string.
'''
s=input("Enter the String:")
a=0
for i in s:
    a+=ord(i)
print(a)
'''
# 5a. find product of ASCII values of vowels.
'''
a=input("Enter the String:")
p=1
for s in a:
    if s in "AEIOUaeiou":
        p*=ord(s)
print(p)
'''
# 5a(i). while loop.
'''
a=input("Enter the String:")
p=1
i=0
while i<len(a):
    if a[i] in "AEIOUaeiou":
        p*=ord(a[i])
    i+=1
print(p)
'''
# 6a. find sum of only integer from given list.
'''
a=eval(input("Enter the List:"))
w=0
for i in a:
    if type(i)==int:
        w+=i
print(w)
'''
# 6a(i). while loop.
'''
a=eval(input("Enter the List:"))
w=0
i=0
while i<=len(a):
    if type(i)==int:
        w+=i
    i+=1
print(w)
'''
# 7a. reverse a string.
'''
s=input("Enter the String:")
i=0
r=''
while i<len(s):
    r=s[i]+r
    i+=1
print(r)
'''
# 7a(i). for loop.
'''
s=input("Enter the String:")
r=''
for i in s:
    r=i+r
print(r)
'''
# 8a. i/p:- happy reddy going to marathalli.
#     o/p:-{'happy':5,'reddy':5,'going':5,'to':2,'marathalli':9}
'''
a=input("Enter the String:").split()
d={}
for i in a:
    s=0
    for _ in i:
        s+=1
    d[i]=s
print(d)
'''
# 9a. i/p:- happy reddy going to marathalli.
#     o/p:-{'happy':'marathalli','reddy':'to','going':'going','to':'reddy','marathalli':'happy'}
'''
a=input("Enter the String:").split()
b=0 # b=len(a)-1
d={}
for i in a:
    d[i]=a[-b-1] # d[i]=a[b]
    b+=1 # b-=1
print(d)
'''
# 10a. i/p:- happy reddy going to marathalli.
#      o/p:-{'happy':'reddy','reddy':'going','going':'to','to':'marathalli','marathalli':'happy'}
'''
l = input("Enter the String: ").split()
d = {}
a=0
for i in l:
    if i==len(a):
        d[i]=l[0]
    else:
        d[i]=l[a]
    a+=1
print(d)
'''
#--------------------------------------------------------19-09-2025----------------------------------------------------

# 1a. display first n natural number in a single line using for loop.
'''
n=int(input("Enter the Number:"))
for i in range(1,n+1):
    print(i,end=',')
'''
# 2a. print n even number between the given range.
'''
n=int(input("Enter the Starting Number:"))
s=int(input("Enter the Ending Number"))
for i in range(n,s):
    if i%2==0:
        print(i,end=',')
'''
# 3a. print first n odd numbers in a single line.
'''
n=int(input("Enter the Starting Number:"))
for i in range(1,n*2,2):
   # if i%2!=0:
        print(i,end=',')
'''
# 4a. print first n even numbers.
'''
n=int(input("Enter the Starting Number:"))
for i in range(0,n*2,2):
        print(i)
'''
# 5a. print all the characters present at even index position from a string.
'''
s=input("Enter the String:")
for i in range(0,len(s),2):
        print(s[i])
'''
# 6a. list1:=[1,2,3,4,5]
#     list2:=[2,4,6,8,10]
#     o/p:=[3,6,9,12,15]
'''
l1=eval(input("Enter the Values for List1:-"))
l2=eval(input("Enter the Values for List2:-"))
r=[]
if len(l1)==len(l2):
        for i in range(len(l1)):
                if type(l1[i])==type(l2[i]):
                        r.append(l1[i]+l2[i])
                else:
                        l.append('Not Possible')
        print(r)   
else:
        print("Length are Unequal")
'''
# 7a. print all the even values present at odd index of a given list.
'''
s=eval(input("Enter the List:"))
for i in range(1,len(s),2):
        print(s[i])
'''
