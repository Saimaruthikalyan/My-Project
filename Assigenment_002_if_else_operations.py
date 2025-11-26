##-------------------------------------------------------------------------
##------M.Sai Maruthi Kalyan ------8142356248 -----------------------------
##-------------------------------------------------------------------------
##                       if_else statements
##-------------------------------------------------------------------------
'''# 1. Check if a number is even or odd.
num=int(input("Enter The Number:"))
if num%2==0:
    print("The Number is a Even Number")
else:
    print("The Number is a odd Number")
# 2.Determine if a number is positive or negative.
num=int(input("Enter The Number:"))
if num>0:
    print("The Given Number is a Positive Number")
else:
    print("The Given Number is a Negative Number")
# 3.Check if a given year is a leap year or not.
year=int(input("Enter The Number:"))
if year%4==0:
    print("It is a Leap Year")
else:
    print("It is not a Leap Year")
# 4.Determine if a person is eligible to vote.
age=int(input("Enter The Age:"))
if age>=18:
    print("Congratulations You Are Eligible for Voting")
else:
    print("OOPs! You Are not Eligible for Voting")
# 5.Check if a string is a palindrome or not.
k=input("Enter The String:")
if k==k[::-1]:
    print("The Given Number is a Palindrome Number")
else:
    print("The Given Number is not a Palindrome Number")
# 6.Find the largest of two numbers.

a=int(input("Enter The Number1:"))
b=int(input("Enter The Number2:"))
if a>b:
    print(f"The Value {a} is Greater than The Value {b}")
else:
    print(f"The Value {b} is Greater than The Value {a}")
# 7.Check if a character is a vowel or consonant.
char=input("Enter The Character:")
if char in 'aeiouAEIOU':
    print("The Given Str is an Vowel")
else:
    print("The Given Str is an Consonant")
# 8.Determine if a number is divisible by 5.
num=int(input("Enter The Number:"))
if num%5==0:
    print("The Given Number is Divisible by 5")
else:
    print("The Given Number is not Divisible by 5")
# 9.Check if a number is in a given range.
num=int(input("Enter The Number:"))
if 0<num<=100:
    print("The Given Number is in the Range of 0 to 100")
else:
    print("The Given Number is not in the Range of 0 to 100")
# 10.Determine pass/fail based on score.
marks=int(input("Enter the Marks:"))
if marks>=35:
    print("Congratulatins 🤝 You Have Passed the Examination")
else:
    print("Sorry! ☹ You Have Fail the Examination")
# 11.Compare two strings for equality.
st1=input("Enter the String1:")
st2=input("Enter the String2:")
if st1==st2:
    print("Two Strings are the Equal")
else:
    print("Two Strings are not Equal")
# 12.Check if a number is multiple of both 3 and 5
num=int(input("Enter the Number:"))
if num%3==0 and num%5==0:
    print(f" The Number {num} is Multiples of Both 3 & 5")
else:
    print(f" The Number {num} is not Multiples of Both 3 & 5")
# 13.Determine if a person is eligible for senior citizen benefits.
age=int(input("Ehter the Age:"))
if age>59:
    print("You are Eligible for Senior Citizen Benefits")
else:
    print("You are not Eligible for Senior Citizen Benefits")'''
# 14. Check if a file path is valid.
path=input("Enter the File_path:")
if path != "":
    print("✅ The file path looks valid.")
else:
    print("❌ Invalid path: Path cannot be empty.")
