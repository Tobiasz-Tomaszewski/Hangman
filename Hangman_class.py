import string


class Hangman:
    def __init__(self, wrd):
        self.w = wrd
        self.status = [1 if v == ' ' else 0 for v in self.w]
        self.guessed_letters = []
        self.word_is_guessed = False
        self.allowed_symbols = string.ascii_letters + ' ' + '-'
        self.hangman_pictures = {}
        self.bad_tries = 0
        self.max_tries = 11
        if not self.__word_is_valid():
            raise ValueError("Word contains unsupported signs.")

    def __str__(self):
        printable: str = ''
        for i in range(len(self.status)):
            if self.status[i] == 1:
                printable += self.w[i]
            if self.status[i] == 0:
                printable += '_'
        if self.word_is_guessed:
            return f'Congratulation! You have guessed the word! \nYour word: {printable}.'
        if self.bad_tries == self.max_tries:
            return f'{self.hangman_pictures[self.bad_tries]}\nYou lost :(\nThe word was: {self.w}.'
        if self.hangman_pictures:
            return f'{self.hangman_pictures[self.bad_tries]}\nLetters you have tried: {self.guessed_letters}.\nYour word: {printable}'
        return f'Letters you have tried: {self.guessed_letters}.\nYour word: {printable}'

    def __word_is_valid(self):
        for char in set(self.w):
            if char not in self.allowed_symbols:
                return False
        return True

    def letter_is_valid(self, letter):
        if letter in set(self.allowed_symbols):
            return True
        return False

    def __update_status(self, letter):
        s = sum(self.status)
        for i, v in enumerate(self.w):
            if letter.lower() == v.lower():
                self.status[i] = 1
        if all(self.status):
            self.word_is_guessed = True
        if s == sum(self.status):
            self.bad_tries += 1
        return None

    def guess_letter(self, letter):
        if self.letter_is_valid(letter):
            self.__update_status(letter)
        else:
            return False
        if letter.lower() not in self.guessed_letters:
            self.guessed_letters.append(letter.lower())

    def read_pictures(self, dict_of_pictures):
        self.hangman_pictures = dict_of_pictures
        self.max_tries = len(self.hangman_pictures) - 1

