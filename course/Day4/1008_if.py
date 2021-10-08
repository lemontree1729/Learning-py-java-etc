# 조건문
"""
if 조건식 :
    실행할 문장

a = 90 # variable declare
if a < 100:
    print(f"{a} is smaller than 100")
if ~ else 문: 참일 때 실행하는 문장과 거짓일 떄 실행하는 문장이 다를 때 사용

if 조건식 :
    실행할 문장
else:
    실행할 문장
a = 110 # variable declare
if a < 100 :
    print(f"{a} is smaller than 100")
else:
    print(f"{a} is same or bigger than 100")

    
# 홀짝 판별기
a = int(input("enter the number : "))
if a % 2:
    print("it is odd.")
else:
    print("it is even.")

# 성적 판별기
score = int(input("enter the score : "))
temp = 100
ch = "ABCDF"
while temp > 60:
    temp -= 10
    if score >= temp:
        print(f"your score is {ch[(90-temp)//10]}")
        break
else:
    print("your score is F!!!!!!")
"""
        
# 계산기
while not input("Continue : press Enter, Quit : enter anything: "):
    n1 = input("first number : ")
    op = input("operator : ")
    n2 = input("second number : ")
    print(f"{n1} {op} {n2} = {eval(n1+op+n2)}")
