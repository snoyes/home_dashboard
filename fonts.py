import pygame, ui
from decouple import config


FONT_SCALE = config("FONT_SCALE", default=0.5, cast=float)
BASE_FONT_SIZE = config("BASE_FONT_SIZE", default=18, cast=int)

def scale_text(multiplier):
    return int(multiplier * BASE_FONT_SIZE * FONT_SCALE)

pygame.font.init()

font_xs = pygame.font.SysFont('manjari', scale_text(0.75))
font_sm = pygame.font.SysFont('manjari', scale_text(0.875))
font_md = pygame.font.SysFont('manjari', scale_text(1))
font_lg = pygame.font.SysFont('manjari', scale_text(1.125))
font_xl = pygame.font.SysFont('manjari', scale_text(1.25))
font_2xl = pygame.font.SysFont('manjari', scale_text(1.5))
font_3xl = pygame.font.SysFont('manjari', scale_text(1.875))
font_4xl = pygame.font.SysFont('manjari', scale_text(2.25))
font_5xl = pygame.font.SysFont('manjari', scale_text(3))
font_6xl = pygame.font.SysFont('manjari', scale_text(3.75))
font_7xl = pygame.font.SysFont('manjari', scale_text(4.5))
font_8xl = pygame.font.SysFont('manjari', scale_text(6))
font_9xl = pygame.font.SysFont('manjari', scale_text(8))