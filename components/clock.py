import sys
sys.path.append('../')

import pygame
import ui
import colors
import fonts

def draw(screen, x, y, width, height):

    # Draw text
    textobj = fonts.font_sm.render("Monday, January 12", 1, colors.white)
    textrect = textobj.get_rect()
    textrect.topleft = (x + 10, y + 10)
    screen.blit(textobj, textrect)