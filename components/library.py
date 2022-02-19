import colors
import fonts
import json

padding = 10

font = fonts.font_6xl

def draw(screen, rect):
    text = get_text().split('\n')
    content_height = font.get_height() * len(text)
    center = (rect.x + rect.width//2, rect.y + rect.height//2)
    content_y = center[1] - content_height//2

    for num, line in enumerate(text):
        text_item = font.render(line, 1, colors.white)
        text_rect = text_item.get_rect()
        text_rect.midtop = (center[0], content_y + num*font.get_height())
        screen.blit(text_item, text_rect)

def get_text():
    try:
        with open('cache/.library') as f:
            data = json.load(f)
        total_checked_out = sum(card['checked_out_count'] for card in data)
        total_overdue = sum(card['overdue_count'] for card in data)
        text = f'{total_checked_out} items checked out from library.'
        if total_overdue > 0:
            text += f'\n{total_overdue} are overdue.'
        return text


    except FileNotFoundError:
        return 'No library data available.'
