def fact(n):
    i=n
    fact = 1
    while i>0:
        fact = fact *i
        i=i-1
    print(fact)
n=int(input())
fact(n)