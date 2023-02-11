import random
import pygame

# initialize pygame
pygame.init()

# set window size
window_size = (800, 600)

# create the window
window = pygame.display.set_mode(window_size)

# create font for displaying text
font = pygame.font.Font(None, 36)

# generate cards for the players
player1_cards = [random.randint(7, 11) for i in range(2)]
player2_cards = [random.randint(7, 11) for i in range(2)]

# game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # update window content
    window.fill((255, 255, 255)) # set background color
    
    # display cards for player 1
    player1_text = font.render("Player 1 cards: {}".format(player1_cards), True, (0, 0, 0))
    window.blit(player1_text, (50, 50))
    
    # display cards for player 2
    player2_text = font.render("Player 2 cards: {}".format(player2_cards), True, (0, 0, 0))
    window.blit(player2_text, (50, 100))
    
    # determine the winner
    player1_sum = sum(player1_cards)
    player2_sum = sum(player2_cards)
    if player1_sum > player2_sum:
        winner_text = font.render("Player 1 wins!", True, (0, 0, 0))
    elif player2_sum > player1_sum:
        winner_text = font.render("Player 2 wins!", True, (0, 0, 0))
    else:
        winner_text = font.render("It's a tie!", True, (0, 0, 0))
    window.blit(winner_text, (50, 150))
    
    pygame.display.update()

# quit pygame
pygame.quit()

