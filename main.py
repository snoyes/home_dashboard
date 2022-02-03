import pygame
import sys
import ui, colors, fonts

pygame.init()
screen = pygame.display.set_mode((ui.SCREEN_WIDTH, ui.SCREEN_HEIGHT))
pygame.display.set_caption('Home Dashboard')
clock = pygame.time.Clock()
grid_debug = True

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def draw_row(row_number):
    y = ui.row_y(row_number)
    row_height = ui.rows[row_number]["height"]
    use_margin = ui.rows[row_number]["use_margin"]
    x = ui.grid_margin if use_margin else 0
    
    for item in ui.grid[row_number]:
        x += item["width"]
        
        if (grid_debug):
            shape = pygame.Rect(x, y, item["width"], row_height)
            pygame.Surface.fill(screen, item["color"], shape)


        if "component" in item:
            item["component"](screen, x, y, item['width'], row_height)

while True:
    screen.fill(colors.indigo_900)
    draw_text('Example Text', fonts.font_md, colors.white, screen, 20, 20)

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
    clock.tick(30)