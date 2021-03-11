import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''', '''
  +---+
  O   |
      |
      |
     ===''', '''
  +---+
  O   |
  |   |
      |
     ===''', '''
  +---+
  O   |
 /|   |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
      |
     ===''', '''
  +---+
  O   |
 /|\  |
 /    |
     ===''', '''
  +---+
  O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O   |
 /|\  |
 / \  |
     ===''', '''
  +---+
 [O]  |
 /|\  |
 / \  |
     ===''']
words = {'Колір':'червоний оранжевий жовтий зелений синій голубий фіолетовий білий чорний коричневий'.split(),
'Фігури':'квадрат трикутник прямокутник круг еліпс ромб трапеція паралелограм пятикутник шестикутник восьмикутник'.split(),
'Фрукти':'яблоко апельсин лимон лайм груша мандарин виноград грейпфрут персик банан абрикос манго банан нектарин'.split(),
'Тварини':'айст баран борсук бик вовк зебра кит коза корова кіт кролик пацюк лев лисиця лось ведмідь миша норка носоріг мавпа вівця олень осел панда пума собака сова тигр тюлень ящірка'.split()}


def getRandomWord(wordDict):
    # Ця функція повертає випадкову рядок з переданого словника списків рядків, а також ключ.
    # По-перше, випадковим чином вибираємо ключ зі словника:
    wordKey = random.choice(list(wordDict.keys()))

    # По-друге, випадковим чином вибираємо слово зі списку ключів в словнику:
    wordIndex = random.randint(0, len(wordDict[wordKey]) - 1)

    return [wordDict[wordKey][wordIndex], wordKey]


def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Помилкові літери:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # замінює пропуски відгадати буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # Показує секретне слово з пробілами між буквами
        print(letter, end=' ')
    print()


def getGuess(alreadyGuessed):
    # Повертає букву, введену гравцем. Ця функція перевіряє, що гравець ввів тільки одну букву і нічого більше.
    while True:
        print('Введіть букву.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Будь ласка, введіть одну букву.')
        elif guess in alreadyGuessed:
            print('Ви вже називали цю букву. Введіть іншу.')
        elif guess not in 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя':
            print('Будь ласка, введіть БУКВУ.')
        else:
            return guess


def playAgain():
    # Ця функція повертає значення True, якщо гравець хоче зіграти заново; в іншому випадку повертає False.
    print('Хочете зіграти ще раз? (так або ні)')
    return input().lower().startswith('т')


print('Ш И Б Е Н И Ц Я')

difficulty = ''
while difficulty not in ['Л', 'С', 'В']:
    print('Виберіть рівень важкості: Л - Легкий, С - Середній, В - Важкий')
    difficulty = input().upper()
if difficulty == 'С':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
if difficulty == 'В':
    del HANGMAN_PICS[8]
    del HANGMAN_PICS[7]
    del HANGMAN_PICS[5]
    del HANGMAN_PICS[3]

missedLetters = ''
correctLetters = ''
secretWord, secretSet = getRandomWord(words)
gameIsDone = False

while True:
    print('Секретне слово з набору: ' + secretSet)
    displayBoard(missedLetters, correctLetters, secretWord)

    # Дозволяє гравцеві ввести букву.
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        # Перевіряє, чи виграв гравець.
        foundAllLetters = True
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('ТАК! Секретне слово - "' + secretWord + '"! Ви вгадали!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        # Перевіряє, чи перевищив гравець ліміт спроб і програв.
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('Ви вичерпали всі спроби!\nНе вгадано літер: ' + str(len(missedLetters)) + ' і вгадано літер: ' + str(len(correctLetters)) + '. Було загадане слово: "' + secretWord + '".')
            gameIsDone = True

    # Запитує, чи хоче гравець зіграти заново (тільки якщо гра завершена).
    if gameIsDone:
        if playAgain():
            missedLetters = ''
            correctLetters = ''
            gameIsDone = False
            secretWord, secretSet = getRandomWord(words)
        else:
            break
