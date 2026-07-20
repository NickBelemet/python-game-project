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

    
    #method to check if block is inside the grid
    def is_inside_grid(self, row, col):
        if row >= 0 and row < self.num_rows and col >= 0 and col < self.num_cols:
            return True
        else:
            return False


    def is_cell_empty(self, row, col):
        if self.grid[row][col] == 0:
            return True
        else:
            return False
        

    def is_row_full(self, row):
        for col in range(self.num_cols): 
            if self.grid[row][col] == 0: 
                return False 
        return True
    

    def clear_row(self, row): 
        for col in range(self.num_cols): 
            self.grid[row][col] = 0

        
    def move_rows_down(self,row,num_rows):
        for col in range(self.num_cols): 
            self.grid[row +num_rows][col] = self.grid[row][col]
            self.grid[row][col] = 0


    def reset(self):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.grid[row][col] = 0

    def clear_full_row(self):
        completed = 0 
        for row in range(self.num_rows - 1, 0, -1): 
            if self.is_row_full(row): 
                self.clear_row(row)
                completed += 1
            elif completed > 0: 
                self.move_rows_down(row, completed)
        return completed

    def draw(self, screen): 
        for row in range(self.num_rows):
            for col in range(self.num_cols): 
                cell_value = self.grid[row][col] 
                cell_rectangle = pygame.Rect(col * self.cell_size +10, row * self.cell_size +10,
                self.cell_size -1, self.cell_size -1)
                pygame.draw.rect(screen, self.colors[cell_value], cell_rectangle)