from __future__ import annotations
from typing import Any
from math import radians, cos, sin, acos, degrees


class Vector:
    def __init__(self, x: int | float, y: int | float) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Any) -> Vector | float:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        else:
            return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(cls, start: tuple, end: tuple) -> Vector:
        return Vector(end[0] - start[0], end[1] - start[1])

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> int:
        cosines = (self * other) / (self.get_length() * other.get_length())
        return round(degrees(acos(cosines)))

    def get_angle(self) -> int:
        positive_y_axis = Vector(0, 1)
        return self.angle_between(positive_y_axis)

    def rotate(self, degree: int) -> Vector:
        x = round(
            self.x * cos(radians(degree))
            - self.y * sin(radians(degree)), 2
        )
        y = round(
            self.x * sin(radians(degree))
            + self.y * cos(radians(degree)), 2
        )

        return Vector(x, y)
