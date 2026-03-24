#subscripting
# print("Hello"[-1])

# print(type("Hello"))

# print("Number of letters in the name:" + str(len(input("Enter your name :"))))

print("Welcome to tip calculator")
totalBill = float(input("What was the total bill? $"))
tipPercent = int(input("How much tip would you like to give? 10, 12, 15?\n"))
numOfPeople = int(input("How many people would you like to split the bill with?\n"))
eachPersonShare = (totalBill * (tipPercent / 100) + totalBill) / numOfPeople
print(f"Each person should pay : ${round(eachPersonShare,2)}")  