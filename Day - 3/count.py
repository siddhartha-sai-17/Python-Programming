def c(n):
    l = [3,2,5,4,6]
    count1 = 0
    count2 = 0
    for i in l:
        if i%2==0:
            count1 = count1 + 1
        else:
            count2 = count2 + 1
    print(count1)
    print(count2)
n = int(input())
c(n)