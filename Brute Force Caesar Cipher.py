Sentence = input("What do you want to cipher?")

NumberOfLetters = len(Sentence)

x = " "

for Shift in range(26):
    for i in range(NumberOfLetters):
        NumberConverted = ord(Sentence[i])
        NumberShifted = NumberConverted + Shift

        if NumberShifted > 90 and NumberShifted < 97:
            NumberShifted = NumberShifted - 26
        if NumberShifted > 122:
            NumberShifted = NumberShifted - 26
        if NumberConverted == 32:
            NumberShifted = NumberShifted - Shift

        LetterConverted = chr(NumberShifted)
        x = x + LetterConverted
    print(x)
    x = ""