def prime(n):
    i = 2
    count = 0
    while i <= n - 1:
        if n % i == 0:
            count = count + 1
            break
        i = i + 1
    if count == 0 and n > 1:
        print("prime")
    else:
        print("not prime")

n = int(input())
prime(n)