import math
from string import digits
from random import choice
print("Hello")
import random
words = ["python", "java", "swift", "javascript"]

#letters = set(chosen_word)
#a = chosen_word[0:3]
#b= ("-" *(len(chosen_word)-3))



wins = 0
losses = 0
reply = ""
while reply != "exit":
    chosen_word = random.choice(words)
    c= ("-" * (len(chosen_word)))
    count = 0
    guesses = []
    print("H A N G M A N")
    print('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit:')
    reply = input()
    if reply == "results":
        print("You won: " + str(wins) + " times")
        print("You lost: " + str(losses) + " times")
    if reply == "play":
        while count < 8:
            print()
            print(c)
            print("Input a letter:")
            answer = input()
            if len(answer) == 0 or len(answer) > 1:
                print("Please, input a single letter.")
                continue
            if answer.islower() == False:
                print("Please, enter a lowercase letter from the English alphabet.")
                continue
            for item in guesses:
                if item == answer:
                    print("You've already guessed this letter.")
                    continue
            if answer in chosen_word:
                guesses.append(answer)
                for itr in range(len(chosen_word)):
                    if chosen_word[itr] == answer:
                        position = itr
                        if c[position] == answer:
                            print("No Improvements")
                            count += 1
                            break
                        c = c[:itr] + answer + c[itr+1:]
            
            if answer not in chosen_word:
                guesses.append(answer)
                print("That letter doesn't appear in the word.")
                count += 1
            if c == chosen_word:
                print("You guessed the word " + chosen_word + "!")
                print("You survived!")
                wins += 1
                break
    if (count == 8):
        print("You lost!")
        losses += 1
    print("Thanks for playing!")