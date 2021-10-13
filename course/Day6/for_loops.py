# for Loops

""" What is for Loops?
type : syntax
how to use : //
for iterator_value_name in iterable:
   action code  <------ recommended to enter space bar for 4 times exactly 
//
input :
  - iterator_value_name : variable that you could use in each action code while looping
  - iterable : variable that make an iterator
  - action code : code that you want to loop
output :
  - loop of output of action code for each iterator value
"""

print("\n- example 1")
for i in [0, 1, 2]: # list is iterable
    print(i) # output will be 0 + "\n" + 1 + "\n" + 2 + "\n"

""" What is range?
type : iterable class
how to use : //
range(start: int, stop: int, step: int)
//
input : 
  - start : defaults 0, starting point of range
  - stop : no default value, ending point that is omitted
  - step : defaults 1, same as common difference
output :
  - range instance that can make int iterator
"""

print("\n- example 2")
# same as print(*range(3), sep = '\n')
for i in range(0, 3, 1): # range(3) is also possible
    print(i) # same output with example


print("\n- example 3, factorial")
fac = 1
for i in range(1, 11): # same as range(1, 11, 1)
    fac *= i # same as fac = i * fac
print(fac) # output is 10!

print("\n- example 4")
# same as print(sum(*range(500, 1001, 2)))
odd_sum = 0
for i in range(500, 1001):
    if i % 2:
        odd_sum += i
print("sum from 500 to 1000 which is odd :", odd_sum)

print("\n- example 5, sum of input start number and end number")
# same as print(sum(range(int(input("start number : ")), int(input("end number : ")), int(input("step number : ")))))
start = int(input("start number : ") or 1)
end = int(input("end number : ") or 1)
step = int(input("step number : ") or 1)
sum_input = 0
for i in range(start, end, step):
    sum_input += i
print(sum_input)

print("\n- example 6, Multiplication table")
multnum = input("multiple number : ") or range(1, 10)
for i in multnum:
    for j in range(1, 10):
        print(f"{int(i)} X {j} = {int(i)*j}")


