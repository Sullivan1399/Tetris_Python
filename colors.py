class Colors:
    dark_grey = (26, 31, 40)
    dark_blue = (44, 44, 127)
    green = (47, 230, 23)
    red = (232, 18, 18)
    orange = (226, 116, 17)
    yellow = (237, 234, 4)
    purple = (166, 0, 247)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)
    white = (255, 255, 255)
    light_blue = (59, 85, 162)

    # @classmethod is a Python decorator that allows to define a method that can be called on a class rather than on an instance of the class.
    @classmethod
    def get_cell_color(cls):   # cls is a reference to the class itself andit allows us to access the class-level attributes
        return [cls.dark_grey, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue]