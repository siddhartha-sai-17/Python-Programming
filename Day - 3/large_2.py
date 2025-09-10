def second_largest(numbers):
    unique_numbers = list(set(numbers))
    if len(unique_numbers) < 2:
        print("No second largest value")
    else:
        unique_numbers.sort(reverse=True)
        print("Second largest:", unique_numbers[1])

# Example usage:
numbers = [int(x) for x in input("Enter numbers separated by space: ").split()]
second_largest(numbers)