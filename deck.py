from card import Card
import random as rand

RANKS = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')
SUITS = ('♣️', '♠️', '♥️', '♦️')
CARDS_LIST = list()

for rank in RANKS:
    for suit in SUITS:
        CARDS_LIST.append(Card(rank, suit))

class Deck:
    def __init__(self):
        self.cards = dict()

    def shuffle(self):
        rand.shuffle(CARDS_LIST)

        for card in CARDS_LIST:
            self.cards[card] = 1

    def display(self):
        temp = ""

        for card in self.cards:
            if self.cards[card] != 0:
                temp = temp + f"{card}, "

        print(temp[:-2])

    def pop(self):
        for card in self.cards:
            if self.cards[card] != 0:
                self.cards.update({card: 0})
                return card