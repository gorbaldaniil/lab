# user_word = input("Enter the word : ")
# length = len(user_word)
#
# for letter in user_word:
#     print(user_word[length-1], end='')
#     length -= 1
#

user_word = input("Enter the word : ")

inputWords = user_word.split(" ")
inputWords = inputWords[-1::-1]

result = ' '.join(inputWords)
result = result[::-1]

print(result)
