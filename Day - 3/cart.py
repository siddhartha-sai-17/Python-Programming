def cart(n):
    l = [3, 5, 6, 7, 8, 9, 4]

    if n == 1:
        print("element to add")
        new_ele = int(input("Enter element: "))
        l.append(new_ele)
        print("Updated list:", l)

    elif n == 2:
        print("element to remove")
        remove_ele = int(input("Enter element to remove: "))
        if remove_ele in l:
            l.remove(remove_ele)
            print("Updated list:", l)
        else:
            print("Element not found in list")

    elif n == 3:
        print("element to search")
        search_ele = int(input("Enter element to search: "))
        if search_ele in l:
            print("Element found at index:", l.index(search_ele))
        else:
            print("Element not found")

    elif n == 4:
        print("Displaying all elements")
        for i in l:
            print(i, end=" ")
        print()
    elif n==5:
        print("elements in sorted order")
        l.sort()
        print(l)
    elif n==6:
        print("clearing the list")
        while l:
            l.remove(l[0])
        print(l)

    elif n==7:
        print("Total number of products:", len(l))
    else:
        print("exited from the cart")


# main program
n = int(input("Enter your choice (1-Add, 2-Remove, 3-Search, 4-Display,  5-Sort, 6-clear, 7-count): "))
cart(n)
