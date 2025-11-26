#------------------------------------------ Assignment-------------------------------------------

#1. Input: "hello world hello python"
#   Output: {'hello': 2, 'world': 1, 'python': 1}
'''
n=input('Enter a string : ').split()
d={}

for i in n:
    c=1
    if i in d:
        c+=1
    d[i]=c
print(d)
''' 
#2. Input: "apple banana"
#   Output: {'apple': {'vowels': 2, 'consonants': 3}, 'banana': {'vowels': 3, 'consonants': 3}}
'''
n=input('Enter a string : ').split()
d={}
for i in n:
    v,c=0,0
    d1={}
    for j in i:
        if j in 'aeiouAEIOU':
            v+=1
        elif j.isalpha():
            c+=1
    d1['vowels']=v
    d1['consonants']=c
    d[i]=d1
print(d)
'''
#3. Input: "python java cplusplus"
#   Output: {'python': ('p', 'n'), 'java': ('j', 'a'), 'cplusplus': ('c', 's')}
'''
n=input('Enter a string : ').split()
d={}
for i in n:
    d[i]=(i[0],i[-1])
print(d)
'''
#4. Input: "hello world"
#   Output: {'hello': 'olleh', 'world': 'dlrow'}
'''
n=input('Enter a string : ').split()
d={}
for i in n:
    d[i]=i[::-1]
print(d)
'''
#5. Input: "apple banana orange"
#   Output: {'apple': 4, 'banana': 3, 'orange': 5}
'''
n=input('Enter a string : ').split()
d={}
for i in n:
    l=[]
    m=0
    for j in i:
        if j not in 'aA':
            l+=[j]
            m+=1
    d[i]=m
print(d)
'''
#6. Input: "python is fun"
#   Output: {'python': 6, 'is': 2, 'fun': 3}
'''
n=input('Enter a string : ').split()
d={}
for i in n:
    m=0
    for j in i:
        m+=1
    d[i]=m
print(d)
'''
#7. Input: "banana mango grape"
#   Output: {'banana': ['b', 'a', 'n'], 'mango': ['m', 'a', 'n', 'g', 'o'], 'grape': ['g', 'r', 'a', 'p', 'e']}
'''
n=input('Enter a string : ').split()
d={}
for i in n:
    l=[]
    for j in i:
        if j not in l:
            l=l+[j]
    d[i]=l
print(d)
'''
#8. Input: "welcome to coding"
#   Output: {'welcome': 7, 'to': 2, 'coding': 6}
'''
n=input('Enter a string : ').split()
d={}
for i in n:
    m=0
    for j in i:
        m+=1
    d[i]=m
print(d)
'''
#9. Input: "abcd abc ab a"
#   Output: {'abcd': 4, 'abc': 3, 'ab': 2, 'a': 1}
'''
n=input('Enter a string : ').split()
d={}
for i in n:
    m=0
    for j in i:
        m+=1
    d[i]=m
print(d)
'''
#10. Input: "hello world"
#    Output: {'hello': ['h', 'e', 'l', 'o'], 'world': ['w', 'o', 'r', 'l', 'd']}
'''
n=input('Enter a string : ').split()
d={}
for i in n:
    l=[]
    for j in i:
        if j not in l:
            l=l+[j]
    d[i]=l
print(d)
'''
#-------------------------------------------Assignment--While Looping------------------------------------------

## While Loop
## _________________________________________________________________________________________________
## 39. Wap to print python for 5 times.
'''
n=input('Enter python : ')
i=0
while i<5:
    print(n)
    i+=1
'''
## 40. Wap to print n natural numbers.
'''
n=int(input('Enter number : '))
i=1
while i<=n:
    print(i)
    i+=1
'''
## 41. Wap to print multiplication table for n.
'''
n=int(input('Enter a number : '))
i=1
while i<=10:
    print(f'{n} X {i} = {n*i}')
    i+=1
'''
## 42. Wap to find the sum of n natural numbers.
'''
n=int(input('Enter number : '))
i=1
s=0
while i<=n:
    s=s+i
    i+=1
print(s)
'''
## 43. Wap to find the product of n natural numbers or factorial of a number.
'''
n=int(input('Enter number : '))
i=1
p=1
while i<=n:
    p=p*i
    i+=1
print(p)
'''
## 44. Wap to print all the characters of a string.
'''
n=input('Enter string : ')
i=0
while i<len(n):
    print(n[i])
    i+=1
'''
## 45. Wap to print all the characters present at even index of a string.
'''
n=input('Enter string : ')
i=0
while i<len(n):
    if i%2==0:
        print(n[i])
    i+=1
'''
## 46. Wap to extract all the lowercase characters present in a string.
'''
n=input('Enter string : ')
i=0
while i<len(n):
    if 'a'<=n[i]<='z':
        print(n[i],end='')
    i+=1
'''
## 47. Wap to extract all the vowels present in a string.
'''
n=input('Enter string : ')
i=0
while i<len(n):
    if n[i] in 'aeiouAEIOU':
        print(n[i],end='')
    i+=1
'''
## 48. Wap to print factors of a integer number.
'''
n=int(input('Enter number : '))
i=1
while i<=n:
    if n%i==0:
        print(i)
    i+=1
'''
## 49. Wap to toggle a string.
'''
n=input('Enter string : ')
i=0
while i<len(n):
    if 'a'<=n[i]<='z':
        print(chr(ord(n[i])-32),end='')
    elif 'A'<=n[i]<='Z':
        print(chr(ord(n[i])+32),end='')
    else:
        print(n[i],end='')
    i+=1
'''
## 50. Wap to reverse the given number.
'''
n=int(input('Enter number : '))
r=0
while n>0:
    r=r*10+n%10
    n//=10
print(r)
'''
## 51. Wap to find the sum of individual digits of a number.
'''
n=int(input('Enter a number : '))
s=0
while n>0:
    s+=n%10
    n//=10
print(s)
'''
## 52. Wap to check whether the number is perfect or not. 
'''
n=int(input('Enter a number : '))
i=1
s=0
while i<n:
    if n%i==0:
        s+=i
    i+=1
if s == n:
    print('perfect number.')
else:
    print('not perfect number')
'''   
## 53. Wap to login to phonepe by entering correct otp.
'''
i=3
while i>0:
    otp=input('Enter a OTP : ')
    if otp == '1234':
        print('OTP is correct ')
        break
    else:
        print('worng Otp ',i-1,' attenpets left')
    i-=1
'''
## 54. Wap to run infinite loop until user enters the correct password.
'''
while True:
    pwd=input('Enter the password : ')
    if pwd == 'abcd123':
        print('Correct Password.')
        break
    else:
        print('Wrong Password ')
'''
## 55. Wap to extaract all the even integers present in a tuple at odd index.
'''
n=eval(input('Enter Tuple : '))
i=0
while i<len(n):
    if i%2 != 0:
        if n[i]%2==0:
            print(n[i],end=',')
    i+=1
'''
## 56.Wap to remove duplicates from a list without converting into set.
'''
n=eval(input('Enter List : '))
i=0
l=[]
while i<len(n):
    if n[i] not in l:
        l.append(n[i])
    i+=1
print(l)
'''
## 57. Wap to find the sum of all the odd numbers between the given range.
'''
n=int(input('Enter starting number : '))
n1=int(input('Enter ending number : '))
while n<=n1:
    if n%2 != 0:
        print(n,end=' ')
    n+=1
'''
## 58. Wap to find the greatest number in a given list of integers.
'''
n=eval(input('Enter List : '))
i=0
g=0
while i<len(n):
    if n[i]>g:
        g=n[i]
    i+=1
print('Greatest number is ',g)
'''
## 59. Wap to find the sum of cube of a number in a string.
'''
n=input('Enter a string with numbers :  ')
num=0
s=0
i=0
while i<len(n):
    if '0'<=n[i]<='9':
        num=num*10+int(n[i])
    else:
        s+=num**3
        num=0
    i+=1
s+=num**3
print('sum of cube if num is ',s)
'''    
## 60. Wap to check whether the number is Armstrong or not.
'''
n=int(input('Enter number : '))
a,b=n,n
s,l=0,0
while n>0:
    l+=1
    n//=10
while a>0:
    s+=(a%10)**l
    a//=10
if s == b:
    print('Armstrong number.')
else:
    print('not Armstrong number.')
'''
## 61. Wap to get the following output.A='10011100' B='00110101' out=4(count of positions having same values)
'''
A='10011100'
B='00110101'
i,c=0,0
while i<len(A):
    if A[i]==B[i]:
        c+=1
    i+=1
print(c)
'''
## 62. Wap to check the given number is prime or not.
'''
n=int(input('Enter a number : '))
i,c=1,0
while i<=n:
    if n%i==0:
        c+=1
    i+=1
if c == 2:
    print('Prime number')
else:
    print('not a prime number.')
'''
## 63. Wap to check whether the number is palindrome or not.
'''
n=int(input('Enter a number : '))
p=0
while n>0:
    p=p*10+n%10
    n//=10
print(p)
'''
## 64. Wap to find the HCFand LCM of two numbers.
'''
a=int(input("Enter the Number1:"))
b=int(input("Enter the Number2:"))
if a>b:
    Lcm=a
    Hcf=b
else:
    Hcf=a
    Lcm=b
while True:
    if Lcm%a==0 and Lcm%b==0:
        print(f"LCM of {a} and {b} is {Lcm}")
        break
    Lcm+=1
while True:
    if a%Hcf==0 and b%Hcf==0:
        print(f"HCF of {a} and {b} is {Hcf}")
        break
    Hcf-=1
'''
## 65. Wap to convert binary to decinaml.
'''
n=int(input('Enter Binary number : '))
i=0
s=0
while n>0:
    s+=(n%10)(2*i)
    i+=1
    n//=10
print(s)

print(int(input('Enter binary number : '),2))
'''
## 66. Wap to convert decimal to binary.
'''
n=int(input('enter a number : '))
binary=''
r=0
while n>0:
    r=n%2
    binary = str(r) + binary
    n//=2
print(binary)
'''
## 67. Wap to count the number of words in a string.
'''
n=input('Enter a string : ')
count=0
if n != '':
    i=0
    while i<len(n):
        if n[i] != ' ':
            pass
        else:
            count+=1
        i+=1
    if n[-1] != ' ':
        count+=1
else:
    count=0
print(count)
'''
## 68. Wap to guess the number.
'''
import random
sn=random.randint(0,9)
print('='*30)
print(' '*7,'GUESSING A NUMBER')
print('='*30)
while True:
    n=int(input('Enter a number(0-9) : '))
    if n == sn:
        print(f'correct number.')
        break
    else:
        if n>sn:
            print(f'you guessing number smaller than {n} ')
        elif n<sn:
            print(f'you guessing number is greater than {n} ')
'''        
## 69. Wap to find the common elements in two sets
'''
s1 = eval(input("Enter first set : "))
s2 = eval(input("Enter second set : "))
list1 = list(s1)
list2 = list(s2)
i = 0
common = set()
while i < len(list1):
    j = 0
    while j < len(list2):
        if list1[i] == list2[j]:
            common.add(list1[i])
        j += 1
    i += 1
print("Common elements :", common)
'''
## 70. Wap to find the product of all the digits present in a number.
'''
n=int(input('Enter a number : '))
p=1
while n>0:
    p*=n%10
    n//=10
print(p)
'''
