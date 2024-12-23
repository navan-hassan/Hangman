from enum import Enum


class StatusMessage(str, Enum):
    MORE_THAN_ONE_CHAR = 'Please enter one character'
    INVALID_CHAR = 'Invalid character'
    ALREADY_GUESSED_CHAR = 'You already guessed that letter'
    GAME_WIN = 'Correct! The word is '
    GAME_LOSE = 'The word we were looking for was '


class ButtonText(str, Enum):
    ENTER = 'Enter'
    CLOSE = 'Close'
