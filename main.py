import sys, pygame
from decouple import config
import ui, colors
import update

CAPTION = config('CAPTION', default='Home Dashboard', cast=str)
FPS = config('FPS', default=1, cast=int)

pygame.init()
screen = pygame.display.set_mode((ui.SCREEN_WIDTH, ui.SCREEN_HEIGHT))
pygame.display.set_caption(CAPTION)
clock = pygame.time.Clock()

# Hide Mouse
pygame.mouse.set_visible(config('SHOW_MOUSE', default=False, cast=bool))

UPDATE_EVENTS = {}
for component in update.list_active_components():
    if (callback := update.get_component_callback(component)):
        update_frequency = update.get_update_frequency(component)
        event_type = pygame.event.custom_type()
        UPDATE_EVENTS[event_type] = callback
        pygame.time.set_timer(event_type, 1000 * update_frequency)
        if config('UPDATE_ON_STARTUP', default=False, cast=bool):
            callback()

while True:

    screen.fill(colors.bg_color)

    for row_index in range(len(ui.rows)):
        ui.draw_row(screen, row_index)

    for event in pygame.event.get():

        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()

        if event.type in UPDATE_EVENTS:
            UPDATE_EVENTS[event.type]()

    pygame.display.update()
    clock.tick(FPS)
