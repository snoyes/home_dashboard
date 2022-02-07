import sys, math, json
from datetime import datetime
from os.path import exists

sys.path.append('../')
import colors
import fonts
import pygame
from pygame import gfxdraw
from decouple import config

padding = 10
ICON_SCALE = config('ICON_SCALE', default=1, cast=int)

def draw(screen, x, y, width, height):

    if(exists('.weather_data') == False):
        # TODO: Add loading text/animation
        return

    with open('.weather_data') as json_file:
        weather_data = json.load(json_file)

    current_weather_data = weather_data['current']

    center = (x + (width//2) - 10, y + (height//2))

    # Draw Circle
    circle_radius = width//10*8//2
    gfxdraw.aacircle(screen, center[0], center[1], circle_radius, colors.white)
    gfxdraw.filled_circle(screen, center[0], center[1], circle_radius, colors.white)
    gfxdraw.aacircle(screen, center[0], center[1], circle_radius-4, colors.indigo_800)
    gfxdraw.filled_circle(screen, center[0], center[1], circle_radius-4, colors.indigo_800)

    # Draw Sun
    current_hour = int(datetime.now().strftime("%H"))
    current_minute = int(datetime.now().strftime("%M"))
    sun_pos = sun_position(center, circle_radius, hours_to_degrees(current_hour+(current_minute/60)))
    sun_radius = circle_radius//5
    gfxdraw.aacircle(screen, sun_pos[0], sun_pos[1], sun_radius, colors.yellow_500)
    gfxdraw.filled_circle(screen, sun_pos[0], sun_pos[1], sun_radius, colors.yellow_500)

    # Draw Temperature
    current_temp = str(round(current_weather_data['temp']))
    temp_text = fonts.font_8xl.render(f'{current_temp}°', 1, colors.white)
    temp_text_rect = temp_text.get_rect()
    temp_text_rect.center = (center[0], center[1] - ((50 if ICON_SCALE > 1 else 25)//2))
    screen.blit(temp_text, temp_text_rect)

    # Draw Icon
    icon_name = current_weather_data['weather'][0]['icon'] + ("@2x" if ICON_SCALE > 1 else "") + ".png"
    icon_path = f'icons/weather/{icon_name}'
    
    if (exists(icon_path)):
        icon = pygame.image.load(icon_path)
        icon_width = icon.get_width()
        icon_height = icon.get_height()
        screen.blit(icon, (center[0] - (icon_width//2), center[1]))

    # Draw Sunrise/Sunset Time
    sun_change_text = fonts.font_2xl.render("Sunset at 6:11 PM", 1, colors.white)
    sun_change_text_rect = sun_change_text.get_rect()
    sun_change_text_rect.center = (center[0], center[1] + circle_radius + fonts.font_2xl.get_height()*1.5)
    screen.blit(sun_change_text, sun_change_text_rect)

def sun_position(center, radius, degrees):
    radians = degrees/180*math.pi
    return (int(radius * math.cos(radians) + center[0]), int(radius * math.sin(radians) + center[1]))

def hours_to_degrees(hours):
    return (hours/24 * 360 + 90) % 360