
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
        self.round = 1 
    
    # add a player and their deck + wins 
    def add_player(self,player_name):
        if len(self.player_hands.keys()) == 5:
            print("maximum player limit")
            return "maximum player limit reached"
        if player_name in self.player_hands:
            print("player already added")
            return "player already added"

        self.player_hands[player_name] = {"cards":[],"wins":0} # maybe wins:{1:5,2:2,3:4} # round:wins 
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

        #https://en.wikipedia.org/wiki/List_of_poker_hands
        face_cards = {"ace":14,"king":13,"queen":12,"jack":11}

        value = card.split("_")[0]
        if value in face_cards:
            return face_cards[value] 
        else:
            return int(value) 
    

    # distribute 5 shuffled cards to each player 
    def deal_hands(self):
        for _ in range(5): 
            for players in self.player_hands:
                if len(self.player_hands[players]["cards"]) < 5: 
                    chosen_card = self.deck[0]
                    self.player_hands[players]["cards"].append(chosen_card)
                    self.deck.pop(0) # remove the card used from the main deck  
    


    def has_empty_hand(self):
        for players in self.get_players():
            if  self.player_hands[players]["cards"] == []:
                return True  


    def update_score(self,player):
        self.player_hands[player]["wins"] += 1 

    # determines the round winner by comparing the players current hand 
    def round_winner(self):
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
        return winner
    
    # calculate the winner of the entire game on their total wins 
    def game_winner(self):
        winner = ""
        amount = 0
        for players in self.player_hands:    
            #print(f"{players} {self.player_hands[players]["wins"]}")
            if  self.player_hands[players]["wins"] > amount:
                amount = self.player_hands[players]["wins"]
                winner = players    
        for players in self.player_hands:
            if self.player_hands[players]["wins"] == amount and players != winner:
                return "draw"
        return winner

    # remove the first card from the deck 
    def handle_round(self):
        for player in self.player_hands:
            if self.player_hands[player]["cards"]:
                self.player_hands[player]["cards"].pop(0)
        self.round +=1 

    def get_players(self):
        return list(self.player_hands.keys())

 
 