Money = int(input("How much money do you have Pooja? "))
WithdrawalMoney = int(input("How much money do you want to withdraw Pooja? "))

if WithdrawalMoney % 5 == 0:
        Money = Money - WithdrawalMoney - 0.5
        print("You now have", Money, "in your account")

else:
    print("We only give money in multiples of five")
    SecondTry = input("Would you like to try again? ")

    while SecondTry in ("Yes", "yes"):
        WithdrawalMoney = int(input("How much money do you want to withdraw Pooja? "))
        if WithdrawalMoney % 5 == 0:
            Money = Money - WithdrawalMoney - 0.5
            print("You now have", Money, "in your account")
            SecondTry = 0



