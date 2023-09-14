#!/usr/bin/env python

import random

def main():
    #Start a genre guessing game.
    print("Guess the genre!")

    genre = [
        "classical",
        "jazz",
        "hiphop",
        "techno"
        ]
    x = random.choice(genre)
    max_trials = 3
    trials = 0
    score = 100       
    guess = None
    #print(x)
    while trials<max_trials:
        guess = str(input("What music am I thinking of? "))
        
        if x == guess:
            print(f"congratulations,You got it right! You get only in {max_trials} attempts and your score is {score}!".format(guess))
            max_trials +=1
            score += 20
            break
        else:
            print(f"Unfortunately you got the wrong answer.You have {max_trials} chances left. Please try again!".format(guess))
            print(f"the genre has {len(x)} words")
            max_trials -=1
            score-=20
            
main()