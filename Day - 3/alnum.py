def c():
    s = "asd324*"
    count1 = 0
    count2 = 0
    count3 = 0
    for i in s : 
            if i>='0' and i<='9':
                count1 = count1+1
            elif i>='a'and i<='z':
                count2 +=1
            else:
                count3 +=1
    print("no of digits",count1)
    print("no of alphabets",count2)
    print("no of special characters" ,count3)
c()
