user_string = input("Enter: ")

userWords = user_string.split(" ")
userWords.sort()
result = " ".join(userWords)

print(result)