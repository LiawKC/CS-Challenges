MaleCalories = 10500
FemaleCalories = 8400

FoodEaten = []
CaloriesConsumed = []

Gender = input("Are you a male or female, if you don't mind me asking? ")
if Gender in ("Male", "male", "Female", "female"):
    Name = input("What is your name, good sir? ")
    Eaten = input("What have you just eaten? ")
    FoodEaten.append(Eaten)
    Calories = int(input("How many calories was it? "))
    CaloriesConsumed.append(Calories)

else:
    print("Ok stay fat you gender neutral brat")

FoodEatenNumber = len(FoodEaten)

if Gender in ("Male", "male"):
    NewCalories = MaleCalories - Calories
    DayStatus = input("Are you done for the day?")

    if DayStatus == "y":
        for i in range(FoodEatenNumber):
            print("You consumed", FoodEaten[i], "today which was", CaloriesConsumed[i], "calories")

    else:
        Eaten1 = input("What have you just eaten? ")
        FoodEaten.append(Eaten1)
        Calories = int(input("How many calories was it? "))
        CaloriesConsumed.append(Calories)
        NewCalories = MaleCalories - Calories
        DayStatus = input("Are you done for the day?")



