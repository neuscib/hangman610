import random

fruits = ["watermelon", "mango", "pomegranate", "strawberry", "pineaple"]
word_list = fruits

#Fruta aleatoria de la lista
word= random.choice(word_list)


#Ask the user for an input
guess=input("Please, enter a single letter")

#Validate entry
if len(guess) == 1 and guess.isalpha():
    print ("Good guess!")
else:
    print ("Oops! That is not a valid input.")
