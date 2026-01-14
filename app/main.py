from __future__ import annotations
from math import sqrt, acos, degrees, sin, cos, radians


class Vector:

    def __init__(self, xxx: int | float, yyy: int | float) -> None:
        self.x = round(xxx, 2)
        self.y = round(yyy, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Vector | int | float) -> int | float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return cls(end_point[0] - start_point[0],
                   end_point[1] - start_point[1])

    def get_length(self) -> int | float:
        return sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, vector2: Vector) -> int | float:
        dot_product = self.x * vector2.x + self.y * vector2.y
        norm_a = self.get_length()
        norm_b = vector2.get_length()
        return round(degrees(acos(dot_product / (norm_a * norm_b))))

    def get_angle(self) -> int:
        return round(degrees(acos(self.y / sqrt(self.x ** 2 + self.y ** 2))))

    def rotate(self, degrees: int) -> Vector:
        new_x = round(cos(radians(degrees))
                      * self.x - sin(radians(degrees)) * self.y, 2)

        new_y = round(sin(radians(degrees))
                      * self.x + cos(radians(degrees)) * self.y, 2)
        self.x, self.y = new_x, new_y
        return self
