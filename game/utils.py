# game/utils.py
from settings import TILE_SIZE, PADDING

def get_center(x, y):
    return (PADDING + x * TILE_SIZE + TILE_SIZE // 2,
            PADDING + y * TILE_SIZE + TILE_SIZE // 2)

def get_grid_from_pos(pos):
    x = int((pos[0] - PADDING) // TILE_SIZE)
    y = int((pos[1] - PADDING) // TILE_SIZE)
    return [x, y]

def is_at_center(pos):
    offset_x = (pos[0] - PADDING) % TILE_SIZE
    offset_y = (pos[1] - PADDING) % TILE_SIZE
    center_offset = TILE_SIZE // 2
    return abs(offset_x - center_offset) < 2 and abs(offset_y - center_offset) < 2
