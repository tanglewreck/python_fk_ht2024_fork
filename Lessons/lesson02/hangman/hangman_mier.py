"""
hangman – guess the secret word

Första versionen av vårt spel kommer vara simplistiskt men fortfarande ett
fungerande program. Under kommande veckor kommer vi lägga till fler funktioner
samt dela upp programmet i flera filer.
"""
import random
from wordlist_se import WORDLIST

# POSSIBLE_WORDS = (
#    "Apa",
#    "Banan",
#    "Cacao",
#    "Dans",
#    "Elefant",
#    )
POSSIBLE_WORDS = WORDLIST

class HangmanGame:
    """Hangman game: guess the secret word"""

    def __init__(self, possible_words=POSSIBLE_WORDS, n_allowed_guesses=5):
        self.possible_words = possible_words
        self.n_allowed_guesses = n_allowed_guesses
        self.initialise()

    def initialise(self):
        """Här borde vissa delar av __init__ ligga för att korta ned den
        metoden.
        """
        # self.word_to_guess = ""
        self.word_to_guess = self.get_word_to_guess()
        print(self.word_to_guess)
        self.guessed_letters = set()
        self.current_guess = ""
        self.incorrect_guesses_made = 0

    def get_word_to_guess(self):
        return random.choice(self.possible_words).lower()

    def display_current_state(self):
        # print("Det hemliga ordet är", len(self.word_to_guess), "tecken långt.")
        # if len(self.guessed_letters) > 0:
        #    print("Du har gissat dessa bokstäver:", *self.guessed_letters)
        #    if self.incorrect_guesses_made == 1:
        #        print("Du har gissat fel", self.incorrect_guesses_made, "gång.")
        #    else:
        #        print("Du har gissat fel", self.incorrect_guesses_made, "gånger.")
        print("Du har", self.n_allowed_guesses - self.incorrect_guesses_made, "gissningar kvar.")
        # self.make_guess()

    def display_partially_hidden_word(self):
        # stat_str = "_ " * len(self.word_to_guess)
        # print(stat_str)
        for c in self.word_to_guess:
            if c in self.guessed_letters:
                print(f"{c} ", end="")
            else:
                print("_ ", end="")
        print()

    def make_guess(self):
        self.display_partially_hidden_word()
        self.current_guess == ""
        while self.current_guess in self.guessed_letters or len(self.current_guess) != 1:
            self.current_guess = input("Gissa en bokstav: ").lower()
        self.guessed_letters.add(self.current_guess)
        if self.check_guess():
            self.correct_guess()
        else:
            self.incorrect_guess()
        # self.display_current_state()

    def check_guess(self):
        return self.current_guess in self.word_to_guess

    def correct_guess(self):
        print(f"'{self.current_guess}' finns i det hemliga ordet.\n")
        self.check_game_won()

    def incorrect_guess(self):
        print(f"'{self.current_guess}' finns inte i det hemliga ordet.\n")
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
        if self.incorrect_guesses_made == self.n_allowed_guesses:
            self.display_partially_hidden_word()
            print(f"Game over! Det hemliga ordet var '{self.word_to_guess}'")
            self.do_quit()

    def mainloop(self):
        while self.incorrect_guesses_made <= self.n_allowed_guesses:
            self.display_current_state()
            self.make_guess()


    def do_quit(self):
        raise SystemExit(0)


if __name__ == '__main__':
    my_dictionary = ['apa', 'bepa']
    game = HangmanGame(WORDLIST)
    game.mainloop()
