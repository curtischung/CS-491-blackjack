from card import Card
import random

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle()

    def build(self):
        for i in ["Spades", "Clubs", "Diamonds", "Hearts"]:
            for j in range(1, 14):
                self.cards.append(Card(i,j))

    def show(self):
        for c in self.cards:
            c.show()
        return True

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()

if __name__ == "__main__":  
    deck = Deck()
    deck.show()
    deck.shuffle()
    print("==================================")
    deck.show()
