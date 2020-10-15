import random

num = random.randint(1, 10)
print(num)
guess = False
while not guess:
    answer = input()
    if answer == num:
        break