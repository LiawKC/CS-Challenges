import random

Numbers = random.sample(range(1,100), 50)

print("The numbers are:", Numbers)
print("The smallest value is", min(Numbers))
print("The largest value is", max(Numbers))

Average = sum(Numbers)/50
print(Average)