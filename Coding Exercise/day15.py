import random

def rand_number():
    x = int(input('Enter the lower bound: '))
    y = int(input('Enter the upper bound: '))
    random_number = random.randrange(x, y)
    print(random_number)
    return random_number

rand_number()

