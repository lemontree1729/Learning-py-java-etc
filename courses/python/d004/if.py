"""
if condition :
    code to run

a = 90 # variable declare
if a < 100:
    print(f"{a} is smaller than 100")
if ~ else statement: Used when we need to specify case for true and the other

if condition :
    code to run
else:
    code to run

a = 110 # variable declare
if a < 100 :
    print(f"{a} is smaller than 100")
else:
    print(f"{a} is same or bigger than 100")

    
# odd even
a = int(input("enter the number : "))
if a % 2:
    print("it is odd.")
else:
    print("it is even.")

# giving grade
score = int(input("enter the score : "))
temp = 100
ch = "ABCDF"
while temp > 60:
    temp -= 10
    if score >= temp:
        print(f"your grade is {ch[(90-temp)//10]}")
        break
else:
    print("your grade is F!!!!!!")
"""

# calculator
while not input("Continue : press Enter, Quit : enter anything: "):
    n1 = input("first number : ")
    op = input("operator : ")
    n2 = input("second number : ")
    print(f"{n1} {op} {n2} = {eval(n1+op+n2)}")
