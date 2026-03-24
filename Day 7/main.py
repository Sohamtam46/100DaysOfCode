import random

wordList = ["anvil", "banana", "bushmills"]

wordChoice = wordList[random.randint(0,len(wordList)-1)]
print(wordChoice)

userGuessLetter = input("Guess the letter : ").lower()

letterGuessed = False

for letter in wordChoice:
    if letter == userGuessLetter:
        letterGuessed = True

if letterGuessed:
    print("Right")
else:
    print("Wrong")
    
