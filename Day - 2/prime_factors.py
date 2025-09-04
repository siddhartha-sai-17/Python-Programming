def prime_factors(n):
    for i in range(2, n+1):
        if n % i == 0:
            # Check if i is prime
            is_prime = True
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    is_prime = False
                    break
            if is_prime:
                print(i)

n = int(input())
prime_factors(n)