# user_word = input("Enter the word: ")
# key = int(input("Enter KEY: "))
#
# length = len(user_word)
#
# result = ""
#
# for letter in user_word:
#     result += chr(ord(letter) + key)
#
#
# print(result)



user_word = input("Enter the word: ")
key = int(input("Enter KEY: "))
result = ""
for ch in user_word.lower():
    ordValue = ord(ch)
    cipherValue = ordValue + key
    if cipherValue == ord(" ") + key:
        cipherValue -= key
    elif cipherValue > ord('я'):
        cipherValue = ord('а') + key - (ord('я') - ordValue + 1)
    elif cipherValue > ord('z') and cipherValue < ord("а"):
         cipherValue = ord('a') + key - (ord('z') - ordValue + 1)


    result = result + chr(cipherValue)
print(result)
