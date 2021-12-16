aa = []
bb = []
value = 0

for i in range(100):
    aa.append(value)
    value += 2
for i in range(100):
    bb.append(aa[99 - i])
print(f"bb[0] is {bb[0]}, bb[99] is {bb[99]}")
