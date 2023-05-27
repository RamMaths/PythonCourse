import pandas

# importing the csv file
letters = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
letters_dict = {row.letter:row.code for (index, row) in letters.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Please, type a word: ")

for letter in user_word:
    print(letter.upper() + " - " + letters_dict[letter.upper()])
