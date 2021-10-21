#1008
#프린트 서식
#문자열

"""
# 3-1, 서식 출력 연습
print('안녕하세요.')


a = (100,)*2
b = [100]*2
c = dict()
c[100] = 100
c[200] = 200

# % formatting(c언어에서 printf 함수를 가져온듯?)
# type() 함수 확인해보기(이 함수 안에 type을 구별하는 방식이 있을수도)
str1 = "%d and %d" % (100, 100)
print(str1, type(str1))
print("%d and %d" % a) # 잘 작동함(why???)
try:
    print("%d and %d" % str(a)) #작동하지 않음
except:
    print("error")
try:
    print("%d and %d" % b) # 작동하지 않음
except:
    print("error")
    

# formatting using format function
str2 = "{} and {}".format(100, 100)
print(str2, type(str2))
print("{} and {}".format(*a))
print("{} and {}".format(*b))
print("{} and {} and {}".format(a, b, c))


# formatting using f string(can use over python 3.6 version)
str3 = f"{100} and {100}"
print(str3, type(str3))
str5 = f"{a[0]} and " + "a[1]" # act like r"\\n"+"\n"
print(str5)
print(f"{a} and {b} and {c}")
"""

# 3-2, 형 변환 연습
s1 = "100" # '=' operator
print(int(s1)+1)
print(float(s1)+1)
