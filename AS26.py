Text = input("What is the text? ")
NumberOfWords = len(Text)

Letters = []

for i in range(NumberOfWords):
    Letter = Text[i]
    Letters.append(Letters)

NumberOfLetters = len(Letters)

AverageWordLength = NumberOfWords/NumberOfLetters
print("The average word length is", AverageWordLength)