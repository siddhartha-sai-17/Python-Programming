def words(n):
    words_list = []
    for i in n:
        if i == '1':
            words_list.append("one")
        elif i == '2':
            words_list.append("two")
        elif i == '3':
            words_list.append("three")
        elif i == '4':
            words_list.append("four")
        elif i == '5':
            words_list.append("five")
        elif i == '6':
            words_list.append("six")
        elif i == '7':
            words_list.append("seven")
        elif i == '8':
            words_list.append("eight")
        elif i == '9':
            words_list.append("nine")
        elif i == '0':
            words_list.append("zero")
    print(' '.join(words_list))

n = input()
words(n)