Choice = input("Choose a number!")

try:
    IntergerChecker = int(Choice)
    print("Your number is an interger!")
except ValueError:
    print("Your number is a float!")

