def sun():
    l1=["ab@gmail","mn@gmail","xy@gmail","er@gmail"]
    l2=["ab@gmail","en@gmail","jk@gmail","ar@gmail"]
    l3=["ab@gmail","kl@gmail","xe@gmail","mn@gmail"]
    s1 = set(e.lower() for e in l1)
    s2 = set(e.lower() for e in l2)
    s3 = set(e.lower() for e in l3)
    print(len(s1|s2|s3))
    print(len(s1 & s2 & s3))
    print(len(s1-s2-s3 | s2 -s1-s3 | s3 - s2 -s1))
    print(s1&s2)
    print(s2&s3)
    print(s3&s1)
sun()