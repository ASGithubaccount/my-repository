# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, 
# between 1500 and 2700 (both included)

l = []
for x in range(1499, 2701):
    if x % 7 == 0 and x / 5 == int(x/5):
        l.append(x)

print(l)

# 2. Write a Python program to convert temperatures to and from celsius, fahrenheit
# [ Formula : c * 1.8 + 32 [ where c = temperature in celsius and f = temperature in fahrenheit ]
# Expected Output :
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius 


def temp_converter(f, u):
    if u == 'c':
        return f * 1.8 + 32
    if u == 'f':
        return (f - 32) / 1.8

dupa = temp_converter(60, 'c')
print(dupa)
print(temp_converter(dupa, 'f'))
cycki = temp_converter(45, 'f')
print(cycki)
print(temp_converter(cycki, 'c'))

# 3. Write a Python program to guess a number between 1 to 9. Go to the editor
# Note : User is prompted to enter a guess. If the user guesses wrong then the 
# prompt appears again until the guess is correct, on successful guess, user will get a 
# "Well guessed!" message, and the program will exit.
import random

num = random.randint(1, 10)
print(num)
guess = False
while not guess:
    answer = str(int(input()))
    print(type(answer))
    if answer == num:
        print('Good job skippy!')
        break