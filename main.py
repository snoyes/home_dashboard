import sys, pygame, os
from decouple import config
import ui, colors, services.weather as weather

CAPTION = config('CAPTION', default='Home Dashboard', cast=str)
FPS = config('FPS', default=1, cast=int)

pygame.init()
screen = pygame.display.set_mode((ui.SCREEN_WIDTH, ui.SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()

if not os.path.exists('cache/.weather_data'):
    os.mkdir('cache')

# Hide Mouse
pygame.mouse.set_visible(config('SHOW_MOUSE', default=False, cast=bool))

# Create timer to fetch weather at intervals
FETCH_WEATHER = pygame.USEREVENT+1
pygame.time.set_timer(FETCH_WEATHER, int(1000 * 60 * weather.FREQUENCY))
weather.update()

while True:

    screen.fill(colors.bg_color)

    for row_index in range(len(ui.rows)):
        ui.draw_row(screen, row_index)

    for event in pygame.event.get():

        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type == FETCH_WEATHER:
            weather.update()

    pygame.display.update()
    clock.tick(FPS)