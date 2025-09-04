def sum_d(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    print(total)

n = int(input())
sum_d(n)