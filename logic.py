
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
            return "maximum player limit reached"
        if player_name in self.player_hands:
            return "player already added"

        self.player_hands[player_name] = {"cards":[]}
        return f"added {player_name}"


    # shuffle a new deck of cards
    def shuffle_deck(self):
        cards = os.listdir("./images/cards")
        random.shuffle(cards)   
        for card in cards:
            self.deck.append(card.replace(".png",""))
        
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
        # need to give a card 5 times to each player 
        for _ in range(5): 
            for players in self.player_hands:
                chosen_card = self.deck[0]
                self.player_hands[players]["cards"].append(chosen_card)
                self.deck.pop(0) # remove the card used 
            
    def check_winner(self):
        highest_card = 0  
        winner = ""
        for player in self.player_hands:
            player_card = self.player_hands[player]["cards"][0]
            card_value = self.get_card_value(player_card)
            print(f"{player}: {player_card}")
            if card_value > highest_card:
                highest_card = card_value
                winner = player
        
        # check if the  "highest card" is also in the list with another player, then its a draw
        for player in self.player_hands:
            if self.get_card_value(self.player_hands[player]["cards"][0]) == highest_card and player != winner:
                return "draw"
        return winner

game = card_game_logic()

game.add_player("ryan")
game.add_player("jeff")
game.add_player("abc")

game.shuffle_deck()
game.deal_hands()
print(game.check_winner())

# check values of player cards, compare them, find winner 
# add the 