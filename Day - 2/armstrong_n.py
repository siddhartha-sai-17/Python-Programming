def arm(n):
    for num in range(1, n+1):
        temp = num
        sum = 0
        t = num
        while t > 0:
            rem = t % 10
            sum = sum + (rem ** 3)
            t = t // 10
        if sum == temp:
            print(temp)

n = int(input("Enter upper limit: "))
arm(n)