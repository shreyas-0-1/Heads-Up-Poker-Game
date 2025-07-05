RANK_ORDER = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}

class Card:
    def __init__(self, rank:str, suit:str):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit}" 
    
    def __repr__(self):
        return f"Card({self.rank}{self.suit})"
    
    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit
    
    def __hash__(self):
        return hash((self.rank, self.suit))
    
    def __lt__(self, other):
        return RANK_ORDER[self.rank] < RANK_ORDER[other.rank]