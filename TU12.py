List = []

while True:
    Add = input("Do you want to add any characters? ")
    if Add == "y":
        Choice = input("What character do you want to add ")
        List.append(Choice)
        print(List)
    else:
        print("Bye")
        break
