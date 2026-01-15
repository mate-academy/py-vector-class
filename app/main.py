from __future__ import annotations

import math
from math import sqrt, acos, degrees


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: float | Vector) -> float | Vector:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        return Vector(self.x * other, self.y * other)

    @classmethod
    def create_vector_by_two_points(
            cls,
            start_point: tuple,
            end_point: tuple
    ) -> Vector:
        return Vector(
            end_point[0] - start_point[0], end_point[1] - start_point[1]
        )

    def get_length(self) -> float:
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def get_angle(self) -> float:
        return round(degrees(acos(self.y / self.get_length())))

    def get_normalized(self) -> Vector:
        return Vector(self.x / self.get_length(), self.y / self.get_length())

    def angle_between(self, other: Vector) -> float:
        return round(
            degrees(
                acos(self * other / (self.get_length() * other.get_length()))
            )
        )

    def rotate(self, angle: int) -> Vector:
        x_coord = self.x
        y_coord = self.y
        cos = math.cos(math.radians(angle))
        sin = math.sin(math.radians(angle))
        self.x = round(x_coord * cos - y_coord * sin, 2)
        self.y = round(x_coord * sin + y_coord * cos, 2)
        return self
