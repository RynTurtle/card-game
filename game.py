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
        # gotta be a cleaner way of doing this 
        self.dealer_x,self.dealer_y = (self.display_w / 2) - (self.card_width / 2), 100  
        self.mid_x,self.mid_y = (self.display_w / 2) - (self.card_width / 2) , self.display_h - (self.card_height + self.padding)
        self.right_x,self.right_y = (self.display_w / 2) - (self.card_width / 2) + self.padding + self.card_width, self.display_h - (self.card_height + self.padding)
        self.right2_x,self.right2_y = (self.display_w / 2) - (self.card_width / 2) + (self.padding *2) + (self.card_width*2), self.display_h - (self.card_height + self.padding)
        self.left_x,self.left_y = (self.display_w / 2) - (self.card_width / 2) - self.padding - self.card_width, self.display_h - (self.card_height + self.padding)
        self.left2_x, self.left2_y = (self.display_w / 2) - (self.card_width / 2) - (self.padding *2) - (self.card_width*2), self.display_h - (self.card_height + self.padding)

        self.card_back = pygame.image.load('./images/card-back.png')
        self.card_back = pygame.transform.scale(self.card_back, (self.card_width,self.card_height ))

        self.add_player("ryan")
        self.add_player("jeff")
        self.add_player("abc")
        self.add_player("def")
        self.add_player("ghi")

                
    def draw_card_placeholders(self):
        #x,y,width,height,line width
        # dealer rectangle
        pygame.draw.rect(self.screen, "red", pygame.Rect(self.dealer_x,self.dealer_y, self.card_width, self.card_height), width=5) 
        self.place_dealer_stack()
        # place a card in the middle of the screen, the height is the screens size - the card height with padding added
        pygame.draw.rect(self.screen, "red", pygame.Rect(self.mid_x,self.mid_y, self.card_width, self.card_height), width=5) 
        
        # right of the middle 
        pygame.draw.rect(self.screen, "red", pygame.Rect(self.right_x,self.right_y, self.card_width, self.card_height), width=5) 
        pygame.draw.rect(self.screen, "red", pygame.Rect(self.right2_x,self.right2_y, self.card_width,self.card_height), width=5) 

        # left of the middle 
        pygame.draw.rect(self.screen, "red", pygame.Rect(self.left_x,self.left_y, self.card_width, self.card_height), width=5) 
        pygame.draw.rect(self.screen, "red", pygame.Rect(self.left2_x,self.left2_y,self.card_width, self.card_height), width=5) 



    def place_dealer_stack(self):
        # give it stacked look
        for i in range(10): 
            self.screen.blit(self.card_back, (self.dealer_x - i,self.dealer_y - i)) # place cards with offset of 1 on each axis

    def deal_cards(self):
        # todo: animate?
        # cards are on dealer stack position, i want to move them to get to the target of each card going from left to right 
        #print(f"dealer: x: {dealer_x} y:{dealer_y}")
        #print(f"target: x: {left2_x} y: {left2_y}")
        pass
    

    def game_loop(self):
        running = True
        clock = pygame.time.Clock()
 
        while running:
            # poll for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT: # user wants to quit
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        #deal cards 
                        self.deal_cards()

            # dark green background 
            self.screen.fill((0, 100, 0))

            #draw white line in middle for reference 
            pygame.draw.line(self.screen, "white", (self.display_w /2, 0), (self.display_w / 2, self.display_h), width=2)


            self.draw_card_placeholders()

            # update game 
            pygame.display.flip()
            # fps
            clock.tick(60)  

        pygame.quit()



card_game().game_loop()