
"""

the card game needs to get the players needed and deal the players cards, 5 per person 
after the cards have been dealt start the game 

{   
    "player1":{
        "cards":[]
    }
    player2:{}

    wins:{player1:3,player2,2}
}

"""
import os
import random 
class card_game_logic():
    def __init__(self):
        self.player_hands = {}
        self.deck = [] 
        
    def add_player(self,player_name):
        if len(self.player_hands.keys()) == 5:
            print("maximum player limit")
            return "maximum player limit reached"
        if player_name in self.player_hands:
            print("player already added")
            return "player already added"

        self.player_hands[player_name] = {"cards":[],"wins":0}
        return f"added {player_name}"

    # shuffle a new deck of cards
    def shuffle_deck(self):
        if self.deck == []:
            cards = os.listdir("./images/cards")
            random.shuffle(cards)   
            for card in cards:
                self.deck.append(card.replace(".png",""))
            print("deck shuffled")
        else:
            print("deck has already been shuffled ")


    def get_card_value(self,card):
        # card name must be formatted like the card image list 
        face_cards = ["jack","king","queen"]
        value = card.split("_")[0]
        if value == "ace":
            return 11
        elif value in face_cards:
            return 10
        else:
            return int(value) 
    

    def deal_hands(self):
        # distribute 5 cards to each player, one player at a time 
        
        for _ in range(5): 
            for players in self.player_hands:
                chosen_card = self.deck[0]
                self.player_hands[players]["cards"].append(chosen_card)
                self.deck.pop(0) # remove the card used 
            
    def check_winner(self):
        highest_card = 0  
        winner = ""
        for player in self.player_hands:
            if len(self.player_hands[player]["cards"]) == 0:
                return "player has ran out of cards"
            
            player_card = self.player_hands[player]["cards"][0]
            card_value = self.get_card_value(player_card)
            #print(f"{player}: {player_card}")
            if card_value > highest_card:
                highest_card = card_value
                winner = player
                
        # check if the  "highest card" is also in the list with another player, then its a draw
        for player in self.player_hands:
            if self.get_card_value(self.player_hands[player]["cards"][0]) == highest_card and player != winner:
                return "draw"
            
        self.player_hands[winner]["wins"] += 1 
        return winner
    
    # remove the first card from the deck
    def handle_move(self):
        for player in self.player_hands:
            if self.player_hands[player]["cards"]:
                self.player_hands[player]["cards"].pop(0)

    def get_players(self):
        return list(self.player_hands.keys())

"""game = card_game_logic()

game.add_player("ryan")
game.add_player("jeff")
game.add_player("abc")
game.add_player("def")
game.add_player("ghi")
game.add_player("ghi")

game.shuffle_deck()
game.deal_hands()
for i in range(6):
    print(game.check_winner())
    game.handle_move()"""

# check values of player cards, compare them, find winner 
# add the 