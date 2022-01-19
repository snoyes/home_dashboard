import sys
sys.path.append('../')

import pygame
import ui
import colors
import fonts

y = 0
x = 0
width = ui.SCREEN_WIDTH
height = 50

def draw(screen):
    # Draw rectangle
    shape = pygame.Rect(x, y, width, height),
    pygame.Surface.fill(screen, colors.blue_500, shape)

    # Draw text
    textobj = fonts.font_sm.render("Alerts component", 1, colors.white)
    textrect = textobj.get_rect()
    textrect.topleft = (x + 10, y + 10)
    screen.blit(textobj, textrect)