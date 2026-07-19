from dis import Positions

from colour import Colours
import pygame
from position import Position

class Block: 
    def __init__(self, id):
        self.id = id
        self.cells = {} 
        self.cell_size = 30 
        self.row_offset = 0
        self.col_offset = 0
        self.rotation_state = 0 
        self.colors = Colours.get_cell_color()

    def move(self, rows, columns):
        self.row_offset += rows 
        self.col_offset += columns 

    def get_cell_pos(self): 
        tiles = self.cells[self.rotation_state]
        moved_tiles = [] 
        for position in tiles: 
            position = Position(position.row + self.row_offset, position.column + self.col_offset)
            moved_tiles.append(position)
        return moved_tiles


    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0

    
    def undo_rotation(self):
        self.rotation_state -= 1 
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells) - 1



    def draw(self, screen): 
        tiles = self.get_cell_pos()
        for tile in tiles: 
            tile_rect = pygame.Rect(tile.column * self.cell_size +1, tile.row * self.cell_size +1,
                                    self.cell_size -1, self.cell_size -1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)


