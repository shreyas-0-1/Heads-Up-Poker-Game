from card import Card
from deck import Deck
from besthand import BestHand
from player import Player
import sys
import time


def main():
    buyin, smallBlind, bigBlind = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
    me = Player(list(), buyin, 0, 'You')
    computer = Player(list(), buyin, 1, 'Computer')
    rotation = [me, computer]
    deck = Deck()

    #while me.stack > 0 and computer.stack > 0:
    for player in rotation:
        print(player)

    print("Shuffling and dealing...")
    time.sleep(2)

    deck.shuffle()

    '''deal hole cards'''
    for i in range(2):
        rotation[0].holeCards.append(deck.pop())
        rotation[1].holeCards.append(deck.pop())

    print(f"Your cards are: {me.holeCards}")

    '''start game'''
    pot = 0

    '''preflop'''
    preflopMove = str()

    if me.position == 0:
        print (f"Posting small blind of {smallBlind}...")
        time.sleep(0.75)
    else:
        preflopMove = input("Move?: ")
        
        print(f"Posting big blind of {bigBlind}...")

    for player in rotation:
        pot = pot + player.placeBlinds(smallBlind, bigBlind)

    

    

    '''end: change positions via rotation'''
    for player in rotation:
        player.position = (player.position + 1) % len(rotation)
    
    for player in rotation:
        rotation[player.position] = player


'''
CLI arguments to get buyin, big blind, small blind. 

for as long as player wants or until computer/player goes bankrupt:

    Shuffle the deck, deal card

    Then, round begins:

    Make pot variable

    Player is small, computer big in odd rounds, opposite in even rounds

    Do preflop: player action as SB, and then computer as BB, until preflop done or other way around in even round

    Then, 3 card into flop, and betting

    Then, 4th card as turn, and betting

    Then, 5th card as river and betting

    Finally, evaluate hands, and whoever is higher wins pot
'''