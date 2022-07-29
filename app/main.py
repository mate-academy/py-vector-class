import math


class Vector:

    def __init__(self,
                 x: float,
                 y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return Vector(self.x * other, self.y * other)
        # scalar
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple):
        return cls(end[0] - start[0], end[1] - start[1])

    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self):
        length = self.get_length()
        return Vector(round(self.x / length, 2), round(self.y / length, 2))

    def angle_between(self, other):
        nom = self * other  # scalar
        denom = self.get_length() * other.get_length()
        cosine = nom / denom
        degree = math.degrees(math.acos(cosine))
        return round(degree)

    def get_angle(self):
        axis = Vector(0, 1)
        return self.angle_between(axis)

    def rotate(self, degree: int):
        d = math.radians(degree)
        x2 = math.cos(d) * self.x - math.sin(d) * self.y
        y2 = math.sin(d) * self.x + math.cos(d) * self.y
        return Vector(x2, y2)
