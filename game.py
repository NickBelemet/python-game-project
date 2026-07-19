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

    #new method move right
    def move_right(self): 
        self.current_block.move(0, 1)

    #new method move down
    def move_down(self): 
        self.current_block.move(1, 0)

    def draw(self, screen): 
        self.grid.draw(screen)
        self.current_block.draw(screen)