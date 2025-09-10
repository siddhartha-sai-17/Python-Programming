def compress(a):
    result = ""
    visited = set()
    for ch in a:
        if ch not in visited:        
            count = a.count(ch)
            result += ch + str(count)
            visited.add(ch)
    return result

a = input("Enter a string: ")
print(compress(a))
