import math


class Vector:

    def __init__(self, x: float = 0.00, y: float = 0.00):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(x=self.x + round(other.x, 2),
                      y=self.y + round(other.y, 2))

    def __sub__(self, other):
        return Vector(x=self.x - round(other.x, 2),
                      y=self.y - round(other.y, 2))

    def __mul__(self, other):
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(x=round(self.x * other, 2),
                      y=round(self.y * other, 2))

    @staticmethod
    def create_vector_by_two_points(start_point: tuple, end_point: tuple):
        return Vector(round(end_point[0] - start_point[0], 2),
                      round(end_point[1] - start_point[1], 2))

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        vector_length = (self.x ** 2 + self.y ** 2) ** 0.5
        return Vector(x=round(self.x / vector_length, 2),
                      y=round(self.y / vector_length, 2))

    def angle_between(self, other):
        length_self = (self.x ** 2 + self.y ** 2) ** 0.5
        length_other = (other.x ** 2 + other.y ** 2) ** 0.5
        cos_a = (self.x * other.x + self.y * other.y) / \
                (length_self * length_other)
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        cos_a = self.y / (self.x ** 2 + self.y ** 2) ** 0.5
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees):
        x2 = \
            self.x * math.cos(math.radians(degrees)) - \
            self.y * math.sin(math.radians(degrees))
        y2 = \
            self.y * math.cos(math.radians(degrees)) + \
            self.x * math.sin(math.radians(degrees))
        return Vector(x2, y2)
