from random import randint


def seq(a: list, b: int):  # case 1: using sequantial search
    for i in range(len(a)):
        if a[i] == b:
            return i
    else:
        return -1


def useindex(a: list, b: int):  # case 2 : using index function
    try:
        return a.index(b)
    except:
        return -1


def casting(a: list, b: int):  # case 3 : using in
    return b in set(a)  # can't find index exactly with set type
    """
    we could just code like "return b in a"
    but it is better changing type to set when we use "in" syntax many times
    """


while 1:
    a = [randint(0, 99) for i in range(10)]
    b = int(input("enter the number(0 ~ 99) : "))
    if seq(a, b) != -1:
        print("number is in list index of", seq(a, b))
    else:
        print("number is not in list(using seq)")

    if useindex(a, b) != -1:
        print("number is in list index of", useindex(a, b))
    else:
        print("number is not in list(using useindex)")

    if casting(a, b):
        print("number is in list")
    else:
        print("number is not in list(using casting)")
    print("list was", a)
    if int(input("Enter 0 to exit : ") or 1) == 0:
        break
