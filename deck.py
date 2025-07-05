from card import Card
import random as rand

RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
SUITS = ('♣️', '♠️', '♥️', '♦️')

class Deck:
    def __init__(self):
        self.deck = list()

        for rank in RANKS:
            for suit in SUITS:
                self.deck.append(Card(rank, suit))

    def display(self):
        temp = ""

        for card in self.deck:
            temp = temp + f"{card}, "

        print(temp[:-2])
            

    def shuffle(self):
        rand.shuffle(self.deck)