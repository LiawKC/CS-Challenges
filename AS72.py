alphabet = "abcdefghijklmnopqrstuvwxyz"
encryptedalphabet = "dnazegschbfmuxwjliktvropyq"
message = input("what message u want")
message2 = ''
messagelen = len(message)
for i in range(messagelen):
    if message[i] == " ":
        message2 = message2 + " "
    for a in range(26):
        if message[i] == alphabet[a]:
            message2 = message2 + encryptedalphabet[a]

print(message2)
