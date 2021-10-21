# Function
"""
def plus():
    cal = input("first number : ")\
          + " " + input("operatorator(+, -, *, /) : ")\
          + " " + input("second number : ")
    print(f"{cal} = {eval(cal)}")

while 1:
    plus()
"""
"""
def func1():
    a = 10
    return a

def func2():
    print("value of a in func2", a)

func1()
func2()
"""
def func(*args):
    return sum(args)

a = []
print("Enter 0 to Exit!")
while 1:
    num = int(input("number : ") or 0)
    if num:
        a.append(num)
    else:
        break
print(func(*a))

def dic_func(**kwargs):
    for key in kwargs:
        print(f"{key}'s member number is {kwargs[key]}")

dic_func(a = 1, b = 2, c = 3)
