
from logic import card_game_logic 

game = card_game_logic()

game.add_player("ryan")
game.add_player("jeff")
game.add_player("abc")
game.add_player("def")
game.add_player("ghi")
game.add_player("ghi")

print(game.get_players())
#game.shuffle_deck()
#game.deal_hands()
#for i in range(6):
#    print(game.check_winner())
#    game.handle_move()


game_loop()