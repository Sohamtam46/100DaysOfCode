#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt",mode="r") as names:
    names_list = names.readlines()

with open("./Input/Letters/starting_letter.txt",mode="r") as letter:
    full_letter = letter.read()

for name in names_list:
    name_clean = name.strip("\n")
    with open(f"./Output/ReadyToSend/letter_to_{name_clean}.txt",mode="w") as output_letter:
        output_letter.write(full_letter.replace(PLACEHOLDER,name_clean))


