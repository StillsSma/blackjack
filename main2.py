import random

class Player:
    def __init__(self,name):
        self.name = name
        self.hand = []
    def score(self):
        self.points =  sum(card.value for card in self.hand)
        return self.points
class Card:

    def __init__(self,number,suit):
        self.number = number
        self.suit = suit
        if number == 1:
            self.ace = True
        else:
            self.ace = False
        if number > 9 and number > 1:
            self.value = 10
        elif number > 1 and number < 10:
            self.value = number
        else:
            self.value = 11


class Deck:

    def __init__(self):
        suits = ["hearts","clubs","spades","diamonds"]
        self.deck = [Card(x,suit) for suit in suits for x in range(1,14)]

    def shuffler (self):
        random.shuffle(self.deck)


def display_hand(player):
    for card in player.hand:
        print (card.number,card.suit)
    print(player.score())

def player_turn(player,deck):
    choice = input("hit or stand? ")
    if choice == "hit":
        player.hand.append(deal(deck))
        display_hand(player)
        if player.points > 21:
            print ("you lose")
            exit()
        else:
            player_turn(player,deck)
    elif choice == "stand":
        pass
    else:
        print("That is not a valid move")
        player_turn(player,deck)


def dealer_turn(dealer,deck):
    if dealer.score() < 17:
        dealer.hand.append(deal(deck))
    else:
        pass

def deal(deck):
    deal = deck.deck.pop()
    return deal

def end_game(player,dealer,deck):
    if player.points > dealer.points:
        print("You Win")
    elif dealer.points > player.points:
        print("You Lose")
    else:
        print("Tie")

def game():
    deck = Deck()
    deck.shuffler()
    player = Player("sam")
    dealer = Player("dealer")

    players = [player,dealer]

#Deal cards
    for people in players:
        for x in range(2):
            people.hand.append(deal(deck))
    display_hand(player)
    player_turn(player,deck)
    dealer_turn(dealer,deck)
    end_game(player,dealer,deck)
















game()
