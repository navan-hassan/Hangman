import requests, random
from tkinter import *

url =  'https://www.randomlists.com/data/vocabulary-words.json'
r = requests.get(url)
allWords = r.json()['data']
word = (random.choice(allWords)['name']).upper()
characters = list(word)
placeholder = ['_'] * len(word);
parts = ["O", "\n/", "|", "\\", "\n/ ",  "\\"]
guesses = 6;
alreadyGuessedList = []
wrongLettersList = []


window = Tk()
window.geometry('1280x720')
window.title("Hangman")
window['bg'] = '#e5e9f0'
title = Label(window, text="Hangman", font = 'Comfortaa', bg = '#e5e9f0', fg = '#2e3440')
title.place(relx=0.5, rely=0.0, anchor = 'n')

man = StringVar()
man.set("")
wrongLetters = StringVar()
wrongLetters.set("Wrong Letters: " + " ".join(wrongLettersList))
placeholderText = StringVar()
placeholderText.set(" ".join(placeholder))
entry = Entry(window, width= 20, bd = 5, font = 'Comfortaa', fg ='#2e3440')
errormsg = StringVar()
errormsg.set("")
answer = StringVar()
answer.set("")


def close():
    window.destroy();

def placeChar():
    errormsg.set("")
    global guesses
    if guesses == 0:
        return
    c = entry.get().upper()
    entry.select_clear()
    if c == word:
        answer.set("Correct! The word is " + word)
        guesses == 0
        button.configure(command = close, text = "Close")
    elif len(c) > 1:
        errormsg.set("Please enter one character.")
    elif c in placeholder or c in wrongLettersList:
        errormsg.set("You already guessed that letter.")
    elif c in characters:
        while c in characters:
            index = characters.index(c)
            placeholder[index] = c
            characters[index] = ''
            placeholderText.set(' '.join(placeholder))
        if '_' not in placeholder:
            answer.set("Correct! The word is " + word)
            button.configure(command = close, text = "Close")
        entry.delete(0, "end")
    else:
        wrongLettersList.append(c)
        guesses -= 1
        man.set(''.join(parts[:(6-guesses)]))
        wrongLetters.set("Wrong Letters: " + " ".join(wrongLettersList))
        if guesses == 0:
            answer.set("The word we were looking for was " + word)
            button.configure(command = close, text = "Close")
        entry.delete(0, "end")


button = Button(window,text="Enter", font='Comfortaa', fg = '#2e3440', bg = '#d8dee9', command = placeChar, width = 20)
button.place(relx = 0.5, rely = 0.8, anchor = 'n')

Label(window, textvariable=man, font = 'Comfortaa', bg = '#e5e9f0', fg = '#2e3440').place(relx=0.5, rely=0.2, anchor = 'n')
Label(window, textvariable=placeholderText, font = 'Comfortaa', bg = '#e5e9f0', fg = '#2e3440').place(relx=0.5, rely=0.4, anchor = 'n')
Label(window, textvariable=wrongLetters, font = 'Comfortaa', bg = '#e5e9f0', fg = '#2e3440').place(relx=0.5, rely=0.5, anchor = 'n')
Label(window, textvariable=answer, font = 'Comfortaa', bg = '#e5e9f0', fg = '#2e3440').place(relx=0.5, rely=0.6, anchor = 'n')
Label(window, textvariable=errormsg, font = 'Comfortaa', bg = '#e5e9f0', fg = '#2e3440').place(relx=0.5, rely=0.9, anchor = 'n')
entry.place(relx = 0.5, rely = 0.7, anchor = 'n')

window.mainloop()




    
    
    


