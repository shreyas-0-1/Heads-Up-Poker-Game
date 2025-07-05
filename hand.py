from card import Card

RANK_ORDER = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
SUIT_ORDER = {'♣️':1, '♠️':2, '♥️':3, '♦️':4}
INVERSE_SUIT_ORDER = {1:'♣️', 2:'♠️', 3:'♥️', 4:'♦️'}

class Hand:
    #only for 5 card hands rn

    def __init__(self, myHand=list):
        self.myHand = myHand
        self.bestHand = None
        self.handRanks = list()
        self.handSuits = list()

        for card in myHand:
            self.handRanks.append(RANK_ORDER[card.rank])

        self.handRanks.sort()

        for card in myHand:
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
        highRank = 0

        for card in self.myHand:
            if card.suit == suit and RANK_ORDER[card.rank] > highRank:
                highRank = RANK_ORDER[card.rank]
        
        return ('flush', highRank)
                
    
    def checkStraight(self):
        noCopies = self.handRanks.copy()
        noCopies = sorted(list(set(noCopies)))

        for i in range(0, len(noCopies)-4):
            temp = noCopies[i:i+5]

            if temp[4] - temp[0] == 4:
                return True
        
        return False
    
    def getStraight(self):
        highRank = 0
        noCopies = self.handRanks.copy()
        noCopies = sorted(list(set(noCopies)))
        
        for i in range(len(noCopies)-1, 3, -1): 
            temp = noCopies[i-4:i+1]

            if temp[4] - temp[0] == 4:
                highRank = temp[4]
                break
        
        return ('straight', highRank)
    
    def checkQuads(self):
        for value in RANK_ORDER.values():
            if self.handRanks.count(value) == 4:
                return True
        
        return False
    
    def getQuads(self):
        highRank = self.handRanks[3]

        return ('quads', highRank)

    def checkTrips(self):
        for value in RANK_ORDER.values():
            if self.handRanks.count(value) == 3:
                return True
        
        return False
    
    def getTrips(self):
        reverseRanks = self.handRanks[::-1]
        highRank = 0
        
        for rank in reverseRanks:
            if reverseRanks.count(rank) == 3:
                highRank = rank
                break
        
        return ('trips', highRank)

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

'''cards = [Card('3', '♣️'), Card('2', '♣️'), Card('4', '♣️'), Card('5', '♣️'), Card('A', '♣️'), Card('4', '♣️'), Card('6', '♣️')]
hand = Hand(cards)'''

