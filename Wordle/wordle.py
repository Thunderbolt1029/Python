from logging import exception
import random

notGoodInput = True
while notGoodInput:
    try:
        wordLen = int(input("What word length would you like? "))
        if wordLen<3 or wordLen>10: raise exception()
        notGoodInput=False
    except:
        notGoodinput=True
        print("It should be a number between 3 and 10 inclusive", end="\n\n")

wordListFile = open(f"{str(wordLen)}letterwords.txt")

words = wordListFile.read().split("\n")

randomWord = words[random.randint(0, len(words))]

guess = ""
tries = 0
while guess!=randomWord:
    goodInput = False
    while not goodInput:
        try:
            guess = input("What is your guess? ")
            if len(guess)!=wordLen or not guess in words: raise exception()
            goodInput=True
        except:
            goodInput=False
            print(f"It should be an English word with a length of {wordLen} letters long", end="\n\n")
    tries+=1

    
    guessArray = [0]*len(guess)
    for i in range(len(guess)):
        guessArray[i] = guess[i]

    randomWordArray = [0]*len(randomWord)
    for i in range(len(randomWord)):
        randomWordArray[i] = randomWord[i]

        
    rightPlace = rightLetter = 0
    if guess!=randomWord: 
        for i in range(len(guess)):
            if guessArray[i]==0: continue
            elif guessArray[i]==randomWordArray[i]:
                rightPlace+=1
                guessArray[i] = randomWordArray[i] = 0

        for i in range(len(guess)):
            if guessArray[i]==0: continue
            elif guessArray[i] in randomWordArray:
                rightLetter+=1
                randomWordArray[randomWordArray.index(guessArray[i])] = guessArray[i] = 0

        print(f"Right letters right place: {rightPlace}, Right letters wrong place {rightLetter}", end="\n\n")

print(f"You guessed the word in {tries} tries!")