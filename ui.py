import pygame
import colors
import sys

# adding components folder the system path
sys.path.insert(0, '/home/anthony/Code/python/home_dashboard/components')
import alerts
import clock
import countdown
import climate_gauge
import weather_forecast

# SCREEN_WIDTH = 1080 
# SCREEN_HEIGHT = 1920

# Get from .env
SCREEN_ORIENTATION = 'landscape'

if SCREEN_ORIENTATION == 'landscape':
    DEFAULT_WIDTH = 1920
    DEFAULT_HEIGHT = 1080
else: 
    DEFAULT_WIDTH = 1080
    DEFAULT_HEIGHT = 1920


# Get from .env
SCREEN_WIDTH = 540
SCREEN_HEIGHT = 960

def row_y(row_number):
    if row_number == 0:
        return 0
    elif row_number == 1:
        return rows[0]["height"]
    y = 0

    for i in range(row_number):
        y += rows[i]["height"]

    return y

rows = []

rows.append({
    "height": SCREEN_HEIGHT*1//16,
    "use_margin": False
})
rows.append({
    "height": SCREEN_HEIGHT*2//16,
    "use_margin": True
})
rows.append({
    "height": SCREEN_HEIGHT*4//16,
    "use_margin": True
})
rows.append({
    "height": SCREEN_HEIGHT*2//16,
    "use_margin": True
})
rows.append({
    "height": SCREEN_HEIGHT*4//16,
    "use_margin": False
})
rows.append({
    "height": SCREEN_HEIGHT*3//16,
    "use_margin": False
})


grid_margin = 30

grid_one_third = (SCREEN_WIDTH - (grid_margin*2))//3
grid_two_thirds = (SCREEN_WIDTH - (grid_margin*2))*2//3
grid_five_twelfth = (SCREEN_WIDTH - (grid_margin*2))*5//12
grid_seven_twelfth = (SCREEN_WIDTH - (grid_margin*2))*7//12
grid_full = SCREEN_WIDTH

grid = []

# Row 0
row = []
row.append({
    "color": colors.red_500,
    "width": SCREEN_WIDTH
})
grid.append(row)


# Row 1
row = []
row.append({
    "color": colors.yellow_500,
    "width": grid_two_thirds,
    "component": clock.draw
})
row.append({
    "color": colors.green_500,
    "width": grid_one_third,
    "component": countdown.draw
})
grid.append(row)

# Row 2
row = []
row.append({
    "color": colors.green_500,
    "width": grid_five_twelfth,
    "component": climate_gauge.draw
})
row.append({
    "color": colors.purple_500,
    "width": grid_seven_twelfth,
    "component": weather_forecast.draw
})
grid.append(row)

# Row 3
row = []
row.append({
    "color": colors.blue_500,
    "width": grid_one_third,
})
row.append({
    "color": colors.red_500,
    "width": grid_one_third,
})
row.append({
    "color": colors.green_500,
    "width": grid_one_third,
})
grid.append(row)

# Row 4
row = []
row.append({
    "color": colors.yellow_500,
    "width": SCREEN_WIDTH
})
grid.append(row)

# Row 5
row = []
row.append({
    "color": colors.blue_500,
    "width": SCREEN_WIDTH//2
})
row.append({
    "color": colors.red_500,
    "width": SCREEN_WIDTH//2
})
grid.append(row)



