#!/usr/bin/env python3 

"""
hangman – guess the secret word

Första versionen av vårt spel kommer vara simplistiskt men fortfarande ett
fungerande program. Under kommande veckor kommer vi lägga till fler funktioner
samt dela upp programmet i flera filer.
"""
import random
from utils import parse_arguments
from wordlist_se import WORDLIST as WORDLIST_1   #   6,212 entries
from swe_wordlist import WORDLIST as WORDLIST_2  # 403,511 entries, including declinations

WORDLIST = WORDLIST_2

class HangmanGame:
    """
    Hangman game: guess the secret word
    """

    def __init__(self, possible_words=WORDLIST, n_allowed_guesses=5, debug=False):
        # A list of words from which the secret word is randomly chosen
        self.debug = debug
        self.possible_words = possible_words
        self.n_allowed_guesses = n_allowed_guesses
        self.initialise()

    def initialise(self):
        """
        Initialise stuff
        """
        # Randomly choose a word from the wordlist
        self.word_to_guess = self.get_word_to_guess()
        if self.debug:
            print(self.word_to_guess)
        self.guessed_letters = set()
        self.current_guess = ""
        self.incorrect_guesses_made = 0

    def get_word_to_guess(self):
        return random.choice(self.possible_words).lower()

    def display_current_state(self):
        if len(self.guessed_letters) > 0:
            print("Gissade bokstäver:", *self.guessed_letters)
        print("Du har", self.n_allowed_guesses - self.incorrect_guesses_made, "gissningar kvar.")

    def display_partially_hidden_word(self):
        return " ".join( [ c if c in self.guessed_letters else "_" for c in self.word_to_guess ])

    def make_guess(self):
        print(self.display_partially_hidden_word())
        print()
        self.current_guess == ""
        while self.current_guess in self.guessed_letters or len(self.current_guess) != 1:
            self.current_guess = input("Gissa en bokstav: ").lower()
            print()
        self.guessed_letters.add(self.current_guess)
        if self.check_guess():
            self.correct_guess()
        else:
            self.incorrect_guess()

    def check_guess(self):
        return self.current_guess in self.word_to_guess

    def correct_guess(self):
        self.check_game_won()

    def incorrect_guess(self):
        self.incorrect_guesses_made += 1
        self.check_game_over()

    def check_game_won(self):
        for letter in self.word_to_guess:
            if letter not in self.guessed_letters:
                return
        self.display_partially_hidden_word()
        print(f"Du vann! Det hemliga ordet var '{self.word_to_guess}'")
        self.do_quit()

    def check_game_over(self):
        """Called after an incorrect guess has been made. If no attempts
        remain, barf and quit"""
        # if self.incorrect_guesses_made == self.n_allowed_guesses:
        if self.n_allowed_guesses - self.incorrect_guesses_made == 0:
            self.display_partially_hidden_word()
            print("Game over!")
            print(f"Det hemliga ordet var '{self.word_to_guess}'")
            self.do_quit()

    def mainloop(self):
        """Mainloop:
        1. Display current state (number of guesses made and remaining)
        2. Make the next guess
        """
        while self.incorrect_guesses_made <= self.n_allowed_guesses:
            self.display_current_state()
            self.make_guess()

    def do_quit(self):
        """Just quit"""
        raise SystemExit(0)


if __name__ == '__main__':
    # Parse command-line arguments (-d, -v, -n)
    args = parse_arguments()
    # 
    game = HangmanGame(possible_words=WORDLIST_2, n_allowed_guesses=args.n, debug=args.debug)
    game.mainloop()
