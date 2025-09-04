def notes(n):
    count100 = n // 100
    n = n % 100
    count50 = n // 50
    n = n % 50
    count20 = n // 20
    print("No of 100 notes:", count100)
    print("No of 50 notes:", count50)
    print("No of 20 notes:", count20)

n = int(input("Enter the amount: "))
notes(n)