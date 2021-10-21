print("Enter nothing to exit")
num = []
while 1:
    a = input()
    if a == '':
        break
    num.append(int(a))

# case 1 : Using Built-in Function
print(max(num), min(num)) 

# case 2 : Using Sequential Search
maxnum = num[0]
minnum = num[0]
for i in num[1:]:
    if i > maxnum:
        maxnum = i
    if i < minnum:
        minnum = i
print(maxnum, minnum)

# case 3 : Using Bubble Sort
temp = []
while num != temp:
    temp = num
    for i in range(len(num) - 1):
        if num[i] > num[i+1]:
            num[i], num[i+1] = num[i+1], num[i]
print(num[-1], num[0])
