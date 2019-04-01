List = []
AnotherList = []

for i in range(101,1000):
    List.append(i)

Length = len(List)

for i in range(Length):
    ChosenNumber = List[i]
    for i in range (3):
        Sum = sum(map(int,str(ChosenNumber)))
        if ChosenNumber % Sum == 0:
            print("It's neat!")
        else:
            print("It ain't neat chief")

