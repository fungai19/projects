def guessingGame(guess):
     y=0
     while guess !=y:
        guess=input("Enter your guess here: ")
        y=random.randint(1,5)
        if guess == y:
            print("You're lucky!")
        elif guess<y:
            print("Too low")
        elif guess>y:
            print("Too high")
        
            
        
            
import random


