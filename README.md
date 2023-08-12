# Hangman
This is small python project that implements simple hangman game in console.
Words that are available in the game are being loaded from 'Words.txt' file.
Words in the 'Words.txt' were extracted from 'The Oxford 3000 is the list of the 3000 most important words to learn in English, from A1 to B2 level'
Link: 'https://www.oxfordlearnersdictionaries.com/external/pdf/wordlists/oxford-3000-5000/The_Oxford_3000.pdf'

User can add their own words as long as: 

    - Every word/phrase is separated by new line.
    - Every word/phrase contains only supported symbols. Supported symbols are: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', ' ', '-''].
    - The end of 'words.txt' file does not contain any new line symbol.

User can change the hangman animation. Animation is stored in 'hangman_drawing.py' as python dictionary.
The format of user-provided animation must match the format of the suggested one.
User -provided animation must be saved as dictionary called 'drawing'.
User-provided animation can have different number of elements than the original.