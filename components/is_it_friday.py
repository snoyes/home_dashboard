import requests
from os.path import exists

import sys
sys.path.append('../')
import pygame
import colors
import fonts

padding = 10

font = fonts.font_6xl

def draw(screen, rect):
    content_height = font.get_height()
    center = (rect.x + rect.width//2, rect.y + rect.height//2)
    content_y = center[1] - content_height//2

    text = font.render(get_text(), 1, colors.white)
    text_rect = text.get_rect()
    text_rect.midtop = (center[0], content_y)
    screen.blit(text, text_rect)

def update():
    url = 'https://www.is-it-friday.org/'
    friday = False
    if (r := requests.get(url)):
        friday = "YES!!! IT'S FRIDAY" in r.text

    with open('.is_it_friday_data', 'w') as f:
        print(friday, file=f)

def get_text():
    try:
        with open('.is_it_friday_data') as f:
            cached_data = f.readline().strip()
            friday = cached_data == 'True'

        return f'Today is {"not "*(not friday)}Friday.'

    except FileNotFoundError:
        return 'Unknown if today is Friday.'
