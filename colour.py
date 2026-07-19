class Colours: 
    dark_grey = (27, 31, 40) 
    green = (48, 230, 23) 
    red = (240, 15, 15) 
    orange = (225, 115, 18) 
    yellow = (237, 234, 4) 
    purple = (166, 0, 247) 
    cyan = (20, 205, 210) 
    blue = (14, 64, 216) 

    @classmethod
    def get_cell_color(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]  