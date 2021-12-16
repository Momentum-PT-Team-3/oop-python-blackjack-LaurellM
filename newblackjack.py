import random

SUITS = ["♥️", "♦️", "☘️", "♠️"]
SCORES = {2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6, 7 : 7, 8 : 8, 9 : 9, 10 : 10, "J" : 10, "Q" : 10, "K" : 10, "A" : 1}

class Player:
    def __init__(self):
        self.name = input("What's your name? ")
        self.hand = []
    
    def __str__(self):
        return self.name

    def show_hand(self):
        print(self.name)
        for card in self.hand:
            print(card)
            
class Dealer:
    def __init__(self):
        self.hand = []

    def __str__(self):
        return "Dealer"

    def show_hand(self):
        print("Dealer")
        for card in self.hand:
            print(card)

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.score= self.calculate_value(self.rank)
        
    def __str__(self):
        return f'{self.rank} of {self.suit} {self.score}'

    def calculate_value(self, rank):
        values_dictionary = {
            2:2,
            3:3,
            4:4,
            5:5,
            6:6,
            7:7, 
            8:8,
            9:9,
            10:10,
            "J":10,
            "Q":10, 
            "K":10,
            "A":1,
        }
        card_value = values_dictionary[rank]
        return card_value
        
class Deck:
    def __init__(self, suits, scores):
        self.cards = []
   
        for suit in suits:
            for rank in scores.keys():
                card = Card(suit, rank)
                self.cards.append(card)
    
    def show_cards(self): 
        for card in self.cards:
            print(card)

    def draw_card(self):               
        drawn_card = random.choice(self.cards)
        self.cards.remove(drawn_card)
        return drawn_card

    def get_score(self):
        card_score = Card.get_score()
        return card_score
   
class Game:
    def __init__(self, suits, scores):
        self.player = Player()
        self.dealer = Dealer()
        self.gamedeck = Deck(suits, scores)
        self.player_score = 0
        self.dealer_score = 0

    def deal_cards(self):
        for i in range(2):
            self.dealer.hand.append(self.gamedeck.draw_card())
            self.player.hand.append(self.gamedeck.draw_card())
        self.dealer.show_hand()
        self.player.show_hand()

# This function is for when the dealer and player want another card (one).
# Needs an if, elif, else statement for if the player wants to stay or be hit.
    def hit(self, person):
        """Adds card to player's hand"""
        person.hand.append(self.gamedeck.draw_card())
        person.show_hand()

    def hit_or_stay(self):
        """Ask for input from person"""
        self.calculate_total_hand(self.dealer, self.player)
        print(f'Your score is currently {self.player_score}')

        while self.player_score < 21:
            choice = input('Would you like to hit? y/n ')
            if choice == 'n':
                print(f'Your score is now {self.player_score}')

                if self.player_score > self.dealer_score:
                    print(f'Your score of {self.player_score} is higher than the dealer\'s score of {self.dealer_score}. You win!!!')
                else:
                    print(f'Your score of {self.player_score} is lower than the dealer\'s score of {self.dealer_score}. Sorry, you lose.')
                break
            else: 
                self.hit(self.player)
                self.calculate_total_hand(self.dealer, self.player)
                print(f'Your score is now {self.player_score}')

        else:
            if self.player_score == 21:
                print(f'You won Blackjack!')
            else:
                print(f'Your score is now {self.player_score}. That\'s a bust.')
            
            # self.player.show_hand()

    def calculate_total_hand(self, dealer, player):
        player_hand_score = []
        dealer_hand_score = []
        for card in player.hand:
            player_hand_score.append(card.score)
        for card in dealer.hand:
            dealer_hand_score.append(card.score)
        self.player_score = sum(player_hand_score)
        self.dealer_score = sum(dealer_hand_score)

    def hit_dealer(self):
        while self.dealer_score < 17:
            self.hit(self.dealer)
            self.calculate_total_hand(self.dealer, self.player)
            if self.dealer_score > 21:
                print('Dealer busts! Player wins!!')
        else:
            self.dealer.show_hand()

    # def winner(self, dealer, player):
    #     if player.show_hand > 17 and player.show_hand <= 21 and player.show_hand > dealer.show_hand:
    #         print('Congrats. You won!!')
    #     else:
    #         print('Sorry, you lost.')

game = Game(SUITS, SCORES)
game.deal_cards()
    #gamedeck.show_cards()
# game.hit(game.player)
game.hit_or_stay()
game.hit_dealer()
game.calculate_total_hand(game.dealer, game.player)
    # game.hit_dealer()
    # game.winner()

# Still need to make funciton work for hit/stay
# Need function to tally score
# Need function to declare winner/loser


