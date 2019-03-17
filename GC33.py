MaleCalories = 10500
FemaleCalories = 8400

Gender = input("Are you a male or female, if you don't mind me asking? ")
if Gender in ("Male", "male", "Female", "female"):
    Name = input("What is your name, good sir? ")
    Eaten = input("What have you just eaten? ")
    Calories = input("How many calories was it? ")
else:
    print("Ok stay fat you gender neutral brat")

while Gender in ("Male", "male"):
    NewCalories = MaleCalories - Calories
    DayStatus = input("Are you done for the day?")
    if DayStatus == "y":
        print("You consumed", Eaten, "today which was", Calories, "calories")
    else:
        Eaten = input("What have you just eaten? ")
        Calories = input("How many calories was it? ")


