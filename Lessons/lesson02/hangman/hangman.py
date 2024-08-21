# Första versionen av vårt spel kommer vara simplistiskt men fortfarande ett
# fungerande program. Under kommande veckor kommer vi lägga till fler funktioner
# samt dela upp programmet i flera filer.
import random

POSSIBLE_WORDS = (
    "Apa",
    "Banan",
    "Cacao",
    "Dans",
    "Elefant",
    )


class HangmanGame:
    def __init__(self, possible_words=None, allowed_guesses=5):
        if possible_words is None:
            self.possible_words = POSSIBLE_WORDS
        self.allowed_guesses = allowed_guesses
        self.word_to_guess = ""
        self.get_word_to_guess()
        self.guessed_letters = set()

    def get_word_to_guess(self):
        self.word_to_guess = random.choice(self.possible_words)


class GameController:
    # current_game: HangmanGame

    def __init__(self):
        self.start_new_game()
        self.current_guess = ""
        self.current_game = self.start_new_game()

    def start_new_game(self):
        return HangmanGame()

    def check_guess(self):
        if self.current_guess in self.current_game.word_to_guess:
            self.correct_guess()
            return True
        else:
            self.incorrect_guess()
            return False

    def correct_guess(self):
        pass

    def incorrect_guess(self):
        pass


def start_hangmangame():
    game = GameController()


if __name__ == '__main__':
    start_hangmangame()
