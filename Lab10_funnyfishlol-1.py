"""
Word Counter
Nathan Henneman
Checks how many instances of each word are in a text file
November 2, 2025
"""
from pathlib import Path
import string 

def main():
    file_name = input("What file do you want to process? ")
    file_path = Path(file_name)
    
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            content = file.read()
            wordFreq(content)
    except FileNotFoundError:
        print("File not found.")

def wordFreq(_content):
    file_words = _content.split()
    removed_punctuation = [word.translate(str.maketrans('', '', string.punctuation)) for word in file_words]
    fixed_words = [word.lower() for word in removed_punctuation]
    words_used = []
    return_array = []
    for i in range(len(file_words)):
        word_count = 0
        curr_word = fixed_words[i].lower()
        if(curr_word not in words_used):
            words_used.append(curr_word)
            for j in range(len(fixed_words)):
                checked_word = fixed_words[j]
                if(checked_word.lower() == curr_word):
                    word_count += 1
            return_array.append([curr_word, word_count])
    return_array.sort()
    printOut(return_array)

    return None

def printOut(_freq_list):
    for element in _freq_list:
        print(f"{element[0]} : {element[1]}")

main()


