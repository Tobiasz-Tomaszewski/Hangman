import string


def letter_in_the_word(word, letter):
    if letter not in string.ascii_letters:
        pass
    word = word.lower()
    letter = letter.lower()
    if letter in word:
        return True
    return False


def print_state(word, guess_state):
    printable = ''
    for letter, state in zip(word, guess_state):
        if state == 1:
            printable += letter
        else:
            printable += '_'
    return printable


def word_is_guessed(guess_state):
    return all(guess_state)


def word_is_valid(word):
    for letter in word:
        if letter not in string.ascii_letters + ' ':
            return False
    return True





