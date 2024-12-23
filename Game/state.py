class GameState:
    def __init__(self, word: str):
        self.word = word
        self.guesses_left = 6
        self.already_guessed = []
        self.wrong_letters = []
        self.placeholder = ['_'] * len(word)

    def is_already_guessed(self, character: str) -> bool:
        return character in self.already_guessed

    def is_wrong_letter(self, character: str) -> bool:
        is_wrong = character not in self.word
        self.already_guessed.append(character)
        if is_wrong:
            self.wrong_letters.append(character)
            self.guesses_left -= 1
        return is_wrong

    def place_char(self, character: str):
        if character not in self.word:
            return

        indices = [index for index, c in enumerate(self.word) if c == character]
        self.already_guessed.append(character)
        for index in indices:
            self.placeholder[index] = character

    def is_game_win(self):
        return '_' not in self.placeholder

    def is_game_loss(self):
        return self.guesses_left <= 0

    def count_wrong_guesses(self):
        return 6 - self.guesses_left
