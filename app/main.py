import math


class Vector:

    def __init__(self, x: float = 0.00, y: float = 0.00):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(x=round(self.x, 2) + round(other.x, 2),
                      y=round(self.y, 2) + round(other.y, 2))

    def __sub__(self, other):
        return Vector(x=self.x - round(other.x, 2),
                      y=self.y - round(other.y, 2))

    def __mul__(self, other):
        if isinstance(other, Vector):
            return (self.x * other.x) + (self.y * other.y)
        return Vector(x=round(self.x * other, 2), y=round(self.y * other, 2))

    @staticmethod
    def create_vector_by_two_points(start_point: tuple, end_point: tuple):
        return Vector(round(end_point[0] - start_point[0], 2),
                      round(end_point[1] - start_point[1], 2))

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        return Vector(x=round(self.x / (self.get_length()), 2),
                      y=round(self.y / (self.get_length()), 2))

    def angle_between(self, other):
        cos_a = (self.x * other.x + self.y * other.y) / (
                (self.get_length()) * other.get_length())
        return round(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        cos_a = self.y / self.get_length()
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees):
        x2 = math.cos(math.radians(degrees)
                      ) * self.x - math.sin(math.radians(degrees)) * self.y
        y2 = math.sin(math.radians(degrees)
                      ) * self.x + math.cos(math.radians(degrees)) * self.y
        return Vector(x2, y2)
