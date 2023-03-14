#Guess the number in max 5 chances
import random

wins = False #original state
print('Guess a number in range 1-20')
num = random.randint(1,20)
for i in range(1,6): #1-5
    print("Guess ", i, ":")
    guess = int(input())
    if guess == num:
        wins = True #update the state indicating a win
        print('You win')
        break
    elif guess > num:
        print("Guess a smaller value ")
    elif guess < num:
        print("Guess a greater value")

if wins == False: # when the state has remained original
    print('You lose')