# 21/10/15 quiz

num = input("Enter a 5-digit number!!\n")
print(("{} + "*4 + "{} = {}").format(*num, sum(map(int, num))))
