def unique(n):
    l = [4,5,3,4,5,6,1]
    p = []
    for i in range(0,len(l)):
        for j in range(1,len(l)):
            if l[i] != l[j]:
                p.append(l[i])
    print(p)
n = int(input())
unique(n)