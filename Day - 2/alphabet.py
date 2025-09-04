def alpha(n):
    if n>='a' and n<='z' or n>='A' and n<='Z':
        print(n,"is an alphabet")
    elif n>='0' and n<='9':
        print("digit")
    else:
        print("special character")
n=input("Enter a character: ")
alpha(n)