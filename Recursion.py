#--------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------Recursion----------------------------------------------------------------
#------------------------------------------------------------09-10-2025---------------------------------------------------------------
# recursion
'''
import sys
print(sys.getrecursionlimit()) #1000
sys.setrecursionlimit(4000)
print(sys.getrecursionlimit()) #4000
'''
# find factorial of a given number.
'''
def fun(n):
    if n==1 or n==0:
        return 1
    return fun(n-1)*n
print(fun(int(input("Enter the Number:"))))
'''
#--------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------10-10-2025---------------------------------------------------------------
# find the sum of first n natural numbers.
'''
n=int(input('Enter the Value:'))
i=1
s=0
while i<=n:
    s+=i
    i+=1
print(s)
print()
def fun(n,i=1,s=0):
    if i>n:
        return s
    return fun(n,i+1,s+i)
print(fun(int(input("Enter the Value:"))))
'''
# fid product of first n natural numbers.
'''
n=int(input('Enter the Value:'))
i=1
p=1
while i<=n:
    p*=i
    i+=1
print(p)
print()
def fun(n,i=1,p=1):
    if i>n:
        return p
    return fun(n,i+1,p*i)
print(fun(int(input("Enter the Value:"))))
'''
# count no of vowles from  a given string.
'''
def vcount(m,i=0,v=0):
    if i>=len(m):
        return f'Number of Vowels are {v}'
    if m[i]in"AEIOUaeiou":
        v+=1
    return vcount(m,i+1,v)
print(vcount(input("Enter the String:")))
'''
# count no of vowles and consonents from  a given string.
'''
def vcount(m,i=0,v=0,c=0):
    if i>=len(m):
        return f"Consonents {c} Vowels {v}"
    elif m[i]in"AEIOUaeiou":
        v+=1
    elif m[i]not in"AEIOUaeiou"and m[i].isalpha():
        c+=1
    return vcount(m,i+1,v,c)
print(vcount(input("Enter the String:")))
'''
# find LCM and HCF of given two numbers.
'''
a=int(input("Enter the Number1:"))
b=int(input("Enter the Number2:"))
i=0
l=max(a,b)
while True:
    if l%a==0 and l%b==0:
        print(f'LCM of The Number {a} and {b} is {l}')
        break
    l+=1
h=(a*b)//l
print(f'HCF of The Number {a} and {b} is {h}')
print()
'''
def LH(a,b,Lcm=1):
    if a<=0 and b<=0:
        return f"LCM is {Lcm} and HCF is {Hcf}"
    elif Lcm%a==0 and Lcm%b==0:
        Hcf=(a*b)//Lcm
        return f"LCM is {Lcm} and HCF is {Hcf}"
    return LH(a,b,Lcm+1)
print(LH(int(input("Enter the Number1:")),int(input("Enter the Number2:"))))
