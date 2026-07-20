class Colours: 
    dark_grey = (27, 31, 40) 
    green = (48, 230, 23) 
    red = (240, 15, 15) 
    orange = (225, 115, 18) 
    yellow = (237, 234, 4) 
    purple = (100, 0, 200) 
    cyan = (20, 205, 210) 
    blue = (14, 64, 216) 
    white = (255, 255, 255)
    dark_purple = (170, 0, 250)
    lilac = (200, 100, 250)

    @classmethod
    def get_cell_color(cls):
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]  