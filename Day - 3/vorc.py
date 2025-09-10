def s(p):
    count1=0
    count2=0
    for i in p:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            count1 +=1
        else:
            count2+=1
    print(count1)
    print(count2)
p =input()
s(p)