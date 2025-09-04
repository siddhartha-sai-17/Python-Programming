def arm(n):
    temp=n
    sum=0
    while n>0:
        rem = n%10
        sum  = sum + (rem* rem*rem)
        n=n//10
    if(sum==temp):
        print("armstrong")
    else:
        print("not")
n=int(input())
arm(n)