#Functionality needed: deal_cards, shuffle_cards, discard_card, tally_count, ablity for player to hit or stand might include splitting cards , rules for dealer to play by....

#Global Variables

import random
  

class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val
    
    def show(self):
        print("{} of {}".format(self.val, self.suit))
    
    
class Deck:
    def __init__(self):
       self.cards = []
       self.build()
    
    def build(self):
        for s in ["Spades", "Hearts", "Clubs", "Diamonds"]:
            for v in range(1, 14):
                if v == 1:
                    v = "Ace"
                if v == 11:
                    v = "Jack"
                if v == 12:
                    v = "Queen"
                if v == 13:
                    v = "King"
                self.cards.append(Card(s, v))
    
    def show(self):
       for c in self.cards:
        c.show()
    
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

    def draw(self):
        return self.cards.pop()

class Player:
    def __init__(self, name):
        self.name = name
        self.player_hand = []

    def __str__(self):
        return "your cards are " + str(self.player_hand)
        
    def draw(self, deck):
        if len(self.player_hand) != 2:
            self.player_hand.append(deck.draw())
        
    def showhand(self):
        for card in self.player_hand:
            card.show()

class Dealer:
    def __init__(self):
        self.hand = []
        
    
    def deal(self, deck):
        self.hand.append(deck.draw())
        
    
    def showhand(self):
        for card in self.hand:
            card.show()
        


deck = Deck()
dealer = Dealer()
deck.shuffle()

player_1 = Player("Bob")
dealer.deal(deck)
player_1.draw(deck)


#Game

#print("Hello, please enter your name:")
#player_1 = Player(input())
#print("Welcome "  + str(player_1.name) + "!")

#if len(player_1.playerhand)

#print("Your hand:")
#player_1.showhand()
#print("The dealer has:\nX")
dealer.showhand()
player_1.__str__()


#print("Your cards are " + str(player_1.showhand()))




#dealer.draw(deck)

#dealer.showhand()
#player_1.showhand()