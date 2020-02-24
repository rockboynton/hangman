# Hangman game

import random

WORDLIST_FILENAME = "./words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)




def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for letter in secretWord:
        if letter not in lettersGuessed:
            return False
            break
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    temp = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            temp += letter
        else:
            temp += '_ '
    return temp


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    temp = ''
    for letter in alphabet:
        if letter not in lettersGuessed:
            temp += letter
    return temp


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) +
          'letters long.')
    print('-----------')
    guesses = 8
    lettersGuessed = []
    while guesses > 0:
        print('You have ' + str(guesses) + ' guesses left.')
        print('Available Letters: ' + getAvailableLetters(lettersGuessed))
        lastGuess = input('Please guess a letter: ').lower()
        lettersGuessed += lastGuess
        if lettersGuessed.count(lastGuess) > 1:
                print("Oops! You've already guessed that letter: " +
                      getGuessedWord(secretWord, lettersGuessed))
                print('-----------')
        elif lastGuess in secretWord:
                print('Good guess: ' + getGuessedWord(secretWord,
                      lettersGuessed))
                print('-----------')
                if isWordGuessed(secretWord, lettersGuessed):
                    print('Congratulations, you won!')
                    break
        else:
            print('Oops! That letter is not in my word: ' + getGuessedWord(
                  secretWord, lettersGuessed))
            guesses -= 1
            print('-----------')
            if guesses == 0:
                print('Sorry, you ran out of guesses. The word was ' +
                      secretWord + '.')

wordlist = loadWords()

if __name__ == '__main__':
    secretWord = chooseWord(wordlist).lower()
    hangman(secretWord)
