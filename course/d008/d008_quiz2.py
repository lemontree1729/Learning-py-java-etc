# 21/10/15 quiz

gend = int(input("enter your gender <0 for man, 1 for woman> : "))
weight = int(input("enter your weigh(unit : [kg]) : "))
data = ((50, 85), (40, 68))
com = "you are "
word = ("underweight", "standard weight", "overweight")
for i in range(2):
    if weight < data[gend][i]:
        print(com + word[i])
        break
else:
    print(com + word[2])
