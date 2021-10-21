# 21/10/15 quiz

score = int(input("enter the score : "))
if score < 60:
    grade = "F"
elif score == 100:
    grade = "A+"
else:
    grade = chr(74 - score // 10) + "+"*(score % 10 not in range(5))
print("your grade is", grade)
