# while Loops

""" What is while Loops?
type : syntax
how to use : //
while conditional bool:
    action code
//
input :
  - condition bool : boolean that has condition to stop
  - action code : code that you want to loop
output :
  - loop of output of action code until condition bool is true
"""

print("\n- example 1, Multiplication table")
i, j = 1, 1
while i < 10:
    j = 1
    while j < 10:
        print(f"{i} X {j} = {i*j}")
        j += 1
    i += 1

print("\n- example 2")
start = int(input("start number : ") or 0)
end = int(input("end number : ") or 0)
step = int(input("step number : ") or 1)
sum_input = 0
while start < end and end:
    sum_input += start
    start += step
print("sum :", sum_input)

print("\n- example 3, infinite loof")
print("you could stop this with ctrl+c")
num = 100
while num:
    print("★", num, sep = '', end = '')
    num -= 1
print()
    
# break Loop

""" What is break syntax?
type : syntax
how to use : //
loop syntax:
   action code
   break
   ignored code
//
input :
  - loop syntax : syntax that make loops. es)for ...: or while ...:
  - action code : code you want to loop until meets break
  - ignored code : code that will be ignored
output :
  - loop of output of only action code until interpreter meets break
"""

print("\n- example 4")
while True :
    a = int(input("first number : "))
    if a == 0:
        break
    b = int(input("second number : "))
    if b == 0:
        break
    print(f"{a} + {b} = {a+b}")
print("you just pressed 0")

# continue Loop

""" What is continue syntax?
type : syntax
how to use : //
loop syntax:
   action code
   continue
   ignored code
//
input :
  - loop syntax : syntax that make loops. es)for ...: or while ...:
  - action code : code you want to loop until meets break
  - ignored code : code that will be ignored
output :
  - loop of output of only action code until loop stops
"""

print("\n- example 5")
print("secret password : 8877")
while True :
    a = int(input("first number : "))
    if a == 8877:
        break
    elif a == 0:
        continue
    b = int(input("second number : "))
    if b == 0:
        continue
    print(f"{a} + {b} = {a+b}")
