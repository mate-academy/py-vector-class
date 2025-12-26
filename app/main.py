import math


class Vector:
    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return Vector(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        else:
            dot_product = self.x * other.x + self.y * other.y
            return dot_product

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple, end_point: tuple):
        x = end_point[0] - start_point[0]
        y = end_point[1] - start_point[1]
        return cls(x, y)

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        vector2 = self
        length = self.get_length()
        vector2.x = round(self.x / length, 2)
        vector2.y = round(self.y / length, 2)
        return vector2

    def angle_between(self, other):
        dot_production = self.__mul__(other)
        angle = dot_production / (self.get_length() * other.get_length())
        return round(math.degrees(math.acos(angle)))

    def get_angle(self):
        angle = self.y / self.get_length()
        return round(math.degrees(math.acos(angle)))

    def rotate(self, degrees: int):
        x = self.x
        y = self.y
        self.x = round(x * math.cos(math.radians(degrees)) - y * math.sin(
            math.radians(degrees)), 2)
        self.y = round(x * math.sin(math.radians(degrees)) + y * math.cos(
            math.radians(degrees)), 2)
        return self
