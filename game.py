import pygame 

pygame.init()
display_info = pygame.display.Info()
display_w = display_info.current_w
display_h = display_info.current_h

screen = pygame.display.set_mode((display_w,display_h),pygame.RESIZABLE)
#screen = pygame.display.set_mode((1920,1080),pygame.RESIZABLE)

clock = pygame.time.Clock()

card_height = 250
card_width = 200 
padding = 50

def draw_card_placeholders():
    #x,y,width,height,line width
    # dealer rectangle 
    pygame.draw.rect(screen, "red", pygame.Rect((display_w / 2) - (card_width / 2) , 100, card_width, card_height), width=5) 

    # place a card in the middle of the screen, the height is the screens size - the card height with padding added
    pygame.draw.rect(screen, "red", pygame.Rect((display_w / 2) - (card_width / 2) , display_h - (card_height + padding), card_width, card_height), width=5) 
    
    # right of the middle 
    pygame.draw.rect(screen, "red", pygame.Rect((display_w / 2) - (card_width / 2) + padding + card_width, display_h - (card_height + padding), card_width, card_height), width=5) 
    pygame.draw.rect(screen, "red", pygame.Rect((display_w / 2) - (card_width / 2) + (padding *2) + (card_width*2), display_h - (card_height + padding), card_width, card_height), width=5) 

    # left of the middle 
    pygame.draw.rect(screen, "red", pygame.Rect((display_w / 2) - (card_width / 2) - padding - card_width, display_h - (card_height + padding), card_width, card_height), width=5) 
    pygame.draw.rect(screen, "red", pygame.Rect((display_w / 2) - (card_width / 2) - (padding *2) - (card_width*2), display_h - (card_height + padding), card_width, card_height), width=5) 

# todo make it responsive using 0.10 for 10% instead 

running = True
while running:
    # poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # user wants to quit
            running = False


    # dark green background 
    screen.fill((0, 100, 0))

    #draw white line in middle for reference 
    pygame.draw.line(screen, "white", (display_w /2, 0), (display_w / 2, display_info.current_h), width=2)


    draw_card_placeholders()

    # update game 
    pygame.display.flip()
    # fps
    clock.tick(60)  

pygame.quit()