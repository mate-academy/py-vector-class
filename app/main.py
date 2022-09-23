class Vector:

    def __init__(self, coord_x, coord_y):
        self.coord_x = round(coord_x, 2)
        self.coord_y = round(coord_y, 2)

    def __str__(self):
        return f"Vector {self.coord_x} {self.coord_y}"

    def __add__(self, other):
        if isinstance(other, Vector):
            self.coord_x = self.coord_x + other.coord_x
            self.coord_y = self.coord_y + other.coord_y
            return Vector(self.coord_x, self.coord_y)

    def __sub__(self, other):
        if isinstance(other, Vector):
            self.coord_x = self.coord_x - other.coord_x
            self.coord_y = self.coord_y - other.coord_y
            return Vector(self.coord_x, self.coord_y)