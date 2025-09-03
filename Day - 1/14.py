def val(n):
    if(n%5==0 and n%11==0):
        print("divisible")
    else:
        print("not divisible")
n = int(input())
val(n)