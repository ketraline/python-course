import random
import requests
import json

difficulty = input("how many letters? ")
word = requests.get('https://random-word-api.herokuapp.com/word?length='+difficulty)
word = json.loads(word.text)[0]

guessword = list("_"*len(word))
print(''.join(guessword))
tries = int(len(word)/2+1)
wrongletters = []

while tries != 0:
    letter = input("\ninput a letter: ")
    if letter in word:
        for i in range(len(word)):
                if word[i] == letter:
                    guessword[i] = letter
        print(''.join(guessword))
        print("remaining tries: ",tries)
        print("wrong letters: ", wrongletters)
        if ''.join(guessword) == word:
            print("\nYOU WIN !!!!!!!!")
            break
    else:
        if letter in wrongletters:
            print(''.join(guessword))
            print("you've already guessed this letter. try a different one")
            print("remaining tries: ",tries)
            print("wrong letters: ", wrongletters)
        else:
            print(''.join(guessword))
            print("this letter isnt in the word")
            tries -= 1
            wrongletters += letter
            print("remaining tries: ",tries)
            print("wrong letters: ", wrongletters)
    if tries == 0:
        print("\nYOU LOSE")
        print("the word was:",word)