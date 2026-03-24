# print("Welcome to Python Pizza Delivery!")
# size = input("What size of pizza do you want? S , M , L : ")
# pepporoni = input("Do you want Pepporoni on your pizza? Y or N : ")
# extra_cheese = input("Do you want extra cheese? Y or N : ")

# if size == "S":
#     bill = 15
#     if pepporoni == "Y":
#         bill += 2
# elif size == "M":
#     bill = 20
# elif size == "L":
#     bill = 25
# else:
#     print("you types wrong input!")

# if size != "S":
#     if pepporoni == "Y":
#         bill += 3

# if extra_cheese == "Y":
#     bill += 1

# print(f"Your final bill is ${bill}")


# final project for the day

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')

print("Welcome to Treasure island")
print("Your mission is to find the treasure")
firstChoice = input("Do you want to go to Dublin or Galway? : ").lower
if firstChoice == "dublin":
    print(firstChoice)
    print("You are dead X")
else:
    print("You arrive at the shore!")
    print("You see an island in the sea and have a strong feeling the treasure is there!")
    secondChoice = input("Do you choose to swim or wait for the ferry to arrive? Answer Swim or Wait : ").lower
    if secondChoice == "swim":
        print("The lochness monster eat you alive!! YOU ARE DEAD!")
    else:
        print("Treasure comes to those who are patient!")
        print("You take the ferry and land on Aran Island")
        print("You come across a castle that has three doors!")
        print("First door has the fire symbol on it!")
        print("Second door has Water symbol on it!")
        print("Third door has tair sadam symbol on it!")
        thirdChoice = input("Which one do you choose? first, second or third?").lower
        if thirdChoice == "first":
            print("YOU ARE BURNED BY FIRE!! YOU ARE DEAD!")
        elif thirdChoice == "second":
            print("You are eaten alive by monster! YOU ARE DEADD")
        else:
            print("Soham waits for you with a plate of tair sadam with vengayawada!! You WINN!!")

