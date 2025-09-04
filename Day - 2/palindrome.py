def palindrome(n):
    original = n
    rev = 0
    while n > 0:
        rem = n % 10
        rev = rev * 10 + rem
        n = n // 10
    return rev == original

n = int(input())
if palindrome(n):
    print("Palindrome")
else:
    print("Not palindrome")