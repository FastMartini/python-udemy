import random

# For Loop:
# for item in list_of_items:
# Do something to each item
#-------------------------------------
# Example 1: Prints each item in list

# fruits = ["Apple", "Oranges", "Pear"]
# for fruit in fruits:
#    print(fruit)
#-------------------------------------
# Example 2: Finding greatest integer in list

# sat_scores = [1450, 1320, 1580, 1210, 990, 1100, 1430, 1250, 1600, 1040, 870, 1390, 1500, 1280, 1160, 1070, 930, 1520, 1360, 980]
#
# max_score = 0
# for score in sat_scores:
#     if score > max_score:
#         max_score = score
#
# print(max_score)
#-------------------------------------
# Example 3: Range function

# for number in  range(1, 11):
#     print(number)

# iterates every three steps:

# for number in range(1, 11, 3):
#     print(number)
#-------------------------------------
# The Gauss Challenge

# sum = 0
# for number in range(1, 101):
#         sum += number
# print(sum)
#-------------------------------------
# FizzBuzz Challenge
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print(str(number) + ": " + "FizzBuzz")
#     elif number % 3 == 0:
#          print(str(number) + ": " + "Fizz")
#     elif number % 5 == 0:
#          print(str(number) + ": " + "Buzz")
#     else:
#         print(number)
#-------------------------------------

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m', 'n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M', 'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!', '#', '@', '$', '%', '&', '*', '(', ')', '_', '-', '+', '=']
password = []

print("Welcome to Password Generator")
num_letters = int(input("How many letters would you like in your password\n"))
num_symbols = int(input("How many symbols would you like in your password\n"))
num_numbers = int(input("How many numbers would you like in your password\n"))

for l in range(0, num_letters):
    password.append(random.choice(letters))
for s in range(0, num_symbols):
    password.append(random.choice(symbols))
for n in range(0, num_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)
for pswd in password:
    print(pswd, end="")








