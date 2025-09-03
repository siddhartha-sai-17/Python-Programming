def leap(n):
    if(n%4==0):
        if(n%100==0):
            return n%400==0
        return True
    return False
n = int(input())
if(leap(n)):
    print("leap year")
else:
    print("not leap year")