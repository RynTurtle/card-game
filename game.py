import pygame 
from logic import card_game_logic 


# if enough time: 
# click card to reveal instead of numbers
# show dealer cards being stacked in an animation with a satisfying sound 
# when shuffle and deal buttons are locked, use alternative image with grey instead of gold



class Button():
    # image,position,size
    # bug: when buttons overlap on different screens it will click them both, for now i will just avoid overlap 
    def __init__(self,screen,image_file,x,y,scale = None,width=0,height=0):
        self.screen = screen

        self.button_image = pygame.image.load(f"./images/{image_file}").convert_alpha() # convert alpha makes sure transparency is preserved 
        if scale != None:
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
        self.big_font = pygame.font.SysFont(None,200)  
        self.font = pygame.font.SysFont(None,60)  


    def main_menu(self):
        # enter to start game 
        x = self.display_w / 2
        y = self.display_h / 2 

        start_button = Button(self.screen,"start.png",x,y,1)
        guide = Button(self.screen,"guide.png",x,y + 150,1)

        while True:
            # handle events 
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    pygame.quit()

            if start_button.is_pressed():
                print("start pressed")
                self.player_screen()

            if guide.is_pressed():
                self.guide()

            self.screen.blit(self.main_menu_image,(0,0))
            start_button.draw()
            guide.draw()
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
                    self.players_chosen = i+2 
                    # start game 
                    card_game(self.players_chosen,self.screen,self.display_w,self.display_h).game_loop()
                    return  # go back to the main menu when card game is exited
        
            self.screen.fill((0, 100, 0))
            #pygame.draw.line(self.screen, "white", (self.display_w /2, 0), (self.display_w / 2, self.display_h), width=2)
            text_image = self.big_font.render("How many players?",True,(0,0,0))
            self.screen.blit(text_image,(self.display_w / 4.5,self.display_h / 5))
            # draw all the buttons 
            for b in btns:
                b.draw()


    def guide(self):
        x = self.display_w / 2 
        y = self.display_h 
        return_button = Button(self.screen,"ok.png",x,y - 150,1)
        welcome = "Welcome to High Five!"
        howtoplay = "Each player has five cards, After each player card is drawn a winner is determined, the player with the most wins after wins the game"
        controls = "Click shuffle to randomise the player cards, click deal to distribute the cards then click on the cards to reveal their values"
        while True:
            # handle events 
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    pygame.quit()
            
            if return_button.is_pressed():
                return 
            
            self.screen.fill((0, 100, 0))
            return_button.draw()


    def game_end(self,winner):
        # game has ended, player won/draw,  continue? Y/N 
        y = Button(self.screen,"y.png", self.display_w / 2  - 50,self.display_h / 2,0.2)
        n = Button(self.screen,"n.png", self.display_w / 2  + 50,self.display_h / 2,0.2)
        if winner == "draw":
            message = f"It was a draw!"
        else:
            message = f"Congratulations {winner}, you have won!!!"

        congrats = self.font.render(message,True,(0,0,0))
        restart = self.font.render("Would you like to restart?",True,(0,0,0))

        while True:
            # handle events 
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  
                    pygame.quit()

            if y.is_pressed():
                self.player_screen()
                print("y")

            if n.is_pressed():
                print("n")
                return 
            
            self.screen.fill((0, 100, 0))
            pygame.draw.line(self.screen, "white", (self.display_w /2, 0), (self.display_w / 2, self.display_h), width=2)
        
            y.draw()
            self.screen.blit(restart,(0,self.display_h / 3))
            self.screen.blit(congrats,(0,self.display_h / 3 - 50))
            n.draw() 
    


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
        
        self.positions = []
        # 5 cards, padding inbetween these cards 
        total_width = self.card_width * 5 + self.padding * 4
        #  get the amount of space left after placing cards, divide it equally in half so you can get the starts spacing 
        start_x = (self.display_w - total_width) / 2
        # height is the card height + padding 

        y = self.display_h - (self.card_height + self.padding)
        for i in range(5):
            # calculate next card by starting far left, then add the card # and * by the cards and their padding 
            x = start_x + i * (self.card_width + self.padding)
            self.positions.append(pygame.Vector2(x,y))
        #pygame draws these objects from the top left corner 
        self.left2 = self.positions[0]
        self.left = self.positions[1]
        self.mid = self.positions[2]
        self.right = self.positions[3]
        self.right2 = self.positions[4]
 
        self.card_back = pygame.image.load('./images/card-back.png')
        self.card_back = pygame.transform.scale(self.card_back, (self.card_width,self.card_height ))

        self.deal_cards = False
        self.updated_score = False 
        self.flipped = [False,False,False,False,False]
        self.continue_game = True   # player has no cards in their hand or they chose to exit 
        self.shuffle_button = Button(self.screen,"shuffle.png",self.display_w / 2, self.card_height + 125,0.5)
        self.deal_button = Button(self.screen, "deal.png",self.display_w / 2,self.card_height  + 180 ,0.5) 
        
        # need to pass the buttons a center instead of top left, to do this add the half of the card its missing 
        center_h = self.card_height / 2
        center_w = self.card_width / 2  
        self.left2_button = Button(self.screen,"card-back.png",self.left2[0] + center_w,self.left2[1] + center_h, width=self.card_width,height=self.card_height)
        self.left_button = Button(self.screen,"card-back.png",self.left[0] + center_w,self.left[1] + center_h, width=self.card_width,height=self.card_height)
        self.mid_button = Button(self.screen,"card-back.png",self.mid[0] + center_w,self.mid[1] + center_h, width=self.card_width,height=self.card_height)
        self.right_button = Button(self.screen,"card-back.png",self.right[0] + center_w,self.right[1] + center_h, width=self.card_width,height=self.card_height)
        self.right2_button = Button(self.screen,"card-back.png",self.right2[0] + center_w,self.right2[1] + center_h, width=self.card_width,height=self.card_height)
        self.card_buttons =  [self.left2_button,self.left_button,self.mid_button,self.right_button,self.right2_button]
        #print(f"new x:{t} y{t2}")


        for i in range(players_chosen):
            self.add_player(f"player {i+1}")
        self.guide = Button(self.screen,"guide.png",100,40,0.7)

    def card_outlines(self):
        #x,y,width,height,line width
        # dealer rectangle
        pygame.draw.rect(self.screen, "gold", pygame.Rect(self.dealer[0],self.dealer[1], self.card_width, self.card_height), width=5) 
        # place a card in the middle of the screen, the height is the screens size - the card height with padding added
        pygame.draw.rect(self.screen, "gold", pygame.Rect(self.mid[0],self.mid[1], self.card_width, self.card_height), width=5) 
        
        # right of the middle 
        pygame.draw.rect(self.screen, "gold", pygame.Rect(self.right[0],self.right[1], self.card_width, self.card_height), width=5) 
        pygame.draw.rect(self.screen, "gold", pygame.Rect(self.right2[0],self.right2[1], self.card_width,self.card_height), width=5) 

        # left of the middle 
        pygame.draw.rect(self.screen, "gold", pygame.Rect(self.left[0],self.left[1], self.card_width, self.card_height), width=5) 
        pygame.draw.rect(self.screen, "gold", pygame.Rect(self.left2[0],self.left2[1],self.card_width, self.card_height), width=5) 



    def place_dealer_stack(self):
        # give it stacked look
        for i in range(10): 
            self.screen.blit(self.card_back, (self.dealer[0] - i,self.dealer[1] - i)) # place cards with offset of 1 on each axis

    def place_cards(self):
        for i in range(5): # 5 cards per player             
            for j,player in enumerate(self.get_players()):
                # place the card from left to right through the positions in self.positions, stack them by offset card through i  
                self.screen.blit(self.card_back, (self.positions[j][0] - i, self.positions[j][1] - i))        
    
    def write_text(self,text,x,y):
        text_image = self.font.render(text,True,(0,0,0))
        self.screen.blit(text_image,(x,y))

    
    def place_card_buttons(self):
        for i,player in enumerate(self.get_players()):
            # draw the button card related to the player 
            self.card_buttons[i].draw()
            
    def handle_buttons(self):
        for i,buttons in enumerate(self.card_buttons):
            if buttons.is_pressed() and self.deal_cards:
                # only flip cards if they are dealt
                self.flipped[i] = True  


        # deal cards when the button is pressed and when the cards have been shuffled 
        if self.deal_button.is_pressed() and len(self.deck) != 0:
            print("deal")
            # now the dealer will move the cards facedown for the player to flip  
            self.deal_cards = True  

        # shuffling can only be done when the game starts 
        if self.shuffle_button.is_pressed() and self.deal_cards == False and self.round == 1:
            print("shuffle")
            self.shuffle_deck()
            self.deal_hands() # deal the shuffled hands  

        if self.guide.is_pressed():
            game_menu().guide()


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
        #self.test.draw()
        self.guide.draw()
        self.shuffle_button.draw()
        self.deal_button.draw()
        if self.deal_cards:
            # place the buttons underneath the cards 
            self.place_card_buttons() 
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
                    if event.key == pygame.K_SPACE:
                        # finish round 
                        self.handle_round()
                        # set the cards to default 
                        self.flipped = [False,False,False,False,False]
                        self.updated_score = False 
                        self.deal_cards = False

            self.handle_buttons()
            self.draw()

            # if the player cards have been flipped, alert the user to press space to continue and update the score only once 
            if self.flipped.count(True) >= len(self.get_players()): 
                # update the winning player
                if self.updated_score == False:
                    player = self.round_winner()
                    if player != "draw":
                        self.update_score(player) 
                        self.updated_score = True 
                
                text_image = self.font.render("Press space to continue",True,(0,0,0))
                self.screen.blit(text_image,(self.display_w / 2 - 100,self.display_h / 2))
                    
            # player has empty hand 
            if self.has_empty_hand() and self.round != 1 : 
                self.continue_game = False  # end game loop 
                # get the final winner of all 5 rounds, pass it into the game end screen 
                game_menu().game_end(self.game_winner())

            # update game 
            pygame.display.flip()
            # fps
            clock.tick(60)  

        #pygame.quit()


menu =  game_menu()
menu.main_menu()