
text = input()
key = 1
i = -1
result = ""

for num in text.split():

    if num.isdigit():
        num = str(int(num) + key)
        inputWords = text.split()
        inputWords[i] = num
        result += ''.join(num)
        result += ' '
        continue
    i += 1
    for letters in num:
        ordValue = ord(letters)
        cipherValue = ordValue + key
        if cipherValue == ord(" ") + key:
            cipherValue -= key
        elif cipherValue > ord("0") and cipherValue <= ord(":"):
            cipherValue = ordValue + key

        elif 97 <= ordValue <= 122:
            cipherValue = (ordValue - 97 + key)% 26 + 97 #eng

        elif 1072 <= ordValue <= 1103:
            cipherValue = (ordValue - 1072 + key)% 32 + 1072

        elif 1040 <= ordValue <= 1071:
            cipherValue = (ordValue - 1071 + 1)% 26 + 1071

        result += chr(cipherValue)
    result += ' '

print(result)