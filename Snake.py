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

music = 'music.mp3'
pygame.mixer.init()
pygame.mixer.music.load(music)
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()


# Create a display



# Update the display and show the button


Button1 = Buttons.Button()
Button2 = Buttons.Button()
Button3 = Buttons.Button()
screen = pygame.display.set_mode((600, 550), 0, 32)
pygame.display.set_caption("Snake")
background_image = pygame.image.load("backgroundSnake.jpg").convert()
# Parameters:               surface,      color,       x,   y,   length, height, width,    text,      text_color
pygame.display.flip()
while True:
    screen.blit(background_image, [0, 0])
    Button1.create_button(screen, (107, 142, 35), 225, 100, 150, 75, 0, "Start", (255, 255, 255))
    Button2.create_button(screen, (107, 142, 35), 225, 235, 150, 75, 0, "About", (255, 255, 255))
    Button3.create_button(screen, (107, 142, 35), 225, 370, 150, 75, 0, "Exit", (255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        elif event.type == MOUSEBUTTONDOWN:
            if Button1.pressed(pygame.mouse.get_pos()):
                import Difficulty
            if Button2.pressed(pygame.mouse.get_pos()):
                import About
            if Button3.pressed(pygame.mouse.get_pos()):
                sys.exit()

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
