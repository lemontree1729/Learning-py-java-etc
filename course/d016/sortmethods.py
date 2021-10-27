from random import randint


def makeList(n):
    return [randint(0, 100) for i in range(n)]


def selectionSort(a):
    b = [i for i in a]
    for i in range(len(b)):
        temp = i
        for j in range(i + 1, len(b)):
            if b[temp] > b[j]:
                temp = j
        b[i], b[temp] = b[temp], b[i]
    return b


def insertionSort(a):
    b = [i for i in a]
    for i in range(1, len(b)):
        while i > 0:
            if b[i - 1] > b[i]:
                b[i - 1], b[i] = b[i], b[i - 1]
                i -= 1
            else:
                break
    return b


def bubbleSort(a):
    b = [i for i in a]
    temp = []
    while temp != b:
        temp = [i for i in b]
        for i in range(len(b) - 1):
            if b[i] > b[i + 1]:
                b[i + 1], b[i] = b[i], b[i + 1]
    return b


def mergeSort(a):
    b = [i for i in a]
    if len(b) <= 1:
        return b
    elif len(b) == 2:
        if b[0] > b[1]:
            b[0], b[1] = b[1], b[0]
        return b
    else:
        first = mergeSort(b[: len(b) // 2])
        last = mergeSort(b[len(b) // 2 :])
        result = []
        i, j = 0, 0
        while 1:
            if i == len(first) or j == len(last):
                result.extend(first[i:] + last[j:])
                break
            if first[i] < last[j]:
                result.append(first[i])
                i += 1
            else:
                result.append(last[j])
                j += 1
        return result


def quickSort(a):
    b = [i for i in a]
    if len(b) <= 1:
        return b
    else:
        rand = randint(0, len(b) - 1)
        i, j = 0, len(b) - 1
        while i != rand or j != rand:
            if i == rand:
                if b[rand] > b[j]:
                    rand = j
                    b[i], b[j] = b[j], b[i]
                    i += 1
                else:
                    j -= 1
            elif j == rand:
                if b[i] > b[rand]:
                    rand = i
                    b[i], b[j] = b[j], b[i]
                    j -= 1
                else:
                    i += 1
            else:
                if b[i] > b[rand]:
                    if b[rand] > b[j]:
                        b[i], b[j] = b[j], b[i]
                        i += 1
                    j -= 1
                else:
                    i += 1

        return quickSort(b[:rand]) + [b[rand]] + quickSort(b[rand + 1 :])


n = 15
a = makeList(n)
print(a)
print(selectionSort(a))
print(insertionSort(a))
print(bubbleSort(a))
print(mergeSort(a))
print(quickSort(a))
