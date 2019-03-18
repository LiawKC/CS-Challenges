Vowels = "aeiouAEIOU"
Count = 0

Text = input("What is your text? ")

for i in Text:
    if i in Vowels: Count = Count+1

print(Count)