weight = float(input("What is your weight"))
height = float(input("What is your height in m"))

BMI = weight / height**2
print(BMI)

if BMI < 18.5:
    print("Bro head to mcdonalds have a big mac or 2 you're probably anorexic")

if BMI < 25 and BMI > 18.5:
    print("Ok, you're average but don't get fat or we will have an obesity problem and we don't need more of that")

if BMI < 30 and BMI > 25:
    print("Bro chill you're pretty fat lay off the big macs bro get a salad")

if BMI > 30:
    print("BRO HEAD TO THE HOSPITAL! BRO CHILL! CHILL!!! GET A DOCTOR! GET SOME OXYGEN BRO YOU HAVE TYPE 2 DIABETES")
