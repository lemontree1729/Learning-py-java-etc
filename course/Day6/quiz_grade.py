while 1:
    try:
        score = int(input("enter the score : "))
    except:
        score = -1
    if not 0 <= score <= 100:
        print("Wrong score!")
        continue
    for i, j in enumerate("FDCBA"):
        if score < 60 + i * 10 or (i, score) == (4, 100):
            print("Your grade is", j)
            break
