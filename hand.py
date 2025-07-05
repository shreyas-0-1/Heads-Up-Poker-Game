from card import Card

#dicts that map rank to its value and suit to number
RANK_ORDER = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
SUIT_ORDER = {'♣️':1, '♠️':2, '♥️':3, '♦️':4}

#inverses of above dicts
INVERSE_RANK_ORDER = dict()
for i in range(13):
    INVERSE_RANK_ORDER[list(RANK_ORDER.values())[i]] = list(RANK_ORDER.keys())[i]

INVERSE_SUIT_ORDER = {1:'♣️', 2:'♠️', 3:'♥️', 4:'♦️'}

class Hand:
    def __init__(self, playerHand=list):
        self.playerHand = playerHand
        #self.bestHand = None
        self.handRanks = list()
        self.handSuits = list()

        #<playerHand> lists player's Cards in descending order
        for i in range(len(self.playerHand)):
            for k in range(i + 1, len(self.playerHand)):
                if self.playerHand[i] < self.playerHand[k]:
                    self.playerHand[i], self.playerHand[k] = self.playerHand[k], self.playerHand[i]

        #<handRanks> lists player's cards' ranks in descending order
        for card in playerHand:
            self.handRanks.append(RANK_ORDER[card.rank])

        self.handRanks.sort(reverse=True)


        #<handSuits> lists player's cards' suits in order c, s, h, d
        for card in playerHand:
            self.handSuits.append(SUIT_ORDER[card.suit])

        self.handSuits.sort()

        for i in range(0, len(self.handSuits)):
            self.handSuits[i] = INVERSE_SUIT_ORDER[self.handSuits[i]]

    def checkFlush(self):
        if self.handSuits.count('♣️') >= 5 or self.handSuits.count('♠️') >= 5 or self.handSuits.count('♥️') >= 5 or self.handSuits.count('♦️') >= 5:
            return True
        
        return False
    
    def getFlush(self):
        suit = self.handSuits[3]
        bestFlush = list()

        for card in self.playerHand:
            if card.suit == suit:
                bestFlush.append(card)

        for i in range(len(bestFlush)):
            for k in range(i + 1, len(bestFlush)):
                if bestFlush[i] < bestFlush[k]:
                    bestFlush[i], bestFlush[k] = bestFlush[k], bestFlush[i]

        while len(bestFlush) > 5:
            bestFlush.pop(len(bestFlush) - 1)
        
        return ('flush', bestFlush)
                
    
    def checkStraight(self):
        noCopies = self.handRanks.copy()
        noCopies = sorted(list(set(noCopies)))
        print(noCopies)

        for i in range(0, len(noCopies)-4):
            temp = noCopies[i:i+5]

            if temp[4] - temp[0] == 4:
                return True
        
        return False
    
    def getStraight(self):
        copy = self.playerHand.copy()
        
        i = 0
        while i < len(copy):
            k = i + 1
            while k < len(copy):
                if copy[i].rank == copy[k].rank:
                    copy.pop(k)
                    k = k - 1
                k = k + 1
            
            i = i + 1
        
        bestStraight = list()
        for j in range(len(copy) - 4):
            if RANK_ORDER[copy[j].rank] - RANK_ORDER[copy[j + 4].rank] == 4:
                bestStraight = copy[j:j + 5]
                break

        return ('straight', bestStraight)
    
    def checkQuads(self):
        for rank in self.handRanks:
            if self.handRanks.count(rank) == 4:
                return True
        
        return False
    
    def getQuads(self):
        highRank = INVERSE_RANK_ORDER[self.handRanks[3]]
        copy = self.playerHand.copy()
        bestQuads = list()

        i = 0
        while i < len(copy):
            if copy[i].rank == highRank:
                bestQuads.append(copy.pop(i))
                i = i -1

            i = i + 1

        bestQuads.append(copy.pop(0))
        
        return ('quads', bestQuads)

    def checkTrips(self):
        for rank in self.handRanks:
            if self.handRanks.count(rank) == 3:
                return True
        
        return False
    
    def getTrips(self):
        highRank = str()
        bestTrips = list()
        copy = self.playerHand.copy()

        print(self.playerHand)
        for i in range(len(self.playerHand) - 2):
            if RANK_ORDER[self.playerHand[i].rank] - RANK_ORDER[self.playerHand[i + 2].rank] == 0:
                highRank = self.playerHand[i].rank

        i = 0
        while i < len(copy):
            if copy[i].rank == highRank:
                bestTrips.append(copy.pop(i))
                i = i - 1

            i = i + 1

        bestTrips.append(copy.pop(0))
        bestTrips.append(copy.pop(0))

        return ('trips', bestTrips)

    def checkPair(self):
        for value in RANK_ORDER.values():
            if self.handRanks.count(value) == 2:
                return True
        
        return False
    
    def getPair(self):
        reverseRanks = self.handRanks[::-1]
        highRank = 0
        
        for rank in reverseRanks:
            if reverseRanks.count(rank) == 2:
                highRank = rank
                break
        
        return ('pair', highRank)
    
    def check2Pair(self):
        if self.checkPair():
            firstPair = self.getPair()[1]
            temp = self.handRanks.copy()

            while firstPair in temp:
                temp.remove(firstPair)

            for value in RANK_ORDER.values():
                if temp.count(value) == 2:
                    return True
        
        return False
    
    def get2Pair(self):
        temp = self.getPair()
        highRank = temp[1]

        return ('2 pair', highRank)

    def checkBoat(self):
        if self.checkTrips():
            trips = self.getTrips()[1]
            temp = self.handRanks.copy()

            while trips in temp:
                temp.remove(trips)

            for value in RANK_ORDER.values():
                if temp.count(value) == 2:
                    return True
        
        return False
    
    def getBoat(self):
        temp = self.getTrips()
        highRank = temp[1]

        return ('full house', highRank)
    
    '''def checkSFlush(self):
        if self.checkFlush() and self.checkStraight():
            highStraight = self.getStraight()[1]
            
        return False'''

#testing
cards = [Card('2', '♣️'), Card('2', '♣️'), Card('A', '♣️'), Card('2', '♦️'), Card('3', '♦️'), Card('5', '♣️'), Card('A', '♦️')]
hand = Hand(cards)
print(hand.handRanks)
print(hand.getTrips())

