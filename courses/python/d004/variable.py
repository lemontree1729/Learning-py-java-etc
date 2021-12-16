"""
# string formatting
print('hello!')


a = (100,)*2
b = [100]*2
c = dict()
c[100] = 100
c[200] = 200

# % formatting(using exact printf in c language)
str1 = "%d and %d" % (100, 100)
print(str1, type(str1))
print("%d and %d" % a) # why works fine???
try:
    print("%d and %d" % str(a)) # not working
except:
    print("error")
try:
    print("%d and %d" % b) # not working
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

# casting
s1 = "100"  # '=' operator
print(int(s1) + 1)
print(float(s1) + 1)
