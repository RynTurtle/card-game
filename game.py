import pygame 
from logic import card_game_logic 


#class game_menu():


#class game_popups():


# need to do:
# enter player names


# when one player has no cards
# do you want to restart? Y/N buttons 



# if enough time: 
# click card to reveal instead of numbers
# show dealer cards being stacked in an animation with a satisfying sound 
# controls button top left 



class Button():
    # image,position,size
    # bug: when buttons overlap on different screens it will click them both 
    def __init__(self,screen,image_file,x,y,scale = 1.0):
        self.screen = screen
        self.button_image = pygame.image.load(f"./images/{image_file}").convert_alpha() # convert alpha makes sure transparency is preserved 
        width = self.button_image.get_width()
        height = self.button_image.get_height()

        width = int(width * scale)
        height = int(height * scale)
        self.button_image = pygame.transform.smoothscale(self.button_image,(width,height)) # create the new button with the scaled width/height 
        self.rect = self.button_image.get_rect(center=(x,y)) # enclose image in rectangle, center it in the x,y coords
       
        self.clicked = False # allow only one click being registered 

    def draw(self):
        # if its clicked then draw the clicked alternative button png?
        # if its hovered over then draw a highlight or something over the button 
        self.screen.blit(self.button_image,self.rect)

    def is_pressed(self):
        position = pygame.mouse.get_pos()
        pressed = pygame.mouse.get_pressed()[0] # bool 
        if self.rect.collidepoint(position): # if the mouse is in the area of the rectangle button 
            if pressed and not self.clicked:
                self.clicked = True 
                return True
            
        if not pressed:
            self.clicked = False 
            return False 
        return False 


# main menu => players => game => game end => replay? Y => game; N => main menu 
class game_menu():
    # to use multiple screens, add multiple game loops where they clear the screen 
    
    def __init__(self):
        pygame.init()
        self.display_w = 1920
        self.display_h = 1080
        #fullscreen
        display_info = pygame.display.Info()
        #self.display_w = display_info.current_w
        #self.display_h = display_info.current_h
        self.screen = pygame.display.set_mode((self.display_w,self.display_h))
        self.main_menu_image = pygame.image.load(f"./images/main-menu.png")
        self.main_menu_image = pygame.transform.smoothscale(self.main_menu_image,(self.display_w,self.display_h)) # resize image to fit display
        self.font = pygame.font.SysFont(None,200)  



    def main_menu(self):
        # enter to start game 
        sx = self.display_w / 2
        sy = self.display_h / 2 
        cx = self.display_h / 2 - 50
        cy = self.display_w / 2 - 50
        start_button = Button(self.screen,"start-button.png",sx,sy,1)
        while True:
            # handle events 
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    pygame.quit()

            if start_button.is_pressed():
                print("start pressed")
                self.player_screen()
            
            self.screen.blit(self.main_menu_image,(0,0))
            start_button.draw()

            #if controls.is_pressed():
            #    print("controls has been clicked")


    def player_screen(self):
        # gets the players and inserts them into the player_hands variable 
        print("player screen")
        # start the card game, give it the screen to write over  
        x = self.display_w / 2 - 350
        y = self.display_h / 2 + 100
        two = Button(self.screen,"2.png",x + 200,y ,0.2)
        three = Button(self.screen,"3.png",x + 300,y,0.2)
        four = Button(self.screen,"4.png",x + 400,y,0.2)
        five = Button(self.screen,"5.png",x + 500 ,y,0.2)
        
        btns = [two,three,four,five] 
        while True:            
            # handle events 
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    pygame.quit()
            
            for i in range(4):
                if btns[i].is_pressed():
                    #print(f"{i+2} players")
                    players_chosen = i+2 
                    # start game 
                    card_game(players_chosen,self.screen,self.display_w,self.display_h).game_loop()
                    return  # go back to the main menu when card game is exited
                
            self.screen.fill((0, 100, 0))
            #pygame.draw.line(self.screen, "white", (self.display_w /2, 0), (self.display_w / 2, self.display_h), width=2)
            text_image = self.font.render("How many players?",True,(0,0,0))
            self.screen.blit(text_image,(self.display_w / 4.5,self.display_h / 5))
            # draw all the buttons 
            for b in btns:
                b.draw()

        
    def game_end(self):
        # game has ended, player won/draw,  continue? Y/N 
        while True:
            # handle events 
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    pygame.quit()

            self.screen.fill((0, 0, 0))

class card_game(card_game_logic):
    def __init__(self,players_chosen, screen,display_w,display_h):
        super().__init__() # initializes the subclasses  
        self.screen = screen
        self.display_w = display_w
        self.display_h = display_h
        self.font = pygame.font.SysFont(None,24) # default font 
        self.card_height = 250
        self.card_width = 200 
        self.padding = 50        
        self.dealer = pygame.Vector2((self.display_w / 2) - (self.card_width / 2), 100) 
        self.mid = pygame.Vector2((self.display_w / 2) - (self.card_width / 2) , self.display_h - (self.card_height + self.padding))
        self.right = pygame.Vector2((self.display_w / 2) - (self.card_width / 2) + self.padding + self.card_width, self.display_h - (self.card_height + self.padding))
        self.right2 = pygame.Vector2((self.display_w / 2) - (self.card_width / 2) + (self.padding *2) + (self.card_width*2), self.display_h - (self.card_height + self.padding))
        self.left = pygame.Vector2((self.display_w / 2) - (self.card_width / 2) - self.padding - self.card_width, self.display_h - (self.card_height + self.padding))
        self.left2 = pygame.Vector2((self.display_w / 2) - (self.card_width / 2) - (self.padding *2) - (self.card_width*2), self.display_h - (self.card_height + self.padding))
        # poistions left to right, players left to right 
        self.positions = [self.left2,self.left,self.mid,self.right,self.right2]
        
        self.card_back = pygame.image.load('./images/card-back.png')
        self.card_back = pygame.transform.scale(self.card_back, (self.card_width,self.card_height ))

        self.deal_cards = False
        self.updated_score = False 
        self.flipped = [False,False,False,False,False]
        self.continue_game = True   # player has no cards in their hand or they chose to exit 
        for i in range(players_chosen):
            self.add_player(f"player {i+1}")
        self.shuffle_deck()
        self.deal_hands()

    def card_outlines(self):
        #x,y,width,height,line width
        # dealer rectangle
        pygame.draw.rect(self.screen, "red", pygame.Rect(self.dealer[0],self.dealer[1], self.card_width, self.card_height), width=5) 
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
    
    def write_text(self,text,x,y):
        text_image = self.font.render(text,True,(0,0,0))
        self.screen.blit(text_image,(x,y))

    
 
    
    def flip_card(self):
        for i,value in enumerate(self.flipped): 
            if i < len(self.get_players()): # if the card has a player allocated
                players_card = self.player_hands[self.get_players()[i]]["cards"][0]
                if value: # the card is wanted to be flipped  
                    #print(f"{self.get_players()[i]},{players_card}")
                    card = pygame.image.load(f'./images/cards/{players_card}.png')
                    card = pygame.transform.scale(card, (self.card_width,self.card_height ))
                    self.screen.blit(card,(self.positions[i][0],self.positions[i][1]))
    

    def write_players(self):
        for i,value in enumerate(self.flipped): 
            if i < len(self.get_players()): # if the card has a player allocated
                player = self.get_players()[i]
                x = self.positions[i][0] 
                y = self.positions[i][1] - 20  #  add padding to ontop of the card
                self.write_text(f"player: {player} wins: {self.player_hands[player]["wins"]}",x,y)


    def draw(self):
        self.screen.fill((0, 100, 0))
        #draw white line in middle for reference 
        pygame.draw.line(self.screen, "white", (self.display_w /2, 0), (self.display_w / 2, self.display_h), width=2)
        self.card_outlines()
        self.place_dealer_stack()

        
        if self.deal_cards:
            self.place_cards()
            self.write_players()
            self.flip_card()

                

    def game_loop(self):
        clock = pygame.time.Clock()
        while self.continue_game:

            # poll for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # user clicked x on game 
                    pygame.quit() # exit the program 


                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_d:
                        #deal cards 
                        self.deal_cards = True 

                    if self.deal_cards: # only flip cards if they are dealt
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

                    if event.key == pygame.K_f:
                        print("finish")
                        # finish round 
                        self.handle_round()
                        # set the cards to default 
                        self.flipped = [False,False,False,False,False]
                        self.updated_score = False 
                        self.deal_cards = False

            self.draw()
            if self.flipped.count(True) >= len(self.get_players()): # if the player cards have been flipped
                # update the winning player
                if self.updated_score == False:
                    player = self.check_winner()
                    if player != "draw":
                        self.update_score(player) 
                        self.updated_score = True 
            
            if self.has_empty_hand(): # player has empty hand 
                self.continue_game = False  # end game loop 
                game_menu().game_end()

            # update game 
            pygame.display.flip()
            # fps
            clock.tick(60)  

        #pygame.quit()


menu =  game_menu()
menu.main_menu()