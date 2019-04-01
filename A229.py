import random

Part1List = []
Part2List = []
Part3List = []
Part4List = []


for i in range(100):
    Part1 = random.randint(10,192)
    Part1List.append(Part1)
    Part2 = random.randint(0,255)
    Part2List.append(Part2)
    Part3 = random.randint(0,255)
    Part3List.append(Part3)
    Part4 = random.randint(0,25)
    Part4List.append(Part4)
    print(Part1List[i],".",Part2List[i],".",Part3List[i],".",Part4List[i])
