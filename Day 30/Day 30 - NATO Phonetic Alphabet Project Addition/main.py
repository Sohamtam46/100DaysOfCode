import pandas as pd

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")
nato_data_df = pd.DataFrame(nato_data)
nato_data_dict = {row.letter:row.code for (index,row) in nato_data_df.iterrows()}


user_word = input("Enter the word you need the phonetic code words for:\n").upper()
phonetic_code_word = {letter:nato_data_dict[letter] for letter in user_word}
print(phonetic_code_word)
