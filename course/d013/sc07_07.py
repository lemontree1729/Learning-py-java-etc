x0, y0 = 12, 4
list1 = [list(range(x0 * i, x0 * (i + 1))) for i in range(y0)]
for y in range(y0):
    for x in range(x0):
        print(f"list1[{y}][{x}] is {list1[y][x]}")
