"""
:this is a arrangement for any card game.
:there will be all 52 cards are defined
:will have the ability to shuffle, distribute and show cards
"""


import random


class Cards:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show_cards(self):
        print("{} of {}".format(self.value, self.suit))


class Deck:
    def __init__(self):
        self.cards = []
        self.generate_cards()

    def generate_cards(self):
        for suit in ["Spades", "Clubs", "Hearts", "Diamonds"]:
            for value in range(2, 11):
                self.cards.append(Cards(suit, value))
            for face in ["King", "Queen", "Jack", "Ace"]:
                self.cards.append(Cards(suit, face))

    def show(self):
        for card in self.cards:
            card.show_cards()

    def draw_card(self):
        return self.cards.pop()

    def cut_randomly(self):

        partition = random.randint(2, 52)
        temp1 = self.cards[partition:]
        temp2 = self.cards[: partition]
        self.cards = temp1 + temp2

    def cross_shuffle(self):
        temp1 = self.cards[: int(len(self.cards)/2)]
        temp2 = self.cards[int(len(self.cards)/2):]
        last_index = 25
        for i in range(51, 0, -2):
            self.cards[i] = temp1[last_index]
            last_index -= 1
        for i in range(50, -2, -2):
            self.cards[i] = temp2[last_index]
            last_index -= 1

    def fisher_yates_shuffle(self):
        for i in range(51, 1, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]


class Player:
    def __init__(self, name, chips):
        self.name = name
        self.chips = chips
        self.hand = []

    def draw_cards(self, deck):
        self.hand.append(Deck.draw_card(deck))

    def show(self):
        for card in self.hand:
            card.show_cards()

    def bet(self, amount):
        self.chips = self.chips

DECK_1 = Deck()
DECK_1.fisher_yates_shuffle()

pl = Player("taz", 12000)
deck1 = Deck()
deck1.fisher_yates_shuffle()
pl.draw_cards(deck1)
pl.draw_cards(deck1)
pl.show()





