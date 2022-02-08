import sys, json
from datetime import datetime
from os.path import exists

sys.path.append('../')
import pygame, colors, fonts
from decouple import config

padding = 10
font = fonts.font_4xl
row_height = font.get_height()

ICON_SCALE = config('ICON_SCALE', default=1, cast=int)

def draw(screen, rect):

    global surface
    surface = screen

    if(exists('.weather_data') == False):
        # TODO: Add loading text/animation
        return

    with open('.weather_data') as json_file:
        weather_data = json.load(json_file)

    column_plus_padding = (rect.width - (padding*2))/5
    column_padding = column_plus_padding/10
    column_width = column_padding*8
    column_height = (column_padding*2) + (row_height + row_height//2) * 5
    table_width = column_plus_padding*5

    padding_x = (rect.width - table_width)//2
    padding_y = (rect.height - column_height)//2

    x_pos = rect.x + padding_x + column_padding + column_width//2

    # Border around first column
    border_rect = (rect.x + padding_x + column_padding//2, rect.y + padding_y, column_padding + column_width, column_height)
    pygame.draw.rect(screen, colors.white, border_rect, 2, 5)

    for i in range(5):
        weather_data_day = weather_data['daily'][i]
        draw_column((x_pos, rect.y + padding_y), {
            "letter": datetime.fromtimestamp(weather_data_day['dt']).strftime("%a")[0],
            "high": str(round(weather_data_day['temp']['max'])),
            "low": str(round(weather_data_day['temp']['min'])),
            "icon": 'weather/' + weather_data_day['weather'][0]['icon'] + ("@2x" if ICON_SCALE > 1 else "") + ".png",
        })
        
        x_pos += column_padding*2 + column_width


def draw_column(position, data):
    y = position[1]
    y += row_height + row_height//2
    draw_day_letter((position[0], y), data['letter'])
    y += row_height + row_height//2
    draw_temp((position[0], y), data['high'])
    y += row_height + row_height//2
    draw_temp((position[0], y), data['low'])
    y += row_height + row_height//2
    draw_icon((position[0], y), data['icon'])

def draw_day_letter(position, letter):
    text = font.render(letter, 1, colors.indigo_200)
    text_rect = text.get_rect()
    text_rect.center = position
    surface.blit(text, text_rect)

def draw_temp(position, temp):
    text = font.render(temp, 1, colors.white)
    text_rect = text.get_rect()
    text_rect.center = position
    surface.blit(text, text_rect)

def draw_icon(position, icon):
    path = f'icons/{icon}'
    
    if (exists(path) == False):
        return

    icon = pygame.image.load(path)
    width = icon.get_width()
    height = icon.get_height()
    surface.blit(icon, (position[0] - (width//2), position[1] - (height//2)))