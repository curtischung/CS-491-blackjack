from player import Player
from deck import Deck
from card import Card

class Blackjack:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Player("Dealer")
        self.playerWin = False
        self.dealerWin = False
        self.stand = False

    def deal(self):
        self.player.draw()
        self.player.draw()
        self.dealer.dealerDraw()

    def bust(self, player):
        total = player.handValue()

        if(total > 21):
            return True
        else:
            return False

    def hit(self, player):
        player.draw()


    def showHand(self, player):
        print("=================")
        print("{} shows: ".format(player.name))
        player.showHand()
        print("Total Points: {}".format(player.handValue()))
        print()
        return True

    def showDealerHand(self, player):
        print("=================")
        print("{} shows: ".format(player.name))
        player.showDealerHand()
        print()
        return True

    def playerStand(self):
        self.dealer.playerStandDraw()
        return True

    def checkWin(self):
        if self.player.handValue() > self.dealer.handValue() and not self.bust(self.player) :
            print("Player has won!")
        elif self.player.handValue() < self.dealer.handValue() and not self.bust(self.player):
            print("Dealer has won!")
        elif self.player.handValue() == self.dealer.handValue():
            print("Tie!")
        elif(self.bust(self.player) is True):
            print("Player busts, Dealer wins!")
        elif(self.bust(self.dealer) is True):
            print("Dealer busts, Player wins!")
        return True



if __name__ == "__main__":  
    blackjack = Blackjack()
    blackjack.deal()
    print("======Initial Hand======")

    stand = False

    while(blackjack.bust(blackjack.player) == False and stand == False and blackjack.bust(blackjack.dealer) == False):
        

        blackjack.showHand(blackjack.player)
        blackjack.showDealerHand(blackjack.dealer)

        action = input("Hit or stand?\n 1. Hit 2. Stand\n")
        print("\n\n\n")
        if action == "1":
            blackjack.hit(blackjack.player)

        elif action == "2":
            blackjack.playerStand()
            stand = True
    
    blackjack.showHand(blackjack.player)
    if(blackjack.bust(blackjack.player) == False):
        blackjack.showHand(blackjack.dealer)
    else:
        blackjack.showDealerHand(blackjack.dealer)
    blackjack.checkWin()


    

