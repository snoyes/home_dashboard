import sys
from datetime import datetime

sys.path.append('../')
import colors
import fonts

padding = 10
starting_y = 0

def draw(screen, x, y, width, height):

    # Draw Date
    date_text = fonts.font_4xl.render(date(), 1, colors.white)
    date_text_rect = date_text.get_rect()
    date_text_rect.topleft = (x + padding, y + padding)
    screen.blit(date_text, date_text_rect)

    # Draw Time
    time_text = fonts.font_8xl.render(time(), 1, colors.white)
    time_text_rect = time_text.get_rect()
    time_text_rect.topleft = (x + padding, date_text_rect.y + date_text_rect.height + date_text_rect.height//3)
    screen.blit(time_text, time_text_rect)

def date():
    return datetime.now().strftime("%A, %B") + " " + str(int(datetime.now().strftime("%d")))

def time():
    hours = str(int(datetime.now().strftime("%I")))
    minutes = datetime.now().strftime("%M")
    ampm = datetime.now().strftime("%p")
    return f'{hours}:{minutes} {ampm}'