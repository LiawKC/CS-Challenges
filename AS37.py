VowelList = ["a","e","i","o","u"]
NewWord = []
NewSentence = ""

Sentence = (input("Enter sentence: "))

Length = len(Sentence)

for i in range(Length):
    if Sentence[i] not in VowelList:
        NewWord = Sentence[i] + "o" + Sentence[i]
        NewSentence = NewSentence + NewWord
    if Sentence[i] in VowelList:
        NewSentence = NewSentence + Sentence[i]

print(NewSentence)