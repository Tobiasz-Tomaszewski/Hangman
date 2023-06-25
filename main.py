from hangman_functions import *
import random
import sys
from Word_class import *

f = open('words.txt')
words = f.readlines()
f.close()
words = [word.strip() for word in words]

for word in words:
    if not word_is_valid(word):
        print(f"Your 'words.txt' contains not supported sign. Only letters and spacebars are allowed.")
        sys.exit()

number_of_words = len(words)
current_word = Word(words[random.randint(0, number_of_words - 1)])
while not current_word.word_is_guessed:
    print(current_word)
    user_letter = input("Guess the letter: ")
    if not current_word.letter_is_valid(user_letter):
        print('The letter you have provided is not supported. Please try again.')
        next
    current_word.guess_letter(user_letter)
    print(current_word)


