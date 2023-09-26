import pygame
from pygame.locals import *

pygame.init()

#screen dimensions 
screen_width = 800
screen_height = 500

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Monty Hall Game")

#loading images
bg_img = pygame.image.load('/Users/graciousasare/Desktop/Projects SWE/Monty Hall Game/Images/background.png')


#GAME LOOP set var to run game continuously
run = True
while run:

    screen.blit(bg_img, (0,0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT: #when window is closed
            run = False #to close game

    pygame.display.update()
    
pygame.quit()