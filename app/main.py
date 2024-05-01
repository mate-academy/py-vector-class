from __future__ import annotations
from math import acos, pi, cos, sin, radians


class Vector:
    def __init__(self, x_coordinate: float, y_coordinate: float) -> None:
        self.x = round(x_coordinate, 2)
        self.y = round(y_coordinate, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector((self.x + other.x), (self.y + other.y))

    def __sub__(self, other: Vector) -> Vector:
        return Vector((self.x - other.x), (self.y - other.y))

    def __mul__(self, other: Vector | float) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector((self.x * other), (self.y * other))

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return Vector(
            end[0] - start[0], end[1] - start[1]
        )

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        x_coefficient = round((self.x ** 2 / (self.x ** 2 + self.y ** 2))
                              ** 0.5, 2)
        y_coefficient = round((self.y ** 2 / (self.x ** 2 + self.y ** 2))
                              ** 0.5, 2)
        if self.x < 0:
            x_coefficient = -x_coefficient
        if self.y < 0:
            y_coefficient = -y_coefficient
        return Vector(x_coefficient, y_coefficient)

    def angle_between(self, other: Vector) -> int | float:
        return round(
            180 * acos((self.x * other.x + self.y * other.y)
                       / ((self.x ** 2 + self.y ** 2) ** 0.5
                          * (other.x ** 2 + other.y ** 2) ** 0.5)) / pi
        )

    def get_angle(self) -> int:
        return round(180 * acos(self.y / (self.x ** 2 + self.y ** 2) ** 0.5
                                * 1 ** 0.5) / pi)

    def rotate(self, angle: int) -> Vector:
        x_rotated = round(cos(radians(angle))
                          * self.x - sin(radians(angle)) * self.y, 2)
        y_rotated = round(sin(radians(angle))
                          * self.x + cos(radians(angle)) * self.y, 2)
        return Vector(x_rotated, y_rotated)
