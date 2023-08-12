import random
from Hangman_class import *
import hangman_drawing

f = open('Words.txt')
words = f.readlines()
f.close()
words = [word.strip() for word in words]
number_of_words = len(words)
current_word = Hangman(words[random.randint(0, number_of_words - 1)])
current_word.read_pictures(hangman_drawing.drawing)

while (not current_word.word_is_guessed) and (current_word.bad_tries != current_word.max_tries):
    print(current_word)
    user_letter = input("Guess the letter: ")
    if not current_word.letter_is_valid(user_letter):
        print('The letter you have provided is not supported. Please try again.')
        next
    current_word.guess_letter(user_letter)
print(current_word)
