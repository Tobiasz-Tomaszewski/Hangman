from hangman_functions import *
import random
import sys


f = open('words.txt')
words = f.readlines()
f.close()
words = [word.strip() for word in words]

for word in words:
    if not word_is_valid(word):
        print(f"Your 'words.txt' contains not supported sign. Only letters and spacebars are allowed.")
        sys.exit()

number_of_words = len(words)
current_word = words[random.randint(0, number_of_words - 1)]
user_guessed_letters = []
current_state = [1 if v == ' 'else 0 for v in current_word]
print(current_state)
print(current_word)
print(print_state(current_word, current_state))