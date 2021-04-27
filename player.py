from card import Card
from deck import Deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.deck = Deck()
        self.hidden = False

    def draw(self):
        self.hand.append(self.deck.drawCard())
        return self

    def showHand(self):
        for cards in self.hand:   
            cards.show()
        return True
    
    def handValue(self):
        total = 0
        for card in self.hand:
            if card.cardValue() >= 11:
                total += 10
            elif card.cardValue == 1:
                total += 11
                if total > 21:
                    total -= 10
            else:
                total += card.cardValue()
        return total

    def dealerDraw(self):
        self.hand.append(self.deck.drawCard())
        self.hand.append(self.deck.drawCard())
        self.hidden = True
        return True
        
    def showDealerHand(self):
        i = 0
        for cards in self.hand:   
            if i == 1 and self.hidden == True:
                print("Face Down Card")
            elif cards == 0:
                cards.show()
                self.hidden = False
            else:
                cards.show()

            i+=1
        return True
    
    def playerStandDraw(self):
        self.hidden = False
        if self.handValue() < 17:
            self.hand.append(self.deck.drawCard())
            return False
        else:
            return True