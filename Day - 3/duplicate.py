def dup():
    l = [4,3,5,2,1,3,4,5]
    count = 0
    for x in l:
        c = 0
        for y in l:
            if x==y:
                c = c + 1
        if c>1:
            count = count + 1
    print(count/2)
dup()