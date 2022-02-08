import sys, math
from datetime import datetime
from os.path import exists

sys.path.append('../')
import colors
import fonts
import pygame
import weather
from pygame import gfxdraw
from decouple import config

padding = 10
ICON_SCALE = config('ICON_SCALE', default=1, cast=int)

def draw(screen, rect):

    weather_data = weather.current()

    if not weather_data:
        # TODO: Add loading text/animation
        return

    center = (rect.x + (rect.width//2) - 10, rect.y + (rect.height//2) - fonts.font_2xl.get_height())

    # Draw Circle
    circle_radius = rect.width//10*8//2
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
    current_temp = str(round(weather_data['temp']))
    temp_text = fonts.font_8xl.render(f'{current_temp}°', 1, colors.white)
    temp_text_rect = temp_text.get_rect()
    temp_text_rect.center = (center[0], center[1] - ((50 if ICON_SCALE > 1 else 25)//2))
    screen.blit(temp_text, temp_text_rect)

    # Draw Icon
    icon_name = weather_data['weather'][0]['icon'] + ("@2x" if ICON_SCALE > 1 else "") + ".png"
    icon_path = f'icons/weather/{icon_name}'
    
    if (exists(icon_path)):
        icon = pygame.image.load(icon_path)
        icon_width = icon.get_width()
        icon_height = icon.get_height()
        screen.blit(icon, (center[0] - (icon_width//2), center[1]))

    # Draw Sunrise/Sunset Time
    next_sun_event = get_next_sun_event(weather_data)
    sun_change_text = next_sun_event[0][0].upper() + next_sun_event[0][1:] + " at " + format_time(next_sun_event[1])
    sun_change_text = fonts.font_2xl.render(sun_change_text, 1, colors.white)
    sun_change_text_rect = sun_change_text.get_rect()
    sun_change_text_rect.center = (center[0], center[1] + circle_radius + fonts.font_2xl.get_height()*2)
    screen.blit(sun_change_text, sun_change_text_rect)

def sun_position(center, radius, degrees):
    radians = degrees/180*math.pi
    return (int(radius * math.cos(radians) + center[0]), int(radius * math.sin(radians) + center[1]))

def hours_to_degrees(hours):
    return (hours/24 * 360 + 90) % 360

def get_next_sun_event(today):

    if datetime.fromtimestamp(today['sunrise']) > datetime.now():
        return ('sunrise', today['sunrise'])

    if datetime.fromtimestamp(today['sunset']) > datetime.now():
        return ('sunset', today['sunset'])

    # Sun has set for today so get tomorrow's sunrise
    return ('sunrise', weather.daily()[1]['sunrise'])

def format_time(timestamp):
    time = datetime.fromtimestamp(timestamp)
    hours = str(int(time.strftime("%I")))
    minutes = time.strftime("%M")
    ampm = time.strftime("%p")
    return f'{hours}:{minutes} {ampm}'