def c():
    s = "hello world"
    for i in s:
        if s.__contains__("ll"):
            return True
        else:
            return False
a = c()
print(a)