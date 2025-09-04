def factors(n):
    for i in range(1,n+1):
        if(n%i==0):
            print(i)
        else:
            i=i+1
n=int(input())
factors(n)