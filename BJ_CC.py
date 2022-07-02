#Functionality needed: deal_cards, shuffle_cards, discard_card, tally_count, ablity for player to hit or stand might include splitting cards , rules for dealer to play by....

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

    def __getitem__(self, game_val):
        return self.game_val

        
class Deck:
    def __init__(self):
         self.cards = []
         self.build()
         self.shuffle()
    
    def build(self):
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
        
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            rand = random.randint(0, i)
            self.cards[i], self.cards[rand] = self.cards[rand], self.cards[i]

    def deal(self):
        if len(self.cards) == 0:
            self.build()
        return self.cards.pop() 

class Hand:
    def __init__(self, card1, card2, card3, card4):
        self.cards = [card1,card3]
        self.dealer_cards = [card2, card4]

    def __repr__(self):
        return str(self.cards)

    def __str__(self):
        return str(self.cards)

    def aces(self, card):
        ace = 1
        if card[2] == 1:
            print("Would you like the ace to have a value of 1 or 11?")
            game_value = input()
            if game_value == str(11):
                ace += 9
                return ace
            
        return ace

    def dealer_ace(self):
        ace = 10
        return ace

    def get_score(self):
        total = 0
        for card in self.cards:
            if card[2] == 1:
                total += int(self.aces(card))
            total += card[2]

        return total
    
    
    def dealer_score(self):
        total = 0
        for card in self.dealer_cards:
            if card[2] == 1:
                total += self.dealer_ace()
            total += card[2]
        return total
    
    def dealer_total(self):
        dealer_total = self.dealer_score()
        while dealer_total <= 16:
            self.dealer_hit(deck.deal())
            new_card = self.dealer_cards[-1]
            if new_card[2] == 1:
                new_card[2] = self.dealer_ace()
                dealer_total += int(new_card[2])
            dealer_total += int(new_card[2])
            print("\nDealer now has:\nX and a", str(self.dealer_cards[1:]))
        return dealer_total

    def player_total(self):
        player_total = self.get_score()
        while player_total < 21:
            print("\nHit or stand?\n")
            player_action = input()
            if player_action == "hit":
                self.player_hit(deck.deal())
                print("\nYour cards are:\n")
                print(self.cards)
                new_card = self.cards[-1]
                if new_card[2] == 1:
                    ace = self.aces()
                    player_total += ace
                player_total += int(new_card[2])
            else:
                break
        return player_total

    def winner(self):
        dealer_score = self.dealer_total() 
        player_score = self.player_total()      
        if player_score > dealer_score and player_score <= 21:
            print("\nYou Win!\n")
            print(str(player_score), str(dealer_score))
        elif player_score > 21:
            print("\nYou busted!\n")
            print(str(player_score), str(dealer_score))
        elif dealer_score > 21:
            print("\nDealer busted. You Win!\n")
            print(str(player_score), str(dealer_score))
        else:
            print("\nDealer Wins!\nBetter luck next time!\n")
            print(str(player_score), str(dealer_score))
        
    def new_hand(self, card):
        card1 = deck.deal()
        card2 = deck.deal()
    
    def player_hit(self, card):
        self.cards.append(card)
    
    def dealer_hit(self, card):
        self.dealer_cards.append(card)
            
        
class Player:
    def __init__(self, name):
        self.name = name
        self.player_hand = []

    def __repr__(self):
        return str(self.player_hand)

    def __str__(self):
        return str(self.player_hand)
        
    def add_hand(self, hand):
        self.player_hand = hand 
        return self.player_hand

    def hit(self, card):
            self.player_hand.player_hit(card)
    
    def get_hand(self):
        return self.player_hand
    
    def discard(self,hand):
        self.player_hand = hand
        self.player_hand = []
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
    
    def get_hand(self):
        return self.hand
    
    def discard(self,hand):
        self.hand = hand
        self.hand = []
        return self.hand
                

#Game
print("Hello, please enter your name:\n")
player_1 = Player(input())
print("\nWelcome "  + str(player_1.name) + "!")
deck = Deck()
dealer = Dealer()
deck.shuffle()


       
            
def start():
    while True:
        hand = Hand(deck.deal(), deck.deal(), deck.deal(), deck.deal())
        dealer_hand = hand.dealer_cards
        player_hand = hand.cards
        dealer.add_hand(dealer_hand)
        player_1.add_hand(player_hand)
        
        print("\nYour cards are:\n" )

        print(player_1)

        print("\nThe dealer has:\n\nX and a",str(dealer_hand[1]),"\n")
             
        hand.winner()
        
        

        print(player_hand)
        print(dealer_hand)
        
        
        
        print("\n\nPlay another hand?\n")
        
        end_game = input()

        
        if end_game == "yes":
            hand = Hand(deck.deal(), deck.deal(), deck.deal(), deck.deal())
            dealer_hand = hand.dealer_cards
            player_hand = hand.cards
            dealer.add_hand(dealer_hand)
            player_1.add_hand(player_hand)

            continue
        else:
            break



start()

