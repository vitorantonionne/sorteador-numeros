import random
drawnNumbers = []

lastNumber = 100
howManyNumber = 10

for num in range(1,howManyNumber+1):
    number = random.randint(1,lastNumber)
    drawnNumbers.append(number)
print(drawnNumbers)