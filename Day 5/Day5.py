# student_score = [450, 550, 80, 20, 760, 500, 530, 110, 230, 500, 750]

# highScore  = 0

# for score in student_score:
#     if highScore < score:
#         highScore = score
#     else:
#         continue

# print(highScore)
# total = 0

# for num in range(0,101):
#     total += num

# print(total)

import random
import data

print("Welcome to the PyPassword Generator!")
numOfLetters = int(input("How many letters would you like in your password?\n"))
numOfSymbols = int(input("How many symbols would you like?\n"))
numofNumbers = int(input("How many numbers would you like?\n"))

letters = []
symbols = []
numbers = []


for i in range(numOfLetters):
    letters += data.letters[random.randint(0,len(data.letters)-1)]
for j in range(numOfSymbols):
    symbols += data.symbols[random.randint(0,len(data.symbols)-1)]
for k in range(numofNumbers):
    numbers += data.numbers[random.randint(0,len(data.numbers)-1)]


combinationOfPass = letters + symbols + numbers
# this helps randomize the sequence of the password
random.shuffle(combinationOfPass)

password = ''

for value in combinationOfPass:
    password += value

print(f"Your password is :{password}")