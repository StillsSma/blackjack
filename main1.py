import random

class Card:

    def __init__(self,number,suit):
        self.number = number
        self.suit = suit
        if number > 8:
            self.value = 10
        elif number > 0 and number < 9:
            self.value = number
        else:
            self.value = 11


class Deck:

    def __init__(self):
        suits = ["hearts","clubs","spades","diamonds"]
        self.deck = [(suit,x) for suit in suits for x in range(13)]

    def shuffler (self):
        random.shuffle(self.deck)




def deal(deck):
    dealt_card = []
    for x in range(2):
        deal = deck.deck.pop()
        dealt_card.append(deal)
    return dealt_card

def game():
    deck = Deck()
    deck.shuffler()
    deal(deck)
    print(deal(deck))

    #card = Card(dealt_card[1],dealt_card[0])

    #print (card.value)


game()
