def add (a,b):
    return a + b
def subtract(a,b):
    return a -b 
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
def modulus(a,b):
    return a % b
def exponent(a,b):
    return a ** b 
a=input("Enter a number: ")
a=int(a)
b=input("Enter another number: ")
b=int(b)



print(f"the sum is {add(a,b)}")
print(f"the difference is {subtract(a,b)}")
print(f"the product is {multiply(a,b)}") 
print(f"the quotient is {divide(a,b)}")
print(f"the modulus is {modulus(a,b)}")
print(f"the exponent is {exponent(a,b)}")
print("thank you for using the calculator")       