import random
difficulty = input("would you like 7 letter or 10 letter words? type 7 or 10 ")

if difficulty == 10:
    word = random.choice(open("2023/hangman/10letterwords.txt","r").read().split())
else:
    word = random.choice(open("2023/hangman/7letterwords.txt","r").read().split())
    
guessword = "_"*len(word)
print(guessword)
tries = int(len(word)/2+1)
wrongletters = []

while tries != 0:
    letter = input("\ninput a letter: ")
    if letter in word:
        guessword = guessword[0:word.index(letter)] + letter + guessword[word.index(letter)+1:]
        print(guessword)
        print("remaining tries: ",tries)
        print("wrong letters: ", wrongletters)
        if guessword == word:
            print("\nYOU WIN !!!!!!!!")
            break
    else:
        if letter in wrongletters:
            print(guessword)
            print("you've already guessed this letter. try a different one")
            print("remaining tries: ",tries)
            print("wrong letters: ", wrongletters)
        else:
            print(guessword)
            print("this letter isnt in the word")
            tries -= 1
            wrongletters += letter
            print("remaining tries: ",tries)
            print("wrong letters: ", wrongletters)
    if tries == 0:
        print("\nYOU LOSE")
        print("the word was:",word)