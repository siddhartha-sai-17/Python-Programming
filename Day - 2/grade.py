def grade(n):
    if n>=40:
        print("pass")
        if n<50:
            print("Grade C")
        elif n>50 and n<70:
            print("Grade B")
        elif n>70 and n<80:
            print("Grade A")
        elif n>80:
            print("Grade Distension")
    else:
        print("Fail")
n = int(input())
grade(n)