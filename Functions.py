#---------------------------------------------------------------------06-10-2025-----------------------------------------------------------------------------
'''class Kv:
    a=10
    b=20
    def __add__(self,other):
        return self.a+other.b
    def __sub__(self,other):
        print(self.a+other.b) 
        return self.a-other.b
ob=Kv()
og=Kv()
print(ob+og)
print(ob-og)
'''
#----------------------------------------------------------------------Functions-----------------------------------------------------------------------------
#----------------------------------------------------------------------string(str)---------------------------------------------------------------------------
# to see string function -> 'dir(str)'
# 1. "capitalize" # first letter will be capital
'''
a="Hello world"
print(a.capitalize())
'''
# 2. "casefold" # it will takes the lowercase
'''
a="Hello world"
print(a.casefold())
'''
# 3. "center" # make the string in the center
'''
a="Hello world"
print(a.center(20))
'''
# 4. "count"  # it will count the number of the perticular letter in the string
'''
a="Hello world"
print(a.count('l'))
'''
# 5. "encode" # it will add b to encode the str here b is the bytecode.
'''
a="Hello world"
print(a.encode())
'''
# 6. "endswith" # it will check the ending position which we provided in the string.
'''
a="Hello world"
print(a.endswith("d"))
'''
# 7. "startswith" # it will check the starting position which we provided in the string.
'''
a="Hello world"
print(a.startswith("H"))
'''
# 8. "find" # it will find the index value of the presented value if we have double character it will take the first repeated value.
'''
a="Hello world"
print(a.find("l"))
'''
# 9. "expandtabs" # it sets the tab size (default is 8 spaces).
'''
a = "Hello\tworld"
print(a.expandtabs(4))
'''
# 10. "format" # it is used to format strings with placeholders.
'''
a = "Hello world"
print("This is {}!".format(a))
'''
# 11. "format_map" # similar to format but takes a dictionary as input.
'''
a = "Hello world"
info = {'word': a}
print("Message: {word}".format_map(info))
'''
# 12. "index" # it returns the index of the given value, raises error if not found.
'''
a = "Hello world"
print(a.index("w"))
'''
# 13. "isalnum" # it checks if all characters are alphanumeric.
'''
a = "Hello world"
print(a.isalnum())  # False because of space
'''
# 14. "isalpha" # it checks if all characters are alphabets.
'''
a = "Hello world"
print(a.isalpha())  # False because of space
'''
# 15. "isascii" # it checks if all characters are ASCII characters.
'''
a = "Hello world"
print(a.isascii())
'''
# 16. "isdecimal" # it checks if all characters are decimals/
'''
a = "Hello world"
print(a.isdecimal())
'''
# 17. "isdigit" # it checks if all characters are digits.
'''
a = "Hello world"
print(a.isdigit())
'''
# 18. "isidentifier" # it checks if the string is a valid Python identifier.
'''
a = "Hello world"
print(a.isidentifier())
'''
# 19. "islower" # it checks if all characters are lowercase.
'''
a = "Hello world"
print(a.islower())
'''
# 20. "isnumeric" # it checks if all characters are numeric.
'''
a = "Hello world"
print(a.isnumeric())
'''
# 21. "isprintable" # it checks if all characters are printable.
'''
a = "Hello world"
print(a.isprintable())
'''
# 22. "isspace" # it checks if all characters are spaces.
'''
a = "Hello world"
print(a.isspace())
'''
# 23. "istitle" # it checks if the string follows title case.
'''
a = "Hello world"
print(a.istitle())
'''
# 24. "isupper" # it checks if all characters are uppercase.
'''
a = "Hello world"
print(a.isupper())
'''
# 25. "join" # it joins elements of a list into a single string.
'''
a = "Hello world"
print("-".join(a))
'''
# 26. "ljust" # it aligns string to the left with a specified width.
'''
a = "Hello world"
print(a.ljust(20, "*"))
'''
# 27. "lower" # it converts all characters to lowercase.
'''
a = "Hello world"
print(a.lower())
'''
# 28. "lstrip" # it removes spaces from the left side.
'''
a = "   Hello world"
print(a.lstrip())
'''
# 29. "maketrans" and "translate" # maketrans creates mapping table, translate replaces accordingly.
'''
a = "Hello world"
table = str.maketrans("H", "J")
print(a.translate(table))
'''
# 30. "partition" # it splits string into 3 parts based on separator.
'''
a = "Hello world"
print(a.partition(" "))
'''
# 31. "removeprefix" # it removes a specific prefix if present.
'''
a = "Hello world"
print(a.removeprefix("Hello"))
'''
# 32. "removesuffix" # it removes a specific suffix if present.
'''
a = "Hello world"
print(a.removesuffix("world"))
'''
# 33. "replace" # it replaces old substring with new substring
'''
a = "Hello world"
print(a.replace("world", "Python"))
'''
# 34. "rfind" # it finds the last occurrence index of substring
'''
a = "Hello world"
print(a.rfind("l"))
'''
# 35. "rindex" # it returns last occurrence index (error if not found)
'''
a = "Hello world"
print(a.rindex("l"))
'''
#36. "rjust" # it aligns string to right side with specified width
'''
a = "Hello world"
print(a.rjust(20, "*"))
'''
# 37. "rpartition" # it splits from the right side into 3 parts
'''
a = "Hello world"
print(a.rpartition(" "))
'''
#38. "rsplit" # it splits string from the right side
'''
a = "Hello world"
print(a.rsplit(" ", 1))
'''
# 39. "rstrip" # it removes spaces from the right side
'''
a = "Hello world   "
print(a.rstrip())
'''
# 40. "split" # it splits the string into a list
'''
a = "Hello world"
print(a.split())
'''
# 41. "splitlines" # it splits the string by line breaks
'''
a = "Hello\nworld"
print(a.splitlines())
'''
# 42. "strip" # it removes spaces from both sides
'''
a = "   Hello world   "
print(a.strip())
'''
# 43. "swapcase" # it swaps lowercase to uppercase and vice versa
'''
a = "Hello world"
print(a.swapcase())
'''
# 44. "title" # it capitalizes the first letter of each word
'''
a = "Hello world"
print(a.title())
'''
# 45. "upper" # it converts all characters to uppercase
'''
a = "Hello world"
print(a.upper())
'''
# 46. "zfill" # it fills the string with zeros at the beginning
'''
a = "Hello world"
print(a.zfill(15))
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------List[list]--------------------------------------------------------------------------
# 1. "append" # it adds an element to the end of the list.
'''
a = [1, 2, 3, 4]
a.append(5)
print(a)
'''
# 2. "clear" # it removes all elements from the list.
'''
a = [1, 2, 3, 4]
a.clear()
print(a)
'''
# 3. "copy" # it returns a shallow copy of the list.
'''
a = [1, 2, 3, 4]
b = a.copy()
print(b)
'''
# 4. "count" # it returns the number of times a value appears in the list.
'''
a = [1, 2, 3, 2, 4, 2]
print(a.count(2))
'''
# 5. "extend" # it adds all elements of another list to the end of the current list.
'''
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)
print(a)
'''
# 6. "index" # it returns the index of the first occurrence of a value.
'''
a = [10, 20, 30, 40, 50]
print(a.index(30))
'''
# 7. "insert" # it inserts an element at a specific position.
'''
a = [10, 20, 30, 40]
a.insert(2, 25)
print(a)
'''
# 8. "pop" # it removes and returns the element at a given index (last by default).
'''
a = [10, 20, 30, 40]
a.pop()
print(a)
'''
# 9. "remove" # it removes the first occurrence of a specified value.
'''
a = [10, 20, 30, 20, 40]
a.remove(20)
print(a)
'''
# 10. "reverse" # it reverses the list order.
'''
a = [1, 2, 3, 4]
a.reverse()
print(a)
'''
# 11. "sort" # it sorts the list in ascending order by default.
'''
a = [5, 3, 1, 4, 2]
a.sort()
print(a)
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------Tuple(tuple)--------------------------------------------------------------------------
# 1. "count" # it returns the number of times a specified value appears in the tuple
'''
a = (10, 20, 30, 20, 40, 20)
print(a.count(20))
'''
# 2. "index" # it returns the index of the first occurrence of a specified value
'''
a = (10, 20, 30, 40, 50)
print(a.index(30))
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------User-Defined Functions------------------------------------------------------------------
# 1. addition of 2 numbers.
# without return and argument.
'''
def addd():
    a=int(input("Enter the Number1:"))
    b=int(input("Enter the Number2:"))
    print(a+b)
addd()
'''
# without return and with arguments.
'''
def addd(a,b):
    print(a+b)
addd(int(input("Enter the Number1:")),int(input("Enter the Number2:")))
'''
# with return and without argument.
'''
def addd():
    a=int(input("Enter the Number1:"))
    b=int(input("Enter the Number2:"))
    return a+b
print(addd())
'''
# with return and without argument.
'''
def addd(a,b):
    return a+b
print(addd(int(input("Enter the Number1:")),int(input("Enter the Number2:"))))
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------Types of Arguments------------------------------------------------------------------------
# types of arguments.
'''
def addd(a,b): #parameters or formal arguments
    print(a)
    print(b)
    print(a+b)
addd(int(input("Enter the Number1:")),int(input("Enter the Number2:"))) #arguments or actual arguments
'''
# types of formal arguments.
# 1. default arguments
'''
def addd(a,b): #parameters or formal arguments
    print(b)
    print(a)
    print(a+b)
addd(int(input("Enter the Number1:")),int(input("Enter the Number2:"))) #arguments or actual arguments
'''
'''
def addd(firstn=[1,2,3],lastn='python'): #parameters or formal arguments
    print(firstn,lastn)
addd('python 2') #arguments or actual arguments
addd('python 2','programing')
'''
# 2. positional arguments.
'''
def student(name,age):
    print(name)
    print(age)
student(60,'hari')
'''
# 3. keyword arguments.
'''
def student(name,age,loc):
    print(name)
    print(age)
    print(locals)
student(age=60,name='hari',loc='btm')
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------Types of Variables-----------------------------------------------------------------------
# Global Variables:-
'''
a="This is the Global Variable"
def fun():
    a="I am Present inside the function"
    print(a)
fun()
print(a)
'''
#------------------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------08-10-2025--------------------------------------------------------------------------------
# Local variables:-
'''
413def Q():
    global name,loc
    loc='kurnool'
    name='kumar'
    print(name)
    print(loc)
Q()
print(name,loc)
'''
# Non-Local Variables:-
'''
def Q():
    loc='kurnool'
    name='kumar'
    con=102589632147
    def Py():
        nonlocal con
        con=9874563210
        print(name,loc,con)
    Py()
    print(name,loc,con)
Q()
'''
# Packing and Unpacking
# Packing:-
# Tuple Packing
'''
def fun(*a):
    print(a)
    print(a[1])
fun(10,20,'kalybh',500)
'''
# Dictionary Packing
'''
def fun(**a):
    print(a)
fun(name='Rama',loc='Kurnool',age=25)
'''
# combination of tuple and dictionay packing.
'''
def fun(*a,**b):
    print(a)
    print(b)
fun(10,20,'kalybh',500,name='Rama',loc='Kurnool',age=25)
'''
# print only the integer from a given values.
'''
def fun(*a):
    for i in a:
        if type(i)==int:
            print(i)
fun(10,20,60,'kaddv')
'''
# from given variables and values print only the values which are SVDT.
'''
def fun(**a):
    for i in a:
        if type(a[i])in(int,float,bool,complex):
            print(a[i])
fun(a=10,b='20',c=300,d=30.8,e=True,f=3+33j)
'''
# from a given characters,print only the vowels.
'''
def fun(*a):
    for i in a:
        if i in"AEIOUaeiou":
            print(i)
fun('k','a','l','y','a','n','r','e','v','i')
'''
# from a given characters,print only the consonents.
'''
def fun(*a):
    for i in a:
        if i not in"AEIOUaeiou"and i.isalpha():
            print(i)
fun('k','a','l','y','a','n','r','e','v','i','1','12')
'''
# find the sum of all the ASCII value from the given character.
'''
def fun(*a):
    s=0
    for i in a:
        s+=ord(i)
    print(s)
fun('k','a','l','y','a','n','r','e','v','i')
'''
# from a given variable and values reverse values with variable.
'''
def fun(**a):
    d={}
    for i in range(len(a)):
        for i in a:
            d[a[i]]=i
    print(d)
fun(a=10, b='20', c=300, d=30.8, e=True, f=3+33j)
'''
#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------unpacking---------------------------------------------------------------
# from a given character,print only the vowels.
'''
def fun(*a):
    print(a)
    print(len(a))
fun(*([10,20,30],'zabernesa',565,['afaefc',['acae']],2518,657894,'ajoaee'))
'''
#
'''
def fun(*a):
    print(a)
    print(len(a))
fun((10,'zabernesa',565,*['afaefc',['acae']],2518,657894,'ajoaee'))
'''
# print all the values from a given collection as individual values.also print all SVDT.
'''
def fun(*a):
    for i in a:
        if type(i)in(list,tuple,set,dict):
            for j in i:
                print(j)
        else:
            print(i)
fun(*eval(input("Enter the Values:")))
'''
