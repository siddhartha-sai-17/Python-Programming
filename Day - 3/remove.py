def r(n):
    my_list = [3, 2, 5, 4, 6]
    if n in my_list:
        my_list.remove(n)
    print(my_list)

n = int(input("Enter number to remove: "))
r(n)