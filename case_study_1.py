"""
#
# Card Game
#
"""
import itertools
import numpy as np
import random
import keyboard
import time
random.seed(0)

red_cards = 26 * [1]
black_cards = 26 * [0]
unshuffled_deck = red_cards + black_cards
#print(unshuffled_deck)
shuffled_deck = np.random.permutation(unshuffled_deck)
print(unshuffled_deck)
#test = unshuffled_deck.pop()
#print(test)
player_choice = input("Do you want to choose, red [r] or black [b]: ")
#for i in range(len(unshuffled_deck)):
#    print(i, len(unshuffled_deck))
#    unshuffled_deck.pop()

def find_winner():
    card = unshuffled_deck.pop()
    if card==1:
        print(player_choice)
        if player_choice == "r":
            return f"You have won 1$"
        else:
            return f"You have lost 1$"
    else:
        if player_choice == "b":
            return f"You have won 1$"
        else:
            return f"You have lost 1$"


while len(unshuffled_deck) > 1:
    card = unshuffled_deck.pop()
    print(card)
    time.sleep(1)
    if keyboard.is_pressed("q"):
        #print("q pressed, ending loop")
        print(find_winner())
        break

#sample_space = set(itertools.permutations(unshuffled_deck))
#print(f"Sample space for a 52-card deck contains {len(sample_space)} elements")