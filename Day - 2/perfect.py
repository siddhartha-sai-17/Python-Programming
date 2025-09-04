def perfect(n):
    temp=n
    sum = 0
    for i in range(1,n):
        if(n%i==0):
            sum = sum+i
        else:
            i=i+1
    if(temp==sum):
        print("perfect")
    else:
        print("not")
n=int(input())
perfect(n)