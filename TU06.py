JohnCenaHeight = 184
MyHeight =int(input(print("What is your height")))
HeightDifference = MyHeight - JohnCenaHeight
HeightDifference2 = JohnCenaHeight - MyHeight
if MyHeight > JohnCenaHeight:
    print("You are %d cm taller than JohnCenaHeight!" % HeightDifference)
    print("You are", HeightDifference, "cm taller than John Cena!")
if JohnCenaHeight > MyHeight:
    print("You are %d cm shorter than John Cena" % HeightDifference2)
    print("You are", HeightDifference2, "cm shorter than John Cena")