gate = input("what kind of gate do you want to try and make using nand gates?")
if gate == "and":
    A = int(input("How much power do you want to give to source A, 1 or 0?"))
    B = int(input("How much power do you want to give to source B, 1 or 0?"))
    if A == 0 and B == 0:
        print("your output is 1")
    else:
        print("your output is 0")
if gate == "or":
    A = int(input("How much power do you want to give to source A, 1 or 0?"))
    B = int(input("How much power do you want to give to source B, 1 or 0?"))
    if A == 0 or B == 0:
        print("your ouput is 1")
    else:
        print("your ouput is 0")
if gate == "nor":
    A = int(input("How much power do you want to give to source A, 1 or 0?"))
    B = int(input("How much power do you want to give to source B, 1 or 0?"))
    if A == 0 and B == 0:
        print("the ouput is 1")
    else:
        print("output is 0")
if gate == "xor":
    A = int(input("How much power do you want to give to source A, 1 or 0?"))
    B = int(input("How much power do you want to give to source B, 1 or 0?"))
    if A == 1 or B == 1:
        print("Ouput is 1")
    if A == 0 and B == 0:
        print("output is 0")
    if A ==1 or B ==1:
        print("output is 0")
if gate == "not":
    A = int(input("How much power do you want to give to source A, 1 or 0?"))
    B = int(input("How much power do you want to give to source B, 1 or 0?"))
    if A == 1 and B ==1:
        print("output is 1")
    else:
        print("output is 0")
