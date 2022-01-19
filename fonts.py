import pygame
import ui

TEXT_SCALE = 1

def scale_text(pixels):
    return int(pixels * TEXT_SCALE)

pygame.font.init()

font_xs = pygame.font.SysFont('manjari', scale_text(8))
font_sm = pygame.font.SysFont('manjari', scale_text(12))
font_md = pygame.font.SysFont('manjari', scale_text(16))
font_lg = pygame.font.SysFont('manjari', scale_text(24))
font_xl = pygame.font.SysFont('manjari', scale_text(32))
font_2xl = pygame.font.SysFont('manjari', scale_text(48))
font_3xl = pygame.font.SysFont('manjari', scale_text(64))
font_4xl = pygame.font.SysFont('manjari', scale_text(92))
font_5xl = pygame.font.SysFont('manjari', scale_text(192))
font_6xl = pygame.font.SysFont('manjari', scale_text(288))