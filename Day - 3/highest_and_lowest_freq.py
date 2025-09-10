def a():
    s = input("Enter a string: ")
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    highest = max(freq, key=freq.get)
    lowest = min(freq, key=freq.get)

    print(f"Highest frequency: '{highest}' occurs {freq[highest]} times")
    print(f"Lowest frequency: '{lowest}' occurs {freq[lowest]} times")