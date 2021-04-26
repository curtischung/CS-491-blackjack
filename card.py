class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def cardValue(self):
        return self.value

    def show(self):
        if(self.value == 11):
            print("{} of {}".format("Jack", self.suit))
        elif(self.value == 12):
            print("{} of {}".format("Queen", self.suit))
        elif(self.value == 13):
            print("{} of {}".format("King", self.suit))
        elif(self.value == 1):
            print("{} of {}".format("Ace", self.suit))
        else:
            print("{} of {}".format(self.value, self.suit))
