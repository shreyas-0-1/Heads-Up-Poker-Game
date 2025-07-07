from card import Card

#dicts that map rank to its value and suit to number
RANK_ORDER = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
SUIT_ORDER = {'♣️':1, '♠️':2, '♥️':3, '♦️':4}

#inverses of above dicts
INVERSE_RANK_ORDER = dict()
for i in range(13):
    INVERSE_RANK_ORDER[list(RANK_ORDER.values())[i]] = list(RANK_ORDER.keys())[i]

INVERSE_SUIT_ORDER = {1:'♣️', 2:'♠️', 3:'♥️', 4:'♦️'}

class BestHand:
    def __init__(self, playerHand=list):
        self.playerHand = playerHand
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

    def getHighCard(self):
        copy = self.playerHand.copy()
        bestHighCard = copy[0:5]

        return ('high card', bestHighCard)

    def checkFlush(self):
        if self.handSuits.count('♣️') >= 5 or self.handSuits.count('♠️') >= 5 or self.handSuits.count('♥️') >= 5 or self.handSuits.count('♦️') >= 5:
            return True
        
        return False
    
    def getFlush(self):
        if self.checkFlush():
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
        
        return None      
    
    def checkStraight(self):
        if 14 in self.handRanks and 2 in self.handRanks and 3 in self.handRanks and 4 in self.handRanks and 5 in self.handRanks and not 6 in self.handRanks:
            return True

        noCopies = self.handRanks.copy()
        noCopies = sorted(list(set(noCopies)))

        for i in range(0, len(noCopies)-4):
            temp = noCopies[i:i+5]

            if temp[4] - temp[0] == 4:
                return True
        
        return False
    
    def getStraight(self):
        if self.checkStraight():
            bestStraight = list()
            copy = self.playerHand.copy()

            if 14 in self.handRanks and 2 in self.handRanks and 3 in self.handRanks and 4 in self.handRanks and 5 in self.handRanks and  6 not in self.handRanks:
                indexA = self.handRanks.index(14)
                index2 = self.handRanks.index(2)
                index3 = self.handRanks.index(3)
                index4 = self.handRanks.index(4)
                index5 = self.handRanks.index(5)

                bestStraight = [self.playerHand[index5], self.playerHand[index4], self.playerHand[index3], self.playerHand[index2], self.playerHand[indexA]]
                return ('straight', bestStraight)
            
            i = 0
            while i < len(copy):
                k = i + 1
                while k < len(copy):
                    if copy[i].rank == copy[k].rank:
                        copy.pop(k)
                        k = k - 1
                    k = k + 1
                
                i = i + 1
            
            for j in range(len(copy) - 4):
                if RANK_ORDER[copy[j].rank] - RANK_ORDER[copy[j + 4].rank] == 4:
                    bestStraight = copy[j:j + 5]
                    break

            return ('straight', bestStraight)
        
        return None
    
    def checkQuads(self):
        for rank in self.handRanks:
            if self.handRanks.count(rank) == 4:
                return True
        
        return False
    
    def getQuads(self):
        if self.checkQuads():
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
        
        return None

    def checkTrips(self):
        for rank in self.handRanks:
            if self.handRanks.count(rank) == 3:
                return True
        
        return False
    
    def getTrips(self):
        if self.checkTrips():
            highRank = str()
            bestTrips = list()
            copy = self.playerHand.copy()

            for i in range(len(self.playerHand) - 2):
                if RANK_ORDER[self.playerHand[i].rank] - RANK_ORDER[self.playerHand[i + 2].rank] == 0:
                    highRank = self.playerHand[i].rank
                    break

            i = 0
            while i < len(copy):
                if copy[i].rank == highRank:
                    bestTrips.append(copy.pop(i))
                    i = i - 1

                i = i + 1

            bestTrips.append(copy.pop(0))
            bestTrips.append(copy.pop(0))

            return ('trips', bestTrips)
        
        return None

    def checkPair(self):
        for rank in self.handRanks:
            if self.handRanks.count(rank) == 2:
                return True
        
        return False
    
    def getPair(self):
        if self.checkPair():
            highRank = str()
            bestPair = list()
            copy = self.playerHand.copy()

            for i in range(len(self.playerHand) - 1):
                if RANK_ORDER[self.playerHand[i].rank] - RANK_ORDER[self.playerHand[i + 1].rank] == 0:
                    highRank = self.playerHand[i].rank
                    break

            i = 0
            while i < len(copy):
                if copy[i].rank == highRank:
                    bestPair.append(copy.pop(i))
                    i = i - 1

                i = i + 1

            bestPair.append(copy.pop(0))
            bestPair.append(copy.pop(0))
            bestPair.append(copy.pop(0))

            return ('pair', bestPair)
        
        return None
    
    def check2Pair(self):
        ranksAppearTwice = list()

        for rank in self.handRanks:
            if self.handRanks.count(rank) == 2 and rank not in ranksAppearTwice:
                ranksAppearTwice.append(rank)

        if len(ranksAppearTwice) > 1: return True

        return False
    
    def get2Pair(self):
        if self.check2Pair():
            copy = self.playerHand.copy()
            best2Pair = list()

            pair = self.getPair()[1][0:2]
            
            for card in pair:
                best2Pair.append(card)
                copy.remove(card)

            for i in range(len(copy) - 1):
                if RANK_ORDER[copy[i].rank] - RANK_ORDER[copy[i + 1].rank] == 0:
                    best2Pair.append(copy[i])
                    best2Pair.append(copy[i + 1])
                    break
            
            best2Pair.append(copy[0])

            return ('two pair', best2Pair)
        
        return None

    def checkBoat(self):
        copy = self.handRanks
        ranksAppearThrice = list()
        ranksAppearTwice = list()

        for rank in copy:
            if copy.count(rank) >= 3 and rank not in ranksAppearThrice:
                ranksAppearThrice.append(rank)

        if len(ranksAppearThrice) > 1: return True
        
        for rank in copy:
            if copy.count(rank) >= 2 and rank not in ranksAppearThrice and rank not in ranksAppearTwice:
                ranksAppearTwice.append(rank)

        if len(ranksAppearThrice) == 1 and len(ranksAppearTwice) >= 1: return True

        return False
    
    def getBoat(self):
        if self.checkBoat():
            copy = self.playerHand.copy()
            bestBoat = list()

            trips = self.getTrips()[1][0:3]
            
            for card in trips:
                bestBoat.append(card)
                copy.remove(card)

            for i in range(len(copy) - 1):
                if RANK_ORDER[copy[i].rank] - RANK_ORDER[copy[i + 1].rank] == 0:
                    bestBoat.append(copy[i])
                    bestBoat.append(copy[i + 1])
                    break
            
            return ('full house', bestBoat)
        
        return None
    
    def checkSFlush(self):
        if self.checkFlush():
            flush = list()
            suit = self.getFlush()[1][0].suit 

            for card in self.playerHand:
                if card.suit == suit:
                    flush.append(card)

            if Card('A', suit) in flush and Card('2', suit) in flush and Card('3', suit) in flush and Card('4', suit) in flush and Card('5', suit) in flush and Card('6', suit) not in flush:
                return True

            for i in range(len(flush) - 4):
                if RANK_ORDER[flush[i].rank] - RANK_ORDER[flush[i + 4].rank] == 4:
                    return True
        
        return False

    def getSFlush(self):
        if self.checkSFlush():
            suit = self.getFlush()[1][0].suit
            bestSFlush = list()

            for card in self.playerHand:
                if card.suit == suit:
                    bestSFlush.append(card)

            if Card('A', suit) in bestSFlush and Card('2', suit) in bestSFlush and Card('3', suit) in bestSFlush and Card('4', suit) in bestSFlush and Card('5', suit) in bestSFlush and Card('6', suit) not in bestSFlush:
                    length = len(bestSFlush)
                    copy = bestSFlush.copy()
                    bestSFlush = [copy[length - 4], copy[length - 3], copy[length - 2], copy[length - 1], copy[0]]
                    return ('straight flush', bestSFlush)

            for i in range(len(bestSFlush)-4):
                if RANK_ORDER[bestSFlush[i].rank] - RANK_ORDER[bestSFlush[i + 4].rank] == 4:
                    bestSFlush = bestSFlush[i:i + 5]
                    break
            
            return ('straight flush', bestSFlush)
        
        return None

    def checkRFlush(self):
        if self.checkSFlush():
            SFlush = self.getSFlush()[1]

            if SFlush[0].rank == 'A':
                return True
            
        return False

    def getRFlush(self):
        if self.checkRFlush():
            RFlush = self.getSFlush()[1]

            return ('royal flush', RFlush)
        
        return None
    
    def evaluate(self):
        ladder = (
            self.getRFlush(),
            self.getSFlush(),
            self.getQuads(),
            self.getBoat(),
            self.getFlush(),
            self.getStraight(),
            self.getTrips(),
            self.get2Pair(),
            self.getPair(),
            self.getHighCard()
        )

        for hand in ladder:
            if hand is not None:
                return hand
        
        return None 