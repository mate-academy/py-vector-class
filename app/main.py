import math
from math import sqrt


class Vector:
    def __init__(self, vector_x: float, vector_y: float) -> None:
        self.x = round(vector_x, 2)
        self.y = round(vector_y, 2)

    def __add__(self, other: tuple) -> tuple:
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: tuple) -> tuple:
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: tuple | int | float) -> tuple | int | float:
        if not isinstance(other, Vector):
            return Vector(self.x * other, self.y * other)
        elif isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> tuple:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> int | float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> tuple:
        length = Vector.get_length(self)
        if self.x != 0 and self.y != 0:
            norm_x = self.x / length
            norm_y = self.y / length
            return Vector(norm_x, norm_y)
        elif self.x != 0 and self.y == 0:
            return Vector(length / self.x, self.y)
        else:
            return Vector(self.x, length / self.y)

    def angle_between(self, other: tuple) -> int | float:
        if isinstance(other, Vector):
            self_length = Vector.get_length(self)
            other_length = Vector.get_length(other)
            multiply = self.__mul__(other)
            cos_a = multiply / (self_length * other_length)
            degrees = math.degrees(math.acos(cos_a))
            return round(degrees)

    def get_angle(self) -> int | float:
        other = Vector(0, 1)
        self_length = Vector.get_length(self)
        other_length = Vector.get_length(other)
        multiply = self.__mul__(other)
        cos_a = multiply / (self_length * other_length)
        degrees = math.degrees(math.acos(cos_a))
        return round(degrees)

    def rotate(self, degrees: int | float) -> int | float:
        rad = math.radians(degrees)
        x_2 = math.cos(rad) * self.x - math.sin(rad) * self.y
        y_2 = math.sin(rad) * self.x + math.cos(rad) * self.y
        return Vector(x_2, y_2)
