import math


class Vector:

    def __init__(self, x: float, y: float):
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls, start_point: tuple,
                                    end_point: tuple):
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self):
        vector_length = Vector.get_length(self)
        return Vector(self.x / vector_length, self.y / vector_length)

    def angle_between(self, vector):
        cos_a = Vector.get_normalized(self) * Vector.get_normalized(vector)
        return math.ceil(math.degrees(math.acos(cos_a)))

    def get_angle(self):
        cos_a = self.y / Vector.get_length(self)
        return round(math.degrees(math.acos(cos_a)))

    def rotate(self, degrees: int):
        return Vector(math.cos(math.radians(degrees)) * self.x -
                      math.sin(math.radians(degrees)) * self.y,
                      math.sin(math.radians(degrees)) * self.x +
                      math.cos(math.radians(degrees)) * self.y)
