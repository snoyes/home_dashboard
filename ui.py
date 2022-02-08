import pygame, sys, json
from decouple import config
from fractions import Fraction

SCREEN_WIDTH = config('SCREEN_WIDTH', default=1080, cast=int)
SCREEN_HEIGHT = config('SCREEN_HEIGHT', default=1920, cast=int)
DEBUG_GRID = config('DEBUG_GRID', default=False, cast=bool)
GRID_MARGIN = config('GRID_MARGIN', default=30, cast=int)

def draw_row(screen, row_number):
    y = row_y(row_number)
    row_height = rows[row_number]["height"]
    use_margin = rows[row_number]["use_margin"]
    x = GRID_MARGIN if use_margin else 0
    
    for column in rows[row_number]['columns']:
        
        if (DEBUG_GRID):
            shape = pygame.Rect(x, y, column["width"], row_height)
            pygame.Surface.fill(screen, column["color"], shape)
            pygame.rect()

        if "component" in column:
            rect = pygame.Rect(x, y, column['width'], row_height)
            column["component"](screen, rect)

        x += column["width"]

def row_y(row_number):
    if row_number == 0:
        return 0
    elif row_number == 1:
        return rows[0]["height"]
    y = 0

    for i in range(row_number):
        y += rows[i]["height"]

    return y

def get_component_callback(component_name):
    sys.path.append('components')
    module = __import__(component_name)
    return getattr(module, 'draw')

def get_rows():
    with open('template.json') as json_file:
        grid_data = json.load(json_file)

    rows = []

    for row in grid_data['rows']:
        columns = []
        
        for column in row['columns']:
            margins = (GRID_MARGIN * 2) if row['use_margin'] else 0
            columns.append({
                "width": int((SCREEN_WIDTH - margins) * Fraction(column['width'])),
                "component": get_component_callback(column['component'])
            })

        rows.append({
            "height": int(SCREEN_HEIGHT * Fraction(row['height'])),
            "columns": columns,
            "use_margin": row["use_margin"]
        })
    
    return rows

rows = get_rows()