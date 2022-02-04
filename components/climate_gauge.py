import sys, math
from datetime import datetime

sys.path.append('../')
import colors
import fonts
import pygame
from pygame import gfxdraw

padding = 10

def draw(screen, x, y, width, height):

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
    sun_radius = circle_radius//4
    gfxdraw.aacircle(screen, sun_pos[0], sun_pos[1], sun_radius, colors.yellow_500)
    gfxdraw.filled_circle(screen, sun_pos[0], sun_pos[1], sun_radius, colors.yellow_500)

    # Draw Temperature
    current_temp = 65
    temp_text = fonts.font_8xl.render(f'{current_temp}°', 1, colors.white)
    temp_text_rect = temp_text.get_rect()
    temp_text_rect.center = (center[0], center[1] + temp_text.get_height()//6)
    screen.blit(temp_text, temp_text_rect)

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