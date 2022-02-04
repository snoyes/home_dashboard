import sys
from datetime import datetime

sys.path.append('../')
import pygame
import colors
import fonts

padding = 10
font = fonts.font_4xl
row_height = font.get_height()


def draw(screen, x, y, width, height):

    global surface
    surface = screen

    column_plus_padding = (width - (padding*2))/5
    column_padding = column_plus_padding/10
    column_width = column_padding*8
    column_height = (column_padding*2) + (row_height + row_height//2) * 5 + fonts.font_3xl.get_height()
    table_width = column_plus_padding*5

    padding_x = (width - table_width)//2
    padding_y = (height - column_height)//2

    x_pos = x + padding_x + column_padding + column_width//2

    # First Column - Today
    draw_column((x_pos, y + padding_y), {
        "letter": "M",
        "high": "68",
        "low": "43",
        "icon": "x",
        "chance_of_rain": "0",
    })
    
    # Border around first column
    border_rect = (x + padding_x + column_padding//2, y + padding_y, column_padding + column_width, column_height)
    pygame.draw.rect(screen, colors.white, border_rect, 2, 5)

    x_pos += column_padding*2 + column_width

    # Second Column
    draw_column((x_pos, y + padding_y), {
        "letter": "M",
        "high": "68",
        "low": "43",
        "icon": "x",
        "chance_of_rain": "0",
    })

    x_pos += column_padding*2 + column_width

    # Third Column
    draw_column((x_pos, y + padding_y), {
        "letter": "M",
        "high": "68",
        "low": "43",
        "icon": "x",
        "chance_of_rain": "0",
    })

    x_pos += column_padding*2 + column_width

    # Fourth Column
    draw_column((x_pos, y + padding_y), {
        "letter": "M",
        "high": "68",
        "low": "43",
        "icon": "x",
        "chance_of_rain": "0",
    })

    x_pos += column_padding*2 + column_width

    # Fifth Column
    draw_column((x_pos, y + padding_y), {
        "letter": "M",
        "high": "68",
        "low": "43",
        "icon": "x",
        "chance_of_rain": "0",
    })


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
    y += row_height + row_height//2
    draw_chance_of_rain((position[0], y), data['chance_of_rain'])

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
    text = font.render(icon, 1, colors.white)
    text_rect = text.get_rect()
    text_rect.center = position
    surface.blit(text, text_rect)

def draw_chance_of_rain(position, percent):
    text = fonts.font_2xl.render(percent, 1, colors.white)
    text_rect = text.get_rect()
    text_rect.center = position
    surface.blit(text, text_rect)