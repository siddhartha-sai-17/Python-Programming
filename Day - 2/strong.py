def fact(rem):
    fact = 1
    i = 1
    while i <= rem:
        fact = fact * i
        i = i + 1
    return fact

def strong(n):
    original = n
    sum = 0
    while n > 0:
        rem = n % 10
        sum = sum + fact(rem)
        n = n // 10
    if sum == original:
        print("strong")
    else:
        print("not strong")

n = int(input())
strong(n)