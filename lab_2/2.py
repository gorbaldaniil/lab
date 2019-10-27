def number_of_letters(user_string):
    result1 = []
    i=0
    b=""
    for letter in user_string:
        f = None
        x = letter
        for l in b:
            if x == l or x == " ":
                f = True
        if f != True:
            b += x
            for l in user_string:
                if x == l:
                    i += 1
            print(x,'=',i)
            i = 0
            f = None

    for word in user_string.split():
        if word not in result1:
            result1.append(word)

    userWords = result1
    userWords.sort()
    result = " ".join(userWords)

    print(result)


user_string = input("Enter: ")
number_of_letters(user_string)