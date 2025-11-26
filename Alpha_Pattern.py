#=======================Alphabet PAttern===============================
n = int(input("Enter odd number of rows:"))
for i in range(1, n+1):
    for j in range(1,n*2):
        if i+j==n+1 or j-i==n-1 or (i==(n//2)+1 and i+j>n+1 and i+j<n*2):
            print("*",end=" ")
        else:
            print(" ",end=" ")#A
    for j in range(1, n+1):
        if i==1 and j==n or i==(n//2)+1 and j==n or i==n and j==n:
            print(" ",end=" ")
        elif j==1 or i==1 or i==n or j==n or(j==n and i<=(n//2)+1) or i==(n//2)+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")#B
    for j in range(1,n+1):
        if i==1 and j==1 or j==1 and i==n or i==n and j==n or i==1 and j==n:
            print(" ",end=" ")
        elif j==1 or i==1 or i==n:
            print("*",end=' ')
        else:
            print(" ",end=" ")#C
    for j in range(1,n+1):
        if i==1 and j==n or j==n and i==n:
            print(" ",end=" ")
        elif i==1 or j==1 or i==n or j==n:
             print("*",end=' ')
        else:
            print(" ",end=" ")#D
    print()
print()
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i==(n//2)+1 and j>=(n//2)+2)or i==1 and j==n or j==n and i==n:
            print(" ",end=" ")
        elif i==1 or j==1 or i==n or i==(n//2)+1:
             print("*",end=' ')
        else:
            print(" ",end=" ")#E
    for j in range(1,n+1):
        if (i==(n//2)+1 and j>=(n//2)+2):
            print(" ",end=" ")
        elif i==1 or j==1 or i==(n//2)+1:
            print("*",end=' ')
        else:
            print(" ",end=" ")#F
    for j in range(1,n+1):
        if (i==1 and j==1)or(i==n and j==1)or(i==n and j==n):
            print(" ",end=" ")
        elif j==1 or i==n or i==1 or (j==n and i>=(n//2)+1)or(i==n//2+1 and j>=(n//2)+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")#G
    for j in range(1,n+1):
        if j==1 or j==n or i==(n//2)+1: 
            print("*",end=' ')
        else:
            print(" ",end=" ")#H
    for j in range(1,n+1):
        if i==1 or i==n or j==(n//2)+1:
            print("*",end=" ")
        else:
            print(" ",end=' ')#I
    print()
print()
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n and j==(n//2)+1:
            print(" ",end=' ')
        elif i==1 or j==(n//2)+1 or (i==n and j<=(n//2)+1):
            print("*",end=" ")
        else:
            print(" ",end=' ')#J
    for j in range(1,n+1):
        if j==1 or i-j==(n//2) or i+j==(n//2)+2:
            print("*",end=" ")
        else:
            print(" ",end=' ')#K
    for j in range(1,n+1):
        if j==1 or i==n:
            print("*",end=" ")
        else:
            print(" ",end=' ')#L
    for j in range(1,n+1):
        if j==1 or j==n or(i==j and j<=(n//2)+1)or(i+j==n+1 and i<=(n//2)+1):
            print("*",end=" ")
        else:
            print(" ",end=' ')#M
    for j in range(1,n+1):
        if j==1 or j==n or i==j:
             print("*",end=' ')
        else:
            print(" ",end=" ")#N
    print()
print()
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 and j==1 or i==n and j==1 or i==1 and j==n or i==n and j==n:
            print(" ",end=" ")
        elif i==1 or j==1 or i==n or j==n:
            print("*",end=' ')
        else:
            print(" ",end=" ")#O
    for j in range(1, n+1):
        if i==1 and j==n or i==(n//2)+1 and j==n:
            print(" ",end=" ")
        elif j==1 or i==1 or (j==n and i<=(n//2)+1) or i==(n//2)+1  :
            print("*",end=" ")
        else:
            print(" ",end=" ")#P
    for j in range(1,n+1):
        if j==2 and i==2 or i==2 and j==n-1 or i==n-1 and j==2:
            print(" ",end=" ")
        elif j==n and i==n:
            print("*",end=' ')
        elif i==1 or j==1 or i==n or j==n:
            print(" ",end=" ")
        elif i==2 or j==2 or i==n-1 or j==n-1 or (i==j and i>=(n//2)+1):
            print("*",end=' ')
        else:
            print(" ",end=" ")#Q
    for j in range(1,n+1):
        if i==1 and j==n or i==(n//2)+1 and j==n:
            print(" ",end=" ")
        elif j==1 or i==1 or (i==n//2+1)or(j==n and i<=n//2+1)or(i==j and i>n//2+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")#R
    for j in range(1, n+1):
        if i==1 and j==1 or j==n and i==n or i==(n//2)+1 and j==1 or i==(n//2)+1 and j==n:
            print(" ",end=" ")
        elif (i==1 or i==n or i==n//2+1)or(i< n//2 + 1 and j == 1)or(i > n//2 + 1 and j == n):
            print("*", end=" ")
        else:
            print(" ", end=" ")#S
    print()
print()
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==(n//2)+1:
            print("*",end=' ')
        else:
            print(" ",end=" ")#T
    for j in range(1,n+1):
        if i==n and j==1 or i==n and j==n:
            print(" ",end=" ")
        elif j==1 or j==n or i==n:
            print("*",end=' ')
        else:
            print(" ",end=" ")#U
    for j in range(1,n*2):
        if i==j or i+j==n*2:
             print("*",end=" ")
        else:
            print(" ",end=" ")#V
    for j in range(1,n+1):
        if j==1 or j==n or(i==j and j>=(n//2)+1)or(i+j==n+1 and i>=(n//2)+1):
            print("*",end=" ")
        else:
            print(" ",end=' ')#W
    print()
print()
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            print("*",end=' ')
        else:
            print(" ",end=" ")#X
    
    for j in range(1,n+1):
        if i==j and i<=(n//2)+1 or i+j==n+1 and i<=(n//2)+1 or j==(n//2)+1 and i>=(n//2)+1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")#Y
    for j in range(1,n+1):
        if i==1 or i==n or i+j==n+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")#Z
    print()
