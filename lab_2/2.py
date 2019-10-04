def number_of_letters(user_string):
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


user_string = input("Enter: ")
number_of_letters(user_string)