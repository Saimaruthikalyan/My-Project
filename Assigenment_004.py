##________________________________________Python Programming__________________________________________
##  Simple If:
# 1. Wap to print the square of a number only if it is even.
'''
a=int(input("Enter the Number:"))
if a%2:
    print(a**2)
'''
# 2. Wap to check whether the character is vowel or not.
'''
a=input("Enter the Character:")
if a in "AEIOUaeiou":
    print("It is the Vowel")
'''
# 3. Wap to print Ascii value of a character only if it is upper case.
'''
a=input("Enter the Character:")
if 'A'<=a<='z':
    print(ord(a))
'''    
# 4. Wap to print the cube of a number only if it is divisible by 9 or 6.
'''
a=int(input("Enter the Number:"))
if a%6==0 or a%9==0:
    print(a**3)
'''
# 5. Wap to check whether the given integer is 3 Digit number.
'''
a=int(input("Enter the NUmber:"))
if 100<=a<=99:
    print("The given number is a 3 Digit Number")
'''
# 6. Wap to check whether the last digit of a given number is 5.
'''
a=int(input("Enter the Number:"))
if a%10==5:
    print("Last Digit is 5")
'''
# 7. Wap to check whether the given data is float.
'''
a=eval(input("Enter the value:"))
if type(a)==float:
    print("The given Data is in A Float")
'''
# 8. Wap to check whether the data is single value data.
'''
a=eval(input("Enter The Value:"))
if type(a)in(int,float,complex,bool):
    print("The given value is in Single Value DataType")
'''
# 9. Wap to check whether the given character is digit or not.
'''
a=input("Enter the Character:"))
if '0'<=char<='9':
    print("The given Character is a Digit")
'''    
# 10. Wap to check whether the given integer is multiple of 3.
'''
a=int(input("Enter the Value:"))
if a%3==0:
    print("The given Integer is Multiple of 3")
'''
## If else:
# 11. Wap to check whether the data is mutable or not.
'''
a=eval(input("Entet the Data:"))
if type(a)in(list,set,dict):
    print("The Data is a Mutable")
else:
    print("The Data is Not a mutable")
'''
# 12. Wap to check whether the given character is digit or not.
'''
a=input("Enter the Character:"))
if '0'<=char<='9':
    print("The given Character is a Digit")
else:
    print("The given Character is Not a Digit")
'''
# 13. Wap to check whether the given character is special or not.
'''
a=input("Enter the Character:")
if 'a'<=a<='z' and 'A'<=a<='Z':
    print("The given Character is not a Special Character")
else:
    print("The given Character is a Special Character")
'''
# 14. Wap to check whether a list consists of middle value or not.
'''
a=eval(input("Enter the List:"))
if len(a)%2!=0:
    print("The Given List Consist of the Middle Value")
else:
    print("The Given list Doesen't Consist of Middle Value")
'''
# 15. Wap to check whether the number is even or odd.
'''
a=int(input("Enter the Number:"))
if a%2==0:
    print("The given number is the Even NUmber")
else:
    Print("The given number is the Odd Number")
'''
# 16. Wap to check whether the given data is mutable or immutable.
'''
a=eval(input("Entet the Data:"))
if type(a)in(list,set,dict):
    print("The Data is a Mutable")
else:
    print("The Data is an Immutable")
'''
# 17. Wap to check whether 2 values are pointing to the same memory or not.
'''
a=input("Enter the Value1:")
b=input("Enter the Value2:")
if a is b:
    print("The both values were pointing to same Memory")
else:
    print("The both values weren't pointing to same Memory")
'''
# 18 Consider a tuple of length 2 and check whether the tuple is homogenous or not.

# 19. Wap to check whether the string is palindrome or not.
# 20. Wap to check whether the number is positive or negative.
##  Elif:
# 21. Wap to check whether the char is uppercase, lowercase, digit or special char.
# 22. Wap to check whether the given integer is single digit or two digits or three digits or more than three digits.
# 23. Wap to check the given points are lying in which quadrant.
# 24. Wap to find the greatest of 3 numbers.
# 25. Wap to find the smallest of 3 numbers.
# 26. Wap to check the relation between two integer numbers.
# 27. Consider a character input if it is uppercase convert it into lowercase, if it is lowercase convert it into uppercase, if it is digit print the reminder when it is divided by 3 else if it is special character print it's ASCII value.
# 28. Wap to print 'Fizz' if the given number is multiple of three print "buzz" if the given number is multiple of 5 and print 'Fizzbuzz" if the number is multiple of both 3 and 5.
## Nested if:
# 29. Wap to login into the Instagram with valid username and password. (enter password only if the user name is valid)
# 30. Wap to print the middle value of a list only if it is string.
# 31. Wap to check whether the character is vowel or consonant.
# 32. Wap to find the greatest of 4 numbers.
# 33. Wap to print the value as it is only if the length of the value is even.
# 34. Wap to print the last value of a list only if it is palindrome string starting with vowel.
# 35. Wap to print the reversed string only if it is starting with vowel,ending with consonant and having a middle value.
# 36. Wap to find the second greatest of 4 values.
# 37. Wap to find the smallest of 4 numbers.
# 38. Write a program to print middle Character of the given string only if it is upper Case Character.
