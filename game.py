import pygame 
from logic import card_game_logic 

 
class card_game(card_game_logic):
    def __init__(self):
        super().__init__() # initializes the logic class 

        pygame.init()
        display_info = pygame.display.Info()
        #display_w = display_info.current_w
        #display_h = display_info.current_h
        self.display_w = 1920
        self.display_h = 1080

        #fullscreen
        self.screen = pygame.display.set_mode((self.display_w,self.display_h))
        self.card_height = 250
        self.card_width = 200 
        self.padding = 50
        
        self.dealer = pygame.Vector2((self.display_w / 2) - (self.card_width / 2), 100) 
        self.mid = pygame.Vector2((self.display_w / 2) - (self.card_width / 2) , self.display_h - (self.card_height + self.padding))
        self.right = pygame.Vector2((self.display_w / 2) - (self.card_width / 2) + self.padding + self.card_width, self.display_h - (self.card_height + self.padding))
        self.right2 = pygame.Vector2((self.display_w / 2) - (self.card_width / 2) + (self.padding *2) + (self.card_width*2), self.display_h - (self.card_height + self.padding))
        self.left = pygame.Vector2((self.display_w / 2) - (self.card_width / 2) - self.padding - self.card_width, self.display_h - (self.card_height + self.padding))
        self.left2 = pygame.Vector2((self.display_w / 2) - (self.card_width / 2) - (self.padding *2) - (self.card_width*2), self.display_h - (self.card_height + self.padding))

        self.positions = [self.left2,self.left,self.mid,self.right,self.right2]
        # poistions left to right, players left to right 
        self.card_back = pygame.image.load('./images/card-back.png')
        self.card_back = pygame.transform.scale(self.card_back, (self.card_width,self.card_height ))
        self.place_card = False
        self.flipped = [False,False,False,False,False]

        # maybe add a newgame function which does this part, getting the names of players 
        self.add_player("ryan")
        self.add_player("jeff")
        self.add_player("abc")
        self.shuffle_deck()
        self.deal_hands()
    
        


    def card_placeholders(self):
        #x,y,width,height,line width
        # dealer rectangle
        pygame.draw.rect(self.screen, "red", pygame.Rect(self.dealer[0],self.dealer[1], self.card_width, self.card_height), width=5) 
        self.place_dealer_stack()
        # place a card in the middle of the screen, the height is the screens size - the card height with padding added
        pygame.draw.rect(self.screen, "red", pygame.Rect(self.mid[0],self.mid[1], self.card_width, self.card_height), width=5) 
        
        # right of the middle 
        pygame.draw.rect(self.screen, "red", pygame.Rect(self.right[0],self.right[1], self.card_width, self.card_height), width=5) 
        pygame.draw.rect(self.screen, "red", pygame.Rect(self.right2[0],self.right2[1], self.card_width,self.card_height), width=5) 

        # left of the middle 
        pygame.draw.rect(self.screen, "red", pygame.Rect(self.left[0],self.left[1], self.card_width, self.card_height), width=5) 
        pygame.draw.rect(self.screen, "red", pygame.Rect(self.left2[0],self.left2[1],self.card_width, self.card_height), width=5) 



    def place_dealer_stack(self):
        # give it stacked look
        for i in range(10): 
            self.screen.blit(self.card_back, (self.dealer[0] - i,self.dealer[1] - i)) # place cards with offset of 1 on each axis

    def place_cards(self):
        # add player name and winning info, would be cool if animated 
        for i in range(5): # 5 cards per player 
            for j,player in enumerate(self.get_players()):
                # place the card from left to right through the positions in self.positions, stack them by offset card through i  
                
                
                self.screen.blit(self.card_back, (self.positions[j][0] - i, self.positions[j][1] - i))        
    
    def flip_card(self):

        for i,value in enumerate(self.flipped): 
            if i < len(self.get_players()): # if the card has a player allocated
                players_card = self.player_hands[self.get_players()[i]]["cards"][0]
                if value: # a number was pressed 
                    print(f"{self.get_players()[i]},{players_card}")
                    card = pygame.image.load(f'./images/cards/{players_card}.png')
                    card = pygame.transform.scale(card, (self.card_width,self.card_height ))

                    self.screen.blit(card,(self.positions[i][0],self.positions[i][1]))


    def draw(self):
        self.screen.fill((0, 100, 0))
        #draw white line in middle for reference 
        pygame.draw.line(self.screen, "white", (self.display_w /2, 0), (self.display_w / 2, self.display_h), width=2)
        self.card_placeholders()
        if self.place_card:
            self.place_cards()
            self.flip_card()


    def game_loop(self):
        running = True
        clock = pygame.time.Clock()
 
        while running:
            # poll for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # user wants to quit
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        #deal cards 
                        self.place_card = True 

                    if event.key == pygame.K_1:
                        self.flipped[0] = True 
                    if event.key == pygame.K_2:
                        self.flipped[1] = True 
                    if event.key == pygame.K_3:
                        self.flipped[2] = True 
                    if event.key == pygame.K_4:
                        self.flipped[3] = True 
                    if event.key == pygame.K_5:
                        self.flipped[4] = True 

                         
            self.draw()
            # update game 
            pygame.display.flip()
            # fps
            clock.tick(60)  

        pygame.quit()



card_game().game_loop()