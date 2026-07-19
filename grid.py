import pygame
from colour import Colours

class Grid: 
    def __init__(self): 
        self.num_rows = 20 
        self.num_cols = 10 
        self.cell_size = 30 
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]  
        self.colors = Colours.get_cell_color()

    def print_grid(self): 
        for row in range(self.num_rows): 
            for col in range(self.num_cols): 
                print(self.grid[row][col], end=' ') 
            print()  

    
    def draw(self, screen): 
        for row in range(self.num_rows):
            for col in range(self.num_cols): 
                cell_value = self.grid[row][col] 
                cell_rectangle = pygame.Rect(col * self.cell_size +1, row * self.cell_size +1,
                self.cell_size -1, self.cell_size -1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rectangle)