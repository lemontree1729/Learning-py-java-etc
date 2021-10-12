# 20211006 python new four arithmetic operations calculator
# calculate four arithmetic operations for two values
# until user press something else with '0'


def cal():
    a = []
    for i in range(1, 3):
        a.append(int(input('enter the value'+str(i)+' : ')))
    for j in (' + ', ' - ', ' * ', ' / '):
        b = str(a[0]) + j + str(a[1])
        print(b, '=', eval(b))
    c = input('enter 0 to continue : ')
    if c == '0':
        cal()


cal()
