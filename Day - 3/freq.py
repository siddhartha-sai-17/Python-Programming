def freq():
    l = [5, 3, 4, 2, 1, 5, 4]
    for i in range(len(l)):
        count = 0
        for j in range(len(l)):
            if l[i] == l[j]:
                count += 1
        if l[i] not in l[:i]:
            print(l[i], "occurs", count, "times")
freq()
