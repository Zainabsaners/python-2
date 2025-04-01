Name=input("Enter your name: ")
children=input("Enter the number of children: ")
children=int (children)
salary=input("Enter your salary: ")
salary=int (salary)
print(f"Your name is {Name} and your salary is {salary}")

if salary<0:  
    print("Invalid salary") 
elif salary<=10000:
    tax=0.1*salary
    print(f"Your tax is {tax}")
elif salary>10000 and salary<=20000:
    tax=0.3*salary
    print(f"Your tax is {tax}")
elif salary>20000 and salary<=50000:
    tax=0.5*salary
    print(f"Your tax is {tax}")
elif salary>50000:
    tax=0.6*salary
    print(f"Your tax is {tax}")

netincome=salary-tax
print(f"Your net income is {netincome}")   
if children>3:
    netincome=netincome-10000*children
else:
    netincome=netincome
print(f"Your net income is {netincome}")
print(f"Hey {Name},your salary is{salary}, your tax is {tax} and your net income is {netincome}  ")
print("thank you for using the tax calculator")
print("Have a nice day!")
print("Please come back again")
print("Happy coding with kiongozi❤")

print("welcome back 😘")







