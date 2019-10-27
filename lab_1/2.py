def caesarShift():
    cipherString = " "
    myString = input("What would you like to encrypt?")
    shiftAmount = int(input("What Shift Amount would you like it encrypted by?"))

    for c in myString:
        if c.isalpha():
            asciiValue = ord(c)
            asciiValue += shiftAmount
            if asciiValue > ord("z"):
                asciiValue -= 26
            if asciiValue < ord("a"):
                asciiValue += 26
            x = chr(asciiValue)
            cipherString += x

    print(cipherString)


if __name__ == "__main__":
    caesarShift()