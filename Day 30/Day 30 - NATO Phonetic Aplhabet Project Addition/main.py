# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

import pandas as pd
# student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    # pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_data_df = pd.DataFrame(nato_data)
nato_data_dict = {row.letter:row.code for (index,row) in nato_data_df.iterrows()}
# this gives you dict with index numbers and key as column name
# nato_data_dict_1 = nato_data_df.to_dict()
# print(nato_data_dict_1)
#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter the word you need the phonetic code words for:\n").upper()
phonetic_code_word = {letter:nato_data_dict[letter] for letter in user_word}
print(phonetic_code_word)
