def s(n):
    s1 = (587, "sid", 65)
    s2 = (543, "amar", 55)
    s3 = (598, "rak", 98)
    s4 = (587, "kcr", 87)
    s5 = (589, "nih", 89)

    # put all students in a list
    l = [s1, s2, s3, s4, s5]

    # find student with highest marks (index 2)
    top_student = max(l, key=lambda x: x[2])
    print("Student with highest marks:", top_student)

    # print students with marks > 75
    print("Students with marks > 75:")
    for student in l:
        if student[2] > 75:
            print(student)


n = int(input("Enter any number: "))
s(n)
