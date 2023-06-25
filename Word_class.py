import string


class Word:
    def __init__(self, wrd):
        self.w = wrd
        self.status = [1 if v == ' ' else 0 for v in self.w]
        self.guessed_letters = []
        self.word_is_guessed = False
        self.allowed_symbols = string.ascii_letters + ' '
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
            return f'Congratulation! You have guessed the word! \nYour word: {printable}.\nYour score: {self.calculate_score()}'
        return f'The letters you have tried: {self.guessed_letters}. \nYour word: {printable}'

    def calculate_score(self):
        pass

    def __word_is_valid(self):
        for char in self.w:
            if char not in self.allowed_symbols:
                return False
        return True

    def letter_is_valid(self, letter):
        if letter in self.allowed_symbols:
            return True
        return False

    def __update_status(self, letter):
        for i, v in enumerate(self.w):
            if letter.lower() == v.lower():
                self.status[i] = 1
        if all(self.status):
            self.word_is_guessed = True
        return None

    def guess_letter(self, letter):
        if self.letter_is_valid(letter):
            self.__update_status(letter)
        else:
            return False
        if letter.lower() not in self.guessed_letters:
            self.guessed_letters.append(letter.lower())

