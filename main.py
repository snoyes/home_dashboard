import sys, pygame, requests, json
import ui, colors, fonts
from decouple import config

pygame.init()
screen = pygame.display.set_mode((ui.SCREEN_WIDTH, ui.SCREEN_HEIGHT))
pygame.display.set_caption('Home Dashboard')
clock = pygame.time.Clock()
fps = 1
debug_grid = config('DEBUG_GRID', default=False, cast=bool)
OPEN_WEATHER_MAP_API_KEY = config('OPEN_WEATHER_MAP_API_KEY')
OPEN_WEATHER_MAP_API_URL = "https://api.openweathermap.org"

LOCATION_LAT = config('LOCATION_LAT', cast=float)
LOCATION_LONG = config('LOCATION_LONG', cast=float)

weather_data = {}

def get_weather_forecast():
    print('get weather')

    try:
        r = requests.get(f'{OPEN_WEATHER_MAP_API_URL}/data/2.5/onecall?lat={LOCATION_LAT}&lon={LOCATION_LONG}&appid={OPEN_WEATHER_MAP_API_KEY}&exclude=minutely,hourly,alerts&units=imperial')
    except:
        print('Error: unable to retrieve weather data')
    else:
        errorMessage = ""
        global weather_data
        weather_data = r.json()
        print(weather_data['current']['dt'])
        weather_data_file = open(".weather_data", "w") 
        weather_data_file.write(json.dumps(weather_data, indent = 4))
        weather_data_file.close()
        

get_weather_forecast()

def draw_row(row_number):
    y = ui.row_y(row_number)
    row_height = ui.rows[row_number]["height"]
    use_margin = ui.rows[row_number]["use_margin"]
    x = ui.grid_margin if use_margin else 0
    
    for item in ui.grid[row_number]:
        
        if (debug_grid):
            shape = pygame.Rect(x, y, item["width"], row_height)
            pygame.Surface.fill(screen, item["color"], shape)


        if "component" in item:
            item["component"](screen, x, y, item['width'], row_height)

        x += item["width"]

while True:
    screen.fill(colors.indigo_800)

    for row_index in range(len(ui.grid)):
        draw_row(row_index)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_SPACE:
                pygame.display.set_mode((200, 300))
            if event.key == pygame.K_a:
                pygame.display.set_mode((540, 900))
    pygame.display.update()
    clock.tick(fps)