#--------------------------------Pattern Programming--------------------------------------------
#------------------------------------22-09-2025-------------------------------------------------
# 1. print first 5 natural numbers in a single line.
'''
for i in range(1,5+1):
    print(i,end='')
'''
# 2. print first n natural numbers
'''
n=int(input("Enter the Number:"))
for i in range(1,n+1):
    print(i,end='')
'''
# 3. 11 12
#    21 22
'''
for i in range(1,3):
    for j in range(1,3):
        print(i,j,sep='',end=' ')
    print()
'''
# 3a. 11 12
#     21 22
'''
n=int(input("Enter the Number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,j,sep='',end=' ')
    print()
'''
# 4. 5 rows and 7 columns
'''
r=int(input("Enter the Number:"))
c=int(input("Enter the Number:"))
for i in range(1,r+1):
    for j in range(1,c+1):
        print(i,j,sep='',end=' ')
    print()
'''
# 4a. 5 rows and 7 columns
'''
for i in range(1,6):
    for j in range(1,8):
        print(i,j,sep='',end=' ')
    print()
'''
# 5. hallow pattern.
'''
n=int(input("Enter the Number of Rows and Columns:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print(i,j,sep='',end=' ')
        else:
            print("  ",sep='',end=' ')
    print()
'''
# 6. Star pattren.
#* * * * * * * * * * * * * * * 
#* + + + + + + + + + + + + + * 
#* + + + + + + + + + + + + + * 
#* + + + + + + + + + + + + + * 
#* + + + + + + + + + + + + + * 
#* + + + + + + + + + + + + + * 
#* + + + + + + + + + + + + + * 
#* + + + + + + + + + + + + + * 
#* + + + + + + + + + + + + + * 
#* + + + + + + + + + + + + + * 
#* + + + + + + + + + + + + + * 
#* + + + + + + + + + + + + + * 
#* + + + + + + + + + + + + + * 
#* + + + + + + + + + + + + + * 
#* * * * * * * * * * * * * * * 
'''
n=int(input("Enter the Number of Rows and Columns:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",sep='',end=' ')
        else:
            print("+",sep='',end=' ')
    print()
'''
# 7. hallow pattern
#2 3 4 5 6 
#3       7 
#4       8 
#5       9 
#6 7 8 9 10 
'''
n=int(input("Enter the Number of Rows and Columns:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print(i+j,sep='',end=' ')
        else:
            print(" ",sep='',end=' ')
    print()
'''
# 8. hallow pattern
#5 10 15 20 25 
#5          25 
#5          25 
#5          25 
#5 10 15 20 25 
'''
n=int(input("Enter the Number of Rows and Columns:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print(j*n,sep='',end=' ')
        else:
            print("  ",sep='',end=' ')
    print()
'''
# 9. pattern
#* * * * * 
#* *   * * 
#*   *   * 
#* *   * * 
#* * * * * 
'''
n=int(input("Enter the Number of Rows and Columns:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i==j or i+j==n+1:
            print("*",sep='',end=' ')
        else:
            print(" ",sep='',end=' ')
    print()
'''
# 10. pattern.
#* * * * * * * * * 
#* *     *     * * 
#*   *   *   *   * 
#*     * * *     * 
#*       *       * 
#*     * * *     * 
#*   *   *   *   * 
#* *     *     * * 
#* * * * * * * * *
'''
n=int(input("Enter the Number of Rows and Columns:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i==j or i+j==n+1 or j==(n//2)+1:
            print("*",sep='',end=' ')
        else:
            print(" ",sep='',end=' ')
    print()
'''
# 11. pattren.
#* * * * * * * * * 
#* *     *     * * 
#*   *   *   *   * 
#*     * * *     * 
#* * * * * * * * * 
#*     * * *     * 
#*   *   *   *   * 
#* *     *     * * 
#* * * * * * * * *
'''
n=int(input("Enter the Number of Rows and Columns:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i==j or i+j==n+1 or j==(n//2)+1 or i==(n//2)+1:
            print("*",sep='',end=' ')
        else:
            print(" ",sep='',end=' ')
    print()
'''
# 12. pattern.
#- - - - - - - - - 
#- - Y Y Y Y Y - - 
#- Y - Y Y Y - Y - 
#- Y Y - Y - Y Y - 
#- Y Y Y - Y Y Y - 
#- Y Y - Y - Y Y - 
#- Y - Y Y Y - Y - 
#- - Y Y Y Y Y - - 
#- - - - - - - - - 
'''
n=int(input("Enter the Number of Rows and Columns:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i==j or i+j==n+1 :
            print("-",sep='',end=' ')
        else:
            print("Y",sep='',end=' ')
    print()
'''
# 13. pattern.
#- - - - - - - - - 
#- - Y Y Y Y Y - - 
#- Y - Y Y Y - Y - 
#- Y Y - Y - Y Y - 
#- - - - - - - - - 
#- Y Y - Y - Y Y - 
#- Y - Y Y Y - Y - 
#- - Y Y Y Y Y - - 
#- - - - - - - - -
'''
n=int(input("Enter the Number of Rows and Columns:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i==j or i+j==n+1 or i==(n//2)+1:
            print("-",sep='',end=' ')
        else:
            print("Y",sep='',end=' ')
    print()
'''
# 14. pattern.
'''
                ~ ~ ~ ~ ~ ~ ~ ~ ~ 
                ~ ~ ? ? ~ ? ? ~ ~ 
                ~ ? ~ ? ~ ? ~ ? ~ 
                ~ ? ? ~ ~ ~ ? ? ~ 
                ~ ~ ~ ~ ~ ~ ~ ~ ~ 
                ~ ? ? ~ ~ ~ ? ? ~ 
                ~ ? ~ ? ~ ? ~ ? ~ 
                ~ ~ ? ? ~ ? ? ~ ~ 
                ~ ~ ~ ~ ~ ~ ~ ~ ~ 
n=int(input("Enter the Number of Rows and Columns:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n or i==j or i+j==n+1 or i==(n//2)+1 or j==(n//2)+1:
            print("~",sep='',end=' ')
        else:
            print("?",sep='',end=' ')
    print()

# 15. pattern.

* *                       * * 
* * * * * * * * * * * * * * * 
  * *                   * *   
  *   *               *   *   
  *     *           *     *   
  *       *       *       *   
  *         *   *         *   
  *           *           *   
  *         *   *         *   
  *       *       *       *   
  *     *           *     *   
  *   *               *   *   
  * *                   * *   
* * * * * * * * * * * * * * * 
* *                       * * 

n=int(input("Enter the Number of Rows and Columns:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==2 or i==n-1 or j==2 or j==n-1 or j==i or i+j==n+1:
            print("*",sep='',end=' ')
        else:
            print(" ",sep='',end=' ')
    print()
'''
#----------------------------------------------23-09-2025---------------------------------------------

# 1. pattern.
'''
                        *         
                        * *       
                        *   *     
                        *     *   
                        * * * * * 
                        * * * * * 
                          *     * 
                            *   * 
                              * * 
                                * 
n=int(input("Enter the Number of Rows and Columns:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or i==n or i==j:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==n or i==j:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
# 2. pattern.
'''
                                    * * * * * 
                                    *     *   
                                    *   *     
                                    * *       
                                    *         
                                            * 
                                          * * 
                                        *   * 
                                      *     * 
                                    * * * * * 
n=int(input("Enter the Number of Rows and Columns:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or i+j==n+1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n or j==n or i+j==n+1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
'''
# 3. pattern.
'''
                                        *         
                                        * *       
                                        *   *     
                                        *     *   
                                        * * * * * 

                                        * * * * * 
                                          *     * 
                                            *   * 
                                              * * 
                                                * 
                                        * * * * * 
                                        *     *   
                                        *   *     
                                        * *       
                                        *         

                                                * 
                                              * * 
                                            *   * 
                                          *     * 
                                        * * * * * 
n=int(input("Enter the Number of Rows and Columns:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or i==n or i==j:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==n or i==j:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or i+j==n+1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n or j==n or i+j==n+1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
print()
'''
# 4. pattern.
'''
                                        *         * * * * * 
                                        * *         *     * 
                                        *   *         *   * 
                                        *     *         * * 
                                        * * * * *         * 
                                        * * * * *         * 
                                        *     *         * * 
                                        *   *         *   * 
                                        * *         *     * 
                                        *         * * * * *
n=int(input("Enter the Number of Rows and Columns:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n or j==1 or i==j:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    for j in range(1,n+1):
        if i==1 or j==n or i==j:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or i+j==n+1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    for j in range(1,n+1):
        if i==n or j==n or i+j==n+1:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

'''
# 5. pattern.
'''
                                                        *                 
                                                        * *               
                                                        *   *             
                                                        *     *           
                                                        *       *         
                                                        *     *           
                                                        *   *             
                                                        * *               
                                                        *   
n = int(input("Enter the Number of Rows and Columns: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if j==1 or (i==j and i<=(n//2)+1)or (i+j==n+1 and j<(n//2)+1) :
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
'''
# 6. pattern.
'''
        * 
      * * 
    *   * 
      * * 
        *
n = int(input("Enter the Number of Rows and Columns: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if j==n or (i==j and j>=(n//2)+1)or (i+j==n+1 and i<(n//2)+1) :
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
'''
# 7. pattern.
'''
                                            *       * 
                                            * *   * * 
                                            *   *   * 
                                            * *   * * 
                                            *       * 
n = int(input("Enter the Number of Rows and Columns: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if j==1 or (i==j and i<=(n//2)+1)or (i+j==n+1 and j<(n//2)+1) or j==n or (i==j and j>=(n//2)+1)or (i+j==n+1 and i<(n//2)+1) :
            print("*", end=' ')
        else:
            print("-", end=' ')
    print()
'''
#---------------------------------------------------24-09-2025-----------------------------------------------------------

# 1. pattern hour glass.
'''
                                        * * * * * 
                                          *   *   
                                            *     
                                          *   *   
                                        * * * * *
n=int(input("Enter the Number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or i==j or i+j==n+1:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
'''
# 2. pattern.
'''
                                                *       * 
                                                * *   * * 
                                                * * * * * 
                                                * *   * * 
                                                *       * 
n = int(input("Enter the Number of Rows and Columns: "))
for i in range(1, n+1):
    for j in range(1, n+1):
        if(i>=j and i<=(n//2)+1) or(i<=j and i>=(n//2)+1):
            print("*", end=' ')
        elif(i+j<=n+1 and i>=(n//2)+1)or(i+j>=n+1 and i<(n//2)+1):
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
'''
# 3. pattern.
'''
                                                    * * * * * 
                                                    * * *   * 
                                                    * * * * * 
                                                    *   * * * 
                                                    * * * * *
n=int(input("Enter the Number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i<=(n//2)+1 and j<=(n//2)+1) or (i>=(n//2)+1 and j>=(n//2)+1) or i==1 or j==1 or i==n or j==n:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
'''
# 4. pattern.
'''
                            * * * * * 
                            *   * * * 
                            * * * * * 
                            * * *   * 
                            * * * * * 
n=int(input("Enter the Number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if (i>=(n//2)+1 and j<=(n//2)+1) or (i<=(n//2)+1 and j>=(n//2)+1) or i==1 or j==1 or i==n or j==n:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()
'''
# 5. pattern.
'''
                                *   * * * 
                                * * * *   
                                * * * * * 
                                  * * * * 
                                * * *   *
n = int(input("Enter odd number of rows:"))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i>=j and i<=n//2+1 or i+j<=n+1 and j>=n//2+1 or i+j>=n+1 and j<=n//2+1 or i<=j and i>=n//2+1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
# 6. reverse pattern.
'''
                                                            * * *   * 
                                                              * * * * 
                                                            * * * * * 
                                                            * * * *   
                                                            *   * * *
n = int(input("Enter odd number of rows:"))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i<=j and j<=(n//2)+1 or i+j>=(n+1) and i<=(n//2)+1 or i>=j and j>=(n//2)+1 or i+j<=n+1 and i>=(n//2)+1:
            print('*',end=' ')
        else:
            print(" ", end=" ")
    print()
'''
#------------------------------------25-09-2025-----------------------------------------

# 1. pattern.
'''

                                            *         * * * * * * 
                                            * *       * * * * *   
                                            * * * * * * * * *     
                                            * * * * * *   * *     
                                            * * *   * * * * *     
                                            * * * * * * * * * * * 
                                                * * * * *   * * * 
                                                * *   * * * * * * 
                                                * * * * * * * * * 
                                              * * * * *       * * 
                                            * * * * * *         *

                                         
n = int(input("Enter odd number of rows:"))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i>=j and i<=n//2+1 and j<=(n//4)+1 or i+j<=n+1 and j>=(n//2)+1 and i<=(n//4)+1 or i<=j and i>=(n//2)+1 and j>=((n//2)+1)+((n//4)+1) or i+j>=n+1 and j<=(n//2)+1 and i>=((n//2)+1)+((n//4)+1):
            print("*", end=" ")
        elif i<=j and j<=(n//2)+1 and i>=(n//4)+1 or i+j>=n+1 and i<=(n//2)+1 and j<=((n//2)+1)+((n//4)+1) or i>=j and j>=(n//2)+1 and i<=((n//2)+1)+((n//4)+1) or i+j<=n+1 and i>=(n//2)+1 and  j>=(n//4)+1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
# 2. python pattern.
'''
n = int(input("Enter odd number of rows:"))
for i in range(1, n+1):
    for j in range(1, n+1):
        if j==1 or i==1 or (j==n and i<=(n//2)+1) or i==(n//2)+1 or :
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
'''
#-------------------------------------------------26-09-2025-------------------------------------

# 1. python pattern.
'''
    * * * *   *       * * * * * * *       *   * * *   *       * 
    *       *   *   *       *     *       * *       * * *     * 
    * * * *       *         *     * * * * * *       * *   *   * 
    *             *         *     *       * *       * *     * * 
    *             *         *     *       *   * * *   *       * 
n = int(input("Enter odd number of rows:"))
for i in range(1, n+1):
    for j in range(1, n+1):
        if i==1 and j==n or i==(n//2)+1 and j==n:
            print(" ",end=" ")
        elif j==1 or i==1 or (j==n and i<=(n//2)+1) or i==(n//2)+1  :
            print("*",end=" ")
        else:
            print(" ",end=" ")#P
    for j in range(1,n+1):
        if i==j and i<=(n//2)+1 or i+j==n+1 and i<=(n//2)+1 or j==(n//2)+1 and i>=(n//2)+1 :
            print("*",end=" ")
        else:
            print(" ",end=" ")#Y
    for j in range(1,n+1):
        if i==1 or j==(n//2)+1:
            print("*",end=' ')
        else:
            print(" ",end=" ")#T
    for j in range(1,n+1):
        if j==1 or j==n or i==(n//2)+1: 
            print("*",end=' ')
        else:
            print(" ",end=" ")#H
    for j in  range(1,n+1):
        if i==1 and j==1 or i==n and j==1 or i==1 and j==n or i==n and j==n:
            print(" ",end=" ")
        elif i==1 or j==1 or i==n or j==n:
            print("*",end=' ')
        else:
            print(" ",end=" ")#O
    for j in range(1,n+1):
        if j==1 or j==n or i==j:
             print("*",end=' ')
        else:
            print(" ",end=" ")#N
    print()
'''
# 2. alphabet pattern.
'''
* * * *   
*       * 
* * * *   
*       * 
* * * * 
n = int(input("Enter odd number of rows:"))
for i in range(1, n+1):
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
    for j in range(1,n+1):
        if (i==(n//2)+1 and j>=(n//2)+2) :
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
        if j==1 or j==n or i==(n//2)+1: 
            print("*",end=' ')
        else:
            print(" ",end=" ")#H
    for j in range(1,n+1):
        if i==1 or i==n or j==(n//2)+1:
            print("*",end=" ")
        else:
            print(" ",end=' ')#I
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
        if i==1 and j==n or i==(n//2)+1 and j==n:
            print(" ",end=" ")
        elif j==1 or i==1 or (j==n and i<=(n//2)+1) or i==(n//2)+1 or i-j==n//2:
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
    for j in range(1,n+1):
        if j==1 or j==n or(i==j and j>=(n//2)+1)or(i+j==n+1 and i>=(n//2)+1):
            print("*",end=" ")
        else:
            print(" ",end=' ')#W
    print()
n = int(input("Enter odd number of rows:"))
for i in range(1, n+1):
    for j in range(1,n+1):
        if i==1 and j==n or i==(n//2)+1 and j==n:
            print(" ",end=" ")
        elif j==1 or i==1 or (i==n//2+1)or(j==n and i<=n//2+1)or(i==j and i>n//2+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")#R
    for j in range(1,n*2):
        if i+j==n+1 or j-i==n-1 or (i==(n//2)+1 and i+j>n+1 and i+j<n*2):
            print("*",end=" ")
        else:
            print(" ",end=" ")#A
    for j in range(1,n*2):
        if i==j or i+j==n*2:
             print("*",end=" ")
        else:
            print(" ",end=" ")#V
    for j in range(1,n+1):
        if (i==1 and j==1)or(i==n and j==1)or(i==n and j==n):
            print(" ",end=" ")
        elif j==1 or i==n or i==1 or (j==n and i>=(n//2)+1)or(i==n//2+1 and j>=(n//2)+1):
            print("*",end=" ")
        else:
            print(" ",end=" ")#G
    print()

'''
n=int(input("Enter the Number:"))
'''
                                        1             
                                        1 2           
                                        1 2 3         
                                        1 2 3 4       
                                        1 2 3 4 5     
                                        1 2 3 4 5 6   
                                        1 2 3 4 5 6 7 

for i in range(n+1):
    for j in range(n+1):
        if i>=j:
            print(j+1,end=' ')
        else:
            print(' ',end=' ')
    print()

                                        1 2 3 4 5 6 7   
                                        1 2 3 4 5 6     
                                        1 2 3 4 5       
                                        1 2 3 4         
                                        1 2 3           
                                        1 2             
                                        1  
for i in range(n+1):
    for j in range(n+1):
        if i+j<n:
            print(j+1,end=' ')
        else:
            print(' ',end=' ')
    print()

                                        *               
                                        * *             
                                        * * *           
                                        * * * *         
                                        * * * * *       
                                        * * * * * *     
                                        * * * * * * *   
                                        * * * * * * * *
for i in range(n+1):
    for j in range(n+1):
        if i>=j:
            print("*",end=' ')
        else:
            print(' ',end=' ')
    print()

                                        * * * * * * *   
                                        * * * * * *     
                                        * * * * *       
                                        * * * *         
                                        * * *           
                                        * *             
                                        * 
for i in range(n+1):
    for j in range(n+1):
        if i+j<n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

                                           1 
                                          1 2 
                                         1 2 3 
                                        1 2 3 4 
                                       1 2 3 4 5 
                                      1 2 3 4 5 6 
                                     1 2 3 4 5 6 7
for i in range(1,n+1):
    print(' '*(n-i),end=' ')
    for j in range(1,i):
        print(j,end=' ')
    print()
                                     1 2 3 4 5 6 7 
                                      1 2 3 4 5 6 
                                       1 2 3 4 5 
                                        1 2 3 4 
                                         1 2 3 
                                          1 2 
                                           1 
for i in range(n):
    print(' '*i,end=' ')
    for j in range(1,(n+1)-i):
        print(j,end=' ')
    print()

                                          * 
                                         * * 
                                        * * * 
                                       * * * * 
                                      * * * * * 
                                     * * * * * * 
for i in range(1,n+1):
    print(' '*(n-i),end=' ')
    for j in range(1,i):
        print('*',end=' ')
    print()

                                     * * * * * * * 
                                      * * * * * * 
                                       * * * * * 
                                        * * * * 
                                         * * * 
                                          * * 
                                           * 
for i in range(n):
    print(' '*i,end=' ')
    for j in range(1,(n+1)-i):
        print('*',end=' ')
    print()


                                                  1
                                                 12
                                                123
                                               1234
                                              12345
                                             123456
                                            1234567
for i in  range(1,(n+1)):
    print(' '*(n-i),end='')
    for j in range(1,i+1):
        print(j,end='')
    print()

                                        1234567
                                         123456
                                          12345
                                           1234
                                            123
                                             12
                                              1
for i in  range(n,0,-1):
    print(' '*(n-i),end='')
    for j in range(1,i+1):
        print(j,end='')
    print()

                                              *
                                             **
                                            ***
                                           ****
                                          *****
                                         ******
                                        *******
for i in  range(1,(n+1)):
    print(' '*(n-i),end='')
    for j in range(1,i+1):
        print('*',end='')
    print()

                                        *******
                                         ******
                                          *****
                                           ****
                                            ***
                                             **
                                              *
for i in  range(n,0,-1):
    print(' '*(n-i),end='')
    for j in range(1,i+1):
        print('*',end='')
    print()

                                               1 
                                              2 2 
                                             3 3 3 
                                            4 4 4 4 
                                           5 5 5 5 5 
                                          6 6 6 6 6 6 
                                         7 7 7 7 7 7 7
for i in range(1,n+1):
    print(' '*(n-i),end=' ')
    for j in range(1,i+1):
        print(i,end=' ')
    print()
                                              1
                                             22
                                            333
                                           4444
                                          55555
                                         666666
                                        7777777
for i in range(1,n+1):
    print(' '*(n-i),end='')
    for j in range(1,i+1):
        print(i,end='')
    print()
                                        12345678
                                        1234567
                                        123456
                                        12345
                                        1234
                                        123
                                        12
                                        1
                                        1
                                        12
                                        123
                                        1234
                                        12345
                                        123456
                                        1234567
for i in range(1,n*2):
    if i<=n:
        limit=n-i+1
    else:
        limit=i-n
    for j in range(1,limit+1):
        print(j,end='')
    print()
                                        1234567
                                         123456
                                          12345
                                           1234
                                            123
                                             12
                                              1
                                              1
                                             12
                                            123
                                           1234
                                          12345
                                         123456
for i in range(1,n*2):
    if i<=n:
        limit=n-i+1
        space=i-1
    else:
        limit=i-n
        space=(2*n-i)
    print(' '*space,end='')
    for j in range(1,limit+1):
        print(j,end='')
    print()
                                        *******
                                        ******
                                        *****
                                        ****
                                        ***
                                        **
                                        *
                                        *
                                        **
                                        ***
                                        ****
                                        *****
                                        ******
for i in range(1,n*2):
    if i<=n:
        limit=n-i+1
    else:
        limit=i-n
    for j in range(1,limit+1):
        print('*',end='')
    print()
                                        *******
                                         ******
                                          *****
                                           ****
                                            ***
                                             **
                                              *
                                              *
                                             **
                                            ***
                                           ****
                                          *****
                                         ******
for i in range(1,n*2):
    if i<=n:
        limit=n-i+1
        space=i-1
    else:
        limit=i-n
        space=(2*n-i)
    print(' '*space,end='')
    for j in range(1,limit+1):
        print('*',end='')
    print()
                                        ABCDEFG
                                        ABCDEF
                                        ABCDE
                                        ABCD
                                        ABC
                                        AB
                                        A
                                        A
                                        AB
                                        ABC
                                        ABCD
                                        ABCDE
                                        ABCDEF
for i in range(1,n*2):
    if i<=n:
        limit=n-i+1
    else:
        limit=i-n
    for j in range(limit):
        print(chr(65+j),end='')
    print()
                                        ABCDEFG
                                         ABCDEF
                                          ABCDE
                                           ABCD
                                            ABC
                                             AB
                                              A
                                              A
                                             AB
                                            ABC
                                           ABCD
                                          ABCDE
                                         ABCDEF
for i in range(1,n*2):
    if i<=n:
        limit=n-i+1
        space=i-1
    else:
        limit=i-n
        space=(2*n-i)
    print(' '*space,end='')
    for j in range(limit):
        print(chr(65+j),end='')
    print()
'''
