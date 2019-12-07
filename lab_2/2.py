def number_of_letters(user_string):
    for letter in set(user_string):
        if letter.isalpha():
            x = user_string.count(letter)
            print(letter, "=", x)


def alfavit(user_string):
    result1 = []
    for word in user_string.split():
        if len(word)>2 and word.isalpha():
            if word not in result1:
                result1.append(word)
    userWords = result1
    userWords.sort()
    result = " ".join(userWords)
    print(result)


user_string = input("Enter: ")

enter = input("a or b")

if enter == "a":
    number_of_letters(user_string)
elif enter == "b":
    alfavit(user_string)