for List in range(1,21):

    if List % 3 == 0 and List % 5 == 0:
        print("Fizzbuzz")
        continue
    elif List % 3 == 0:
        print("Buzz")
        continue

    elif List % 5 == 0:
        print("Buzz")
        continue

    print(List)
