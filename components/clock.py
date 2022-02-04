import sys
from datetime import datetime

sys.path.append('../')
import pygame
import colors
import fonts

padding = 10

date_font = fonts.font_4xl
time_font = fonts.font_9xl
ampm_font = fonts.font_6xl

def draw(screen, x, y, width, height):

    # Draw Date
    date_text = date_font.render(date(), 1, colors.white)
    date_text_rect = date_text.get_rect()
    date_text_rect.topleft = (x + padding, y + padding)
    screen.blit(date_text, date_text_rect)

    # Draw Time
    time_text = time_font.render(time(), 1, colors.white)
    time_text_rect = time_text.get_rect()
    time_text_rect.topleft = (x + padding, date_text_rect.y + date_text_rect.height + date_text_rect.height//2)
    screen.blit(time_text, time_text_rect)

    # AM/PM
    y_offset_time = time_font.metrics(time())[0][3]
    y_offset_ampm = ampm_font.metrics(ampm())[0][3]

    ampm_text = ampm_font.render(ampm(), 1, colors.white)
    ampm_text_rect = ampm_text.get_rect()
    ampm_text_rect.topleft = (x + padding + time_text_rect.width + fonts.font_4xl.get_height()//2, time_text_rect.y + (y_offset_time - y_offset_ampm))
    screen.blit(ampm_text, ampm_text_rect)

def date():
    return datetime.now().strftime("%A, %B") + " " + str(int(datetime.now().strftime("%d")))

def time():
    hours = str(int(datetime.now().strftime("%I")))
    minutes = datetime.now().strftime("%M")
    return f'{hours}:{minutes}'

def ampm():
    return datetime.now().strftime("%p")