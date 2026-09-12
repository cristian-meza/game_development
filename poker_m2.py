# POKER MARK II

import random



class Card:
    def __init__(self, rank, value, suite):
        self.rank = rank
        self.value = value
        self.suite = suite
        
class Deck:
    
    def __init__(self):
        self.create = []
        
        values = {
        'Two' : 2,
        'Three' : 3,
        'Four' : 4,
        'Five' : 5,
        'Six' : 6,
        'Seven' : 7,
        'Eight' : 8,
        'Nine' : 9,
        'Ten' : 10,
        'Jack' : 11,
        'Queen' : 12,
        'King' : 13,
        'Ace' : 14
        }

        suites = ("Hearts", "Spades", "Diamonds", "Clubs")
        
        for suite in suites:
            for rank, value in values.items():
                self.create.append((rank, value, suite))
        
        
        
    def shuffle(self):
        return random.shuffle(self)
        
                
                
deck = Deck()

deck = deck.create



print(deck.shuffle())




            
        
    
    
