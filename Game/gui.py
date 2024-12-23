from tkinter import StringVar, Label, Entry, Button, Tk

from Game.constants import ButtonText, StatusMessage
from Game.state import GameState


class GameWindow:
    parts = ["O", "\n/", "|", "\\", "\n/ ", "\\"]

    def __init__(self, game_state: GameState):
        self.game_state = game_state
        self.window = Tk()
        self.window.geometry('1280x720')
        self.window.title("Hangman")
        self.window['bg'] = '#e5e9f0'
        self.title = Label(self.window, text="Hangman", font='Comfortaa', bg='#e5e9f0', fg='#2e3440')
        self.title.place(relx=0.5, rely=0.0, anchor='n')

        self.man = StringVar()
        self.man.set('')
        self.placeholder_text = StringVar()
        self.placeholder_text.set(' '.join(self.game_state.placeholder))
        self.wrong_letters = StringVar()
        self.wrong_letters.set('Wrong Letters: ' + ' '.join(self.game_state.wrong_letters))
        self.status_message = StringVar()
        self.status_message.set('')

        self.text_entry = Entry(self.window, width=20, bd=5, font='Comfortaa', fg='#2e3440')

        Label(self.window,
              textvariable=self.man,
              font='Comfortaa', bg='#e5e9f0', fg='#2e3440').place(relx=0.5, rely=0.2, anchor='n')
        Label(self.window,
              textvariable=self.placeholder_text,
              font='Comfortaa', bg='#e5e9f0', fg='#2e3440').place(relx=0.5, rely=0.4, anchor='n')
        Label(self.window,
              textvariable=self.wrong_letters,
              font='Comfortaa', bg='#e5e9f0', fg='#2e3440').place(relx=0.5, rely=0.5, anchor='n')
        Label(self.window,
              textvariable=self.status_message,
              font='Comfortaa', bg='#e5e9f0', fg='#2e3440').place(relx=0.5, rely=0.6, anchor='n')

        self.text_entry.place(relx=0.5, rely=0.7, anchor='n')

        self.button = Button(self.window,
                             text=ButtonText.ENTER,
                             font='Comfortaa', fg='#2e3440', bg='#d8dee9',
                             command=self.process_input, width=20)
        self.button.place(relx=0.5, rely=0.8, anchor='n')

    def process_input(self):
        text = self.text_entry.get().upper()
        self.text_entry.select_clear()

        if not text.isalpha():
            self.set_status_message(StatusMessage.INVALID_CHAR)
            return

        if len(text) != 1:
            self.set_status_message(StatusMessage.MORE_THAN_ONE_CHAR)
            return

        if self.game_state.is_already_guessed(text):
            self.set_status_message(StatusMessage.ALREADY_GUESSED_CHAR)
            return

        self.text_entry.delete(0, 'end')

        if self.game_state.is_wrong_letter(text):
            self.wrong_letters.set('Wrong Letters: ' + ' '.join(self.game_state.wrong_letters))
            self.man.set(''.join(self.parts[:self.game_state.count_wrong_guesses()]))
            if self.game_state.is_game_loss():
                self.set_status_message(StatusMessage.GAME_LOSE + self.game_state.word)
                self.switch_button_state()
            else:
                self.set_status_message('')
            return

        self.game_state.place_char(text)
        self.placeholder_text.set(' '.join(self.game_state.placeholder))

        if self.game_state.is_game_win():
            self.set_status_message(StatusMessage.GAME_WIN + self.game_state.word)
            self.switch_button_state()
        else:
            self.set_status_message('')

    def close(self):
        self.window.destroy()

    def run(self):
        self.window.mainloop()

    def switch_button_state(self):
        self.button.configure(command=self.close, text=ButtonText.CLOSE)

    def set_status_message(self, text: str):
        self.status_message.set(text)
