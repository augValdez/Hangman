'''
Hangman.py

Sept 11, 19

Augustine Valdez
partner: Preston McIllece
'''

import sys
import random

class Hangman:
    '''
    Initializes the words list
    '''
    def __init__(self):
        file = open('words.txt','r')
        self.words = []
        self.wordguess = []
        for line in file:
            self.words.append(line.rstrip())

    '''
    Outputs the current status of the guesses
    '''
    def printword(self):
        for c in self.wordguess:
            print(c,end="")
        print()

    def playgame(self):
        # generate random word
        word = self.words[random.randint(0,len(self.words)-1)]
        #print word
        self.wordguess = ['_'] * len(word)
        print()
        print("Welcome to Hangman! Guess one letter at a time to guess the secret word!")
        guesses = 0
        previousGuess = []
        hasWon = False
        while guesses < 10:
            print()
            print(list(map(lambda x: x, self.wordguess)))
            print()
            ch = input('Enter a guess: ').lower()
            # check if alphabetical
            if not ch.isalpha():
                print("Input needs to be alphabetical.")
            # check if input is not 1
            elif len(ch) != 1:
                print("Input only 1 letter!")
            else:
                firstIndex = 0
                print("letter guessed:",ch)
                if ch in previousGuess:
                    print("You already guessed: ", ch)
                elif ch in word and ch not in previousGuess:
                    self.wordguess = list(map(lambda a, b: a if a == ch else b, word, self.wordguess))
                    guesses += 1
                else:
                    previousGuess.extend(ch)
                    print(ch, "is not in word.")
                    guesses += 1
                
            print("guessed left: ", 10 - guesses )
            if "_" not in self.wordguess:
                print("Congradulations! You have correctly guessed the word:", word, "!")
                hasWon = True
                break
        if hasWon is False:
            print("Sorry dude, the word was:", word)


if __name__ == "__main__":

    game = Hangman()

    game.playgame()
