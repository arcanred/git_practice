#Functionality needed: deal_cards, shuffle_cards, discard_card, tally_count, ablity for player to hit or stand might include splitting cards , rules for dealer to play by....

#Global Variables

import random
  

class Card:
    def __init__(self, suit, val, game_val):
        self.suit = suit
        self.val = val
        self.game_val = game_val
            
    def __repr__(self):
        return "{} of {}".format(self.val, self.suit)

    def __str__(self):
        return "{} of {}".format(self.val, self.suit)

    def get_game_val():
        return self.game_value

    
        
        
class Deck:
    def __init__(self):
         self.cards = []
         self.build()
         
    
    def build(self):
        self.shuffle()

        for s in ["Spades", "Hearts", "Clubs", "Diamonds"]:
            for v in range(1, 14):
                gv = v
                if gv > 10:
                    gv = 10
                if v == 1:
                    v = "Ace"
                if v == 11:
                    v = "Jack"
                if v == 12:
                    v = "Queen"
                if v == 13:
                    v = "King"
                self.cards.append(Card(s, v, gv))
    
    def show(self):
       for c in self.cards:
        c.show()
    
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

    def deal(self):
        if len(self.cards) == 0:
            self.build()
        return self.cards.pop() 

class Hand:
    def __init__(self, card1, card2):
        self.cards = [card1, card2]
        
    def __repr__(self):
        return str(self.cards)

    def __str__(self):
        return str(self.cards)

    def get_scores(self):
        total = 0
        for card in self.cards:
            new_total = 0
            for value in total:
                new_total += (card.game_val() + value)
            
            total = new_total
        
        return total
    
    def new_hand(self, card):
        card1 = deck.deal()
        card2 = deck.deal()



class Player:
    def __init__(self, name):
        self.name = name
        self.player_hand = []

    def __repr__(self):
        return "your cards are " + str(self.player_hand)

    def __str__(self):
        return "your cards are " + str(self.player_hand)
        
    def add_hand(self, hand):
        self.player_hand = hand 
        return self.player_hand

class Dealer:
    def __init__(self):
        self.hand = []
        
    def __repr__(self):
        return str(self.hand)

    def __str__(self):
        return str(self.hand)
    
    def add_hand(self, hand):
        self.hand = hand 
        return self.hand
         
deck = Deck()
dealer = Dealer()
deck.shuffle()
hand = Hand(deck.deal(), deck.deal())

player_1 = Player("Bob")
#dealer.deal(deck)
#player_1.draw(deck)
player_1.add_hand(hand)
dealer.add_hand(hand)
#Game

#print("Hello, please enter your name:")
#player_1 = Player(input())
#print("Welcome "  + str(player_1.name) + "!")

#if len(player_1.playerhand)

#print("Your hand:")
#player_1.showhand()
#print("The dealer has:\nX")
print(dealer)
print(player_1)
#player_1.__str__()


#print("Your cards are " + str(player_1.showhand()))




#dealer.draw(deck)

#dealer.showhand()
#player_1.showhand()