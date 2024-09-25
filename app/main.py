from __future__ import annotations
from typing import Any
from math import degrees, sin, cos, acos, radians


class Vector:
    def __init__(self, xx: float, yy: float) -> None:
        self.x = round(xx, 2)
        self.y = round(yy, 2)

    @classmethod
    def create_vector_by_two_points(
            cls, start_point: tuple, end_point: tuple) -> Vector:
        return Vector(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> Any:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        return self.x * other.x + self.y * other.y

    def get_length(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def get_normalized(self) -> Vector:
        length = self.get_length()
        return Vector(self.x / length, self.y / length)

    def angle_between(self, other: Vector) -> int:
        return round(degrees(acos(
            (self * other) / (self.get_length() * other.get_length())
        )))

    def get_angle(self) -> int:
        return round(degrees(acos(
            (self * Vector(0, 1))
            / (self.get_length() * Vector(0, 1).get_length())
        )))

    def rotate(self, degree: int) -> Vector:
        return Vector(
            self.x * cos(radians(degree)) - self.y * sin(radians(degree)),
            self.x * sin(radians(degree)) + self.y * cos(radians(degree))
        )
