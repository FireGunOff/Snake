# -*- coding: cp1252 -*-
# /usr/bin/env python
# Simon H. Larsen
# Buttons.py - example
# Project startet: d. 28. august 2012
# Import pygame modules and Buttons.py(it must be in same dir)
import pygame, Buttons
import sys
from pygame.locals import *
import os


# Initialize pygame
pygame.init()


clock = pygame.time.Clock()


# Create a display



# Update the display and show the button


Button1 = Buttons.Button()
Button2 = Buttons.Button()
Button3 = Buttons.Button()
Button4 = Buttons.Button()
screen = pygame.display.set_mode((650, 410), 0, 32)
pygame.display.set_caption("Difficulty")
background_image = pygame.image.load("backgroundDif.jpg").convert()
# Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
pygame.display.flip()
while True:
    screen.blit(background_image, [0, 0])
    Button1.create_button(screen, (0, 142, 35), 240, 50, 150, 75, 0, "Easy", (255, 255, 255))
    Button2.create_button(screen, (210, 200, 0), 240, 160, 150, 75, 0, "Medium", (255, 255, 255))
    Button3.create_button(screen, (178, 34, 34), 240, 270, 150, 75, 0, "Hard", (255, 255, 255))
    Button4.create_button(screen, (178, 34, 34), 475, 320, 150, 75, 0, "Back", (255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            if Button1.pressed(pygame.mouse.get_pos()):
                import Zmeyka_Easy
            if Button2.pressed(pygame.mouse.get_pos()):
                import Zmeyka
            if Button3.pressed(pygame.mouse.get_pos()):
                import Zmeyka_Hard
            if Button4.pressed(pygame.mouse.get_pos()):
                import Snake

        pygame.display.flip()
    clock.tick(60)


if __name__ == '__main__':
    obj = Button_Example()
    obj.display()
    obj.update_display()
    obj.main()

dif = Button_Example()
dif.display()
dif.update_display()
dif.main()
