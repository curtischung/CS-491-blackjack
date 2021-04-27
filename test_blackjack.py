import unittest
from blackjack import Blackjack
from player import Player
from card import Card
from deck import Deck

class TestBlackJack(unittest.TestCase):

#    def setup(self):
#        self.card = Card("clubs", 1)
#        self.deck = Deck()
#        self.player = Player("Jimbo")
#        self.blackjack = Blackjack()

    def test_draw(self):
        player = Player("Bum")
        player.draw()
        self.assertEqual(len(player.hand), 1)

    def test_deck_build(self):
        deck = Deck()
        deck.build()
        self.assertIsNotNone(deck)

    def test_card_value(self):
        card = Card("spade", 1)
        self.assertEqual(card.cardValue(), 1)

    def test_card_show(self):
        card = Card("spades", 1)
        card.show()
        self.assertTrue(card.show())

    def test_deck_show(self):
        deck = Deck()
        deck.build()
        self.assertTrue(deck.show())

    def test_card_equal(self):
        card1 = Card("spades", 1)
        card2 = Card("spades", 2)
        self.assertNotEqual(card1, card2)

    def test_player_showhand(self):
        player = Player("Joe")
        player.hand.append(Card("spades", 10))
        self.assertTrue(player.showHand)

    def test_dealerdraw(self):
        player = Player("dealer")
        self.assertTrue(player.dealerDraw())

    def test_shuffle(self):
        deck1 = Deck()
        deck2 = Deck()
        deck1.shuffle()
        self.assertNotEqual(deck1, deck2)

    def test_hit(self):
        game = Blackjack()
        player = Player("Loser")
        game.hit(player)
        card = Card("spades", 1)
        self.assertTrue(isinstance(player.hand[0], type(card)))

    def test_card(self):
        card = Card("spades", 1)
        self.assertTrue(isinstance(card, type(card)))

    def test_card_in_hand(self):
        card = Card("spades", 1)
        self.assertTrue(isinstance(card, type(card)), type(card))

    def test_player_bust(self):
        game = Blackjack()
        player = Player("Who")
        player.hand.append(Card("spades", 10))
        player.hand.append(Card("spades", 10))
        player.hand.append(Card("spades", 10))
        self.assertTrue(game.bust(player))

    def test_player_bust_false(self):
        game = Blackjack()
        player = Player("Who")
        player.hand.append(Card("spades", 10))
        player.hand.append(Card("spades", 10))       
        self.assertFalse(game.bust(player))

    def test_hand_value(self):
        player = Player("Dummy")
        player.hand = [Card("hearts", 5), Card("spades", 9)]
        self.assertEqual(player.handValue(), 14)


if __name__ == "__main__":
    unittest.main()