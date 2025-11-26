#=======================Word Pattern===============================
w = input("Enter the Message: ").upper()
n = int(input("Enter odd number of rows: "))

for i in range(1, n+1):   
    for a in w:           
        if a == "A":
            for j in range(1, n*2):
                if i+j==n+1 or j-i==n-1 or (i==(n//2)+1 and i+j>n+1 and i+j<n*2):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        elif a == "B":
            for j in range(1, n+1):
                if i==1 and j==n or i==(n//2)+1 and j==n or i==n and j==n:
                    print(" ", end=" ")
                elif j==1 or i==1 or i==n or j==n or(j==n and i<=(n//2)+1) or i==(n//2)+1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        elif a=="C":
            for j in range(1,n+1):
                if i==1 and j==1 or j==1 and i==n or i==n and j==n or i==1 and j==n:
                    print(" ",end=" ")
                elif j==1 or i==1 or i==n:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
        elif a=="D":
            for j in range(1,n+1):
                if i==1 and j==n or j==n and i==n:
                    print(" ",end=" ")
                elif i==1 or j==1 or i==n or j==n:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
        elif a=="E":
            for j in range(1,n+1):
                if (i==(n//2)+1 and j>=(n//2)+2)or i==1 and j==n or j==n and i==n:
                    print(" ",end=" ")
                elif i==1 or j==1 or i==n or i==(n//2)+1:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
        elif a=="F":
            for j in range(1,n+1):
                if (i==(n//2)+1 and j>=(n//2)+2):
                    print(" ",end=" ")
                elif i==1 or j==1 or i==(n//2)+1:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
        elif a=="G":
            for j in range(1,n+1):
                if (i==1 and j==1)or(i==n and j==1)or(i==n and j==n):
                    print(" ",end=" ")
                elif j==1 or i==n or i==1 or (j==n and i>=(n//2)+1)or(i==n//2+1 and j>=(n//2)+1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
        elif a=="H":
            for j in range(1,n+1):
                if j==1 or j==n or i==(n//2)+1: 
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
        elif a=="I":
            for j in range(1,n+1):
                if i==1 or i==n or j==(n//2)+1:
                    print("*",end=" ")
                else:
                    print(" ",end=' ')
        elif a=="J":
            for j in range(1,n+1):
                if i==n and j==(n//2)+1:
                    print(" ",end=' ')
                elif i==1 or j==(n//2)+1 or (i==n and j<=(n//2)+1):
                    print("*",end=" ")
                else:
                    print(" ",end=' ')
        elif a=="K":
            for j in range(1,n+1):
                if j==1 or i-j==(n//2) or i+j==(n//2)+2:
                    print("*",end=" ")
                else:
                    print(" ",end=' ')
        elif a=="L":
            for j in range(1,n+1):
                if j==1 or i==n:
                    print("*",end=" ")
                else:
                    print(" ",end=' ')
        elif a=="M":
            for j in range(1,n+1):
                if j==1 or j==n or(i==j and j<=(n//2)+1)or(i+j==n+1 and i<=(n//2)+1):
                    print("*",end=" ")
                else:
                    print(" ",end=' ')
        elif a=="N":
            for j in range(1,n+1):
                if j==1 or j==n or i==j:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
        elif a=="O":
            for j in range(1,n+1):
                if i==1 and j==1 or i==n and j==1 or i==1 and j==n or i==n and j==n:
                    print(" ",end=" ")
                elif i==1 or j==1 or i==n or j==n:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
        elif a=="P":
            for j in range(1, n+1):
                if i==1 and j==n or i==(n//2)+1 and j==n:
                    print(" ",end=" ")
                elif j==1 or i==1 or (j==n and i<=(n//2)+1) or i==(n//2)+1  :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
        elif a=="Q":
            for j in range(1,n+1):
                if j==2 and i==2 or i==2 and j==n-1 or i==n-1 and j==2:
                    print(" ",end=" ")
                elif j==n and i==n:
                    print("*",end=' ')
                elif i==1 or j==1 or i==n or j==n:
                    print("*",end=" ")
                elif i==2 or j==2 or i==n-1 or j==n-1 or (i==j and i>=(n//2)+1):
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
        elif a=="R":
            for j in range(1,n+1):
                if i==1 and j==n or i==(n//2)+1 and j==n:
                    print(" ",end=" ")
                elif j==1 or i==1 or (i==n//2+1)or(j==n and i<=n//2+1)or(i==j and i>n//2+1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
        elif a=="S":
            for j in range(1, n+1):
                if i==1 and j==1 or j==n and i==n or i==(n//2)+1 and j==1 or i==(n//2)+1 and j==n:
                    print(" ",end=" ")
                elif (i==1 or i==n or i==n//2+1)or(i< n//2 + 1 and j == 1)or(i > n//2 + 1 and j == n):
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
        elif a=="T":
            for j in range(1,n+1):
                if i==1 or j==(n//2)+1:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
        elif a=="U":
            for j in range(1,n+1):
                if i==n and j==1 or i==n and j==n:
                    print(" ",end=" ")
                elif j==1 or j==n or i==n:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
        elif a=="V":
            for j in range(1,n*2):
                if i==j or i+j==n*2:
                     print("*",end=" ")
                else:
                    print(" ",end=" ")
        elif a=="W":
            for j in range(1,n+1):
                if j==1 or j==n or(i==j and j>=(n//2)+1)or(i+j==n+1 and i>=(n//2)+1):
                    print("*",end=" ")
                else:
                    print(" ",end=' ')
        elif a=="X":
            for j in range(1,n+1):
                if i==j or i+j==n+1:
                    print("*",end=' ')
                else:
                    print(" ",end=" ")
        elif a=="Y":
            for j in range(1,n+1):
                if i==j and i<=(n//2)+1 or i+j==n+1 and i<=(n//2)+1 or j==(n//2)+1 and i>=(n//2)+1 :
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
        elif a=="Z":
            for j in range(1,n+1):
                if i==1 or i==n or i+j==n+1:
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
        print(" ", end="  ")  
    print()  
