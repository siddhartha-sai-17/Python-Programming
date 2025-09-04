def tu(n):
    if n>=1 and n<=50:
         return n*3.8
    elif n>=51 and n<=100:
        return (50*3.8)+((n-50)*4.2)
    elif n>=101 and n<=200:
        return (50*3.8)+(100*4.2)+((n-100)*5.1)
    elif n>=201 and n<=300:
        return (50*3.8)+(100*4.2)+(200*5.1)+((n-200)*6.3)
    else:
        return (50*3.8)+(100*4.2)+(200*5.1)+(300*6.3)+((n-300)*7.5)
n=float(input())
print(tu(n))

    