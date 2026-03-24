import random
import data

userChoice = int(input("What do you choose? Type 0 = rock, 1 = paper and 2 = scissor:\n"))
# catches any number entered by user that is more than 2 or less than 0
if 0 < userChoice >= 3:
    print("Wrong Choice!")
else:
    print(f"You choose {data.symbolNames[userChoice]}")
    print(data.symbols[userChoice])
    compChoice = random.randint(0,2)
    print(f"Computer chooses {data.symbolNames[compChoice]}")
    print(data.symbols[compChoice])
    if userChoice == compChoice:
        print("Its a tie!")
    elif (userChoice == 0 and compChoice == 1) or (userChoice == 1 and compChoice == 2) or (userChoice == 2 and compChoice == 0):
        print("Computer Wins!")
    else:
        print("You Win!")




