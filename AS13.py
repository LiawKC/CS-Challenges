Choice = input("Are you looking for the GPM or the NPM? ")

if Choice == "GPM":
    GrossProfit = int(input("What is the gross profit?"))
    Sales = int(input("What are the sales"))
    GPM = GrossProfit/Sales * 100
    print("The GPM is", GPM)

if Choice == "APM":
    NetProfit = int(input("What is the net profit?"))
    Sales = int(input("What are the sales"))
    NPM = NetProfit/Sales * 100
    print("The NPM is", NPM)
