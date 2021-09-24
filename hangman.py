import random

words = []
for line in open('poolOfWords.csv'):  # creates a list of over 1300 words to use
    line = line.rstrip('\n')
    line = line.split(',')
    if line[0] == '':
        break
    for word in line:
        words.append(word)

del words[0]

word = words[random.randint(0, len(words) - 1)].upper()
placeholder = []
for i in range(len(word)):
    placeholder.append('_')

guessesLeft = len(word) // 2 + len(word) // 3 + 5

temp = list(word)  # extracts each correct letter from the word
wrongLetters = []
alreadyGuessed = []  # keeps track of letters that have already been inputted

while guessesLeft > 0:
    print(placeholder)
    print('Number of guesses left:', guessesLeft)
    print('Wrong Letters: ', wrongLetters)
    print()
    answer = input('Guess a letter.\n').upper()
    if answer == word:  # the user inputs the correct word
        break
    elif len(answer) > 1:  # the user inputs multiple characters (excluding the correct word)
        print('Enter a single character!')
    elif answer in alreadyGuessed:  # the user inputs a letter that they put in before
        print('You already guessed that letter.')
    elif answer in word:  # the user inpurs a correct letter
        while answer in temp:
            replace = temp.index(answer)
            placeholder[replace] = answer
            temp[replace] = '_'
    else:  # the user inputs an incorrect character
        print('Nope!\n')
        alreadyGuessed.append(answer)
        wrongLetters.append(answer)
        guessesLeft -= 1
    if '_' not in placeholder:  # all correct letters have been guessed
        break

if guessesLeft > 0:  # the while loop breaks without using all available guesses
    print('Correct!, the word was', word)

else:
    print('The word we were looking for was', word + '!')
