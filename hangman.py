from Game.gui import GameWindow
from Game.state import GameState
from Game.utilities import get_random_word

if __name__ == '__main__':
    word = get_random_word()
    game_state = GameState(word)
    game_window = GameWindow(game_state)
    game_window.run()