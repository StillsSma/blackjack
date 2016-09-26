import random

class Player:
    def __init__(self,name,money):
        self.name = name
        self.hand = []
        self.money = money
    def score(self):
        self.points =  sum(card.value for card in self.hand)
        return self.points
class Card:

    def __init__(self,number,suit):
        self.number = number
        self.suit = suit
        if number > 9:
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


def check_ace(card):
    if card.number == 1:
        ace = input("Is your ace worth 11 or 1? ")
        if ace == "11":
            card.value = 11
        elif ace == "1":
            card.value = 1
        else:
            print("not a valid answer")


def display_hand(player):
    for card in player.hand:
        print (card.number,card.suit)
    print("Your total is {}".format(player.score()))

def player_turn(player,deck):
    choice = input("hit or stand? ")
    if choice == "hit":
        player.hand.append(deal(deck))
        display_hand(player)
        check_ace(player.hand[-1])
        if player.points > 21:
            print ("you bust")
            exit()
        elif player.points == 21:
            print ("You've got Black Jack!")
            next_round()
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

def next_round():
    answer = input("Play again? y/n ")
    if answer == "y":
        game()
    elif answer == "n":
        exit()
    else:
        print("Not a valid answer")
        next_round()


def game():
    deck = Deck()
    deck.shuffler()
    player = Player("sam", 100)
    dealer = Player("dealer",100)

    players = [player,dealer]

    print("Welcome to Black Jack! Place your bet.")
    bet = int(input("How much would you like to bet? "))
    for people in players:
        for x in range(2):
            people.hand.append(deal(deck))
    display_hand(player)
    if player.points == 21:
        print("Black Jack!")
        next_round()
    else:
        pass
    print("Dealer is showing")
    print (dealer.hand[0].number, dealer.hand[0].suit)
    player_turn(player,deck)
    dealer_turn(dealer,deck)
    
    if player.points > dealer.points:
        print("You Win")
    elif dealer.points > player.points:
        print("You Lose")
    else:
        print("Tie")

    next_round()
















game()
