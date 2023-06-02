from __future__ import annotations
from math import cos, sin, radians, acos, degrees


class Vector:
    def __init__(self, x_: int | float, y_: int | float) -> None:
        self.x = round(x_, 2)
        self.y = round(y_, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int | float | Vector) -> int | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls,
                                    start_point: tuple,
                                    end_point: tuple) -> Vector:
        return Vector(
            end_point[0] - start_point[0],
            end_point[1] - start_point[1]
        )

    def get_length(self) -> int | float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int | float:
        dot_product = self.x * other.x + self.y * other.y
        length = self.get_length() * other.get_length()
        result = acos(dot_product / length)
        return round(degrees(result))

    def get_angle(self) -> int | float:
        return self.angle_between(Vector(0, 1))

    def rotate(self, degrees: int) -> Vector:
        cos_x = cos(radians(degrees)) * self.x
        cos_y = cos(radians(degrees)) * self.y
        sin_x = sin(radians(degrees)) * self.x
        sin_y = sin(radians(degrees)) * self.y
        rotate_x = cos_x - sin_y
        rotate_y = sin_x + cos_y
        return Vector(rotate_x, rotate_y)
