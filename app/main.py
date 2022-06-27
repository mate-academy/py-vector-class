import math


class Vector:

    def __init__(self, x, y):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(round(self.x + other.x, 2), round(self.y + other.y, 2))

    def __sub__(self, other):
        return Vector(round(self.x - other.x, 2), round(self.y - other.y, 2))

    def __mul__(self, other):
        if type(other) == Vector:
            return (self.x * other.x) + (self.y * other.y)
        else:
            return Vector(round(self.x * other, 2), round(self.y * other, 2))

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        return cls(round(end_point[0] - start_point[0], 2),
                   round(end_point[1] - start_point[1], 2))

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(round(self.x / (self.x ** 2 + self.y ** 2) ** 0.5, 2),
                      round(self.y / (self.x ** 2 + self.y ** 2) ** 0.5, 2))

    def angle_between(self, other):
        cos_a = (self.x * other.x + self.y * other.y) / (((
            self.x ** 2 + self.y ** 2) ** 0.5) * (
                (other.x ** 2 + other.y ** 2) ** 0.5))
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        cos_a = self.y / ((self.x ** 2 + self.y ** 2) ** 0.5)
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees):
        x2 = math.cos(math.radians(degrees)
                      ) * self.x - math.sin(math.radians(degrees)) * self.y
        y2 = math.sin(math.radians(degrees)
                      ) * self.x + math.cos(math.radians(degrees)) * self.y
        return Vector(round(x2, 2), round(y2, 2))
