from grid import Grid
from blocks import *
import random 


class Game: 
    def __init__(self): 
        self.grid = Grid()
        self.blocks = [IBlock(), LBlock(), JBlock(), SBlock(), OBlock(), TBlock(), ZBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()

    def get_random_block(self): 
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), LBlock(), JBlock(), SBlock(), OBlock(), TBlock(), ZBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    #new method move left 
    def move_left(self): 
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False: 
            self.current_block.move(0, 1)

    #new method move right
    def move_right(self): 
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False: 
            self.current_block.move(0, -1)

    #new method move down
    def move_down(self): 
        self.current_block.move(1, 0)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(-1, 0) 
            self.lock_block()

    
    def lock_block(self): 
        tiles = self.current_block.get_cell_pos()
        for position in tiles: 
            self.grid.grid[position.row][position.column] = self.current_block.id
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        self.grid.clear_full_row()


    def block_fits(self): 
        tiles = self.current_block.get_cell_pos()
        for tile in tiles: 
            if self.grid.is_cell_empty(tile.row, tile.column) == False:
                return False 
        return True


    def block_inside(self): 
        tiles = self.current_block.get_cell_pos()
        for tile in tiles:
            if self.grid.is_inside_grid(tile.row, tile.column) == False:
                return False
        return True


    def rotate(self):
        self.current_block.rotate()
        if self.block_inside() == False or self.block_fits() == False: 
            self.current_block.undo_rotation()
            


    def draw(self, screen): 
        self.grid.draw(screen)
        self.current_block.draw(screen)