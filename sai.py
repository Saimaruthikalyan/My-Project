# write a progrsm to check the given data belongs to which individual datatype
a=eval(input("enter the value:-"))
if type(a)==int:
    print(f"{a} is the integer datatype")
elif type(a)==float:
    print(f"{a} is the Float datatype")
elif type(a)==complex:
    print(f"{a} is the complex datatype")
elif type(a)==bool:
    print(f"{a} is the boolean datatype")
else:
    print(f"{a} is the collection datatype")
