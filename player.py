from card import Card

class Player:
    def __init__(self, holeCards:list[Card], stack:int, position:int, name:str):
        self.name = name
        self.holeCards = holeCards
        self.stack = stack
        self.position = position
    
    def __str__(self):
        return f'{self.name}: {self.stack}'
    
    def __repr__(self):
        return f"Player({self.stack} at {self.position})"
    
    def __eq__(self, other):
        return self.holeCards == other.holeCards and self.stack == other.stack and self.position == other.position
    
    def __hash__(self):
        return hash((self.holeCards, self.stack, self.position))
    
    #factor in stack size later
    def placeBlinds(self, sb, bb):
        if self.position == 0:
            self.stack = self.stack - sb
            return sb
        else:
            self.stack = self.stack - bb
            return bb
    
    def fold(self):
        self.holeCards = None
        return 0
    
    def check(self):
        return 0

    def call(self, amount):
        self.stack = self.stack - amount
        return amount

    def bet(self, amount):
        self.stack = self.stack - amount
        return amount