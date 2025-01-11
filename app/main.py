from __future__ import annotations

import math
from typing import Union


class Vector:
    def __init__(self, x_coord: float, y_coord: float) -> None:
        self.x = round(x_coord, 2)
        self.y = round(y_coord, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other: Union[Vector, float]) -> Union[Vector, float]:
        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y
        elif isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        raise TypeError

    @classmethod
    def create_vector_by_two_points(cls, p1: tuple[float],
                                    p2: tuple[float]) -> Vector:
        return cls(p2[0] - p1[0], p2[1] - p1[1])

    def get_length(self) -> float:
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def get_normalized(self) -> Vector:
        length = self.get_length()
        if length == 0:
            raise ValueError
        return Vector(self.x / length, self.y / length)

    def angle_between(self, vector: Vector) -> float:
        distance1 = self.get_length()
        distance2 = vector.get_length()
        cos = (self * vector) / (distance1 * distance2)
        return round(math.degrees(math.acos(cos)))

    def get_angle(self) -> float:
        return round(self.angle_between(Vector(0, 1)))

    def rotate(self, degrees: float) -> Vector:
        radians = math.radians(degrees)
        cos = math.cos(radians)
        sin = math.sin(radians)
        x2 = self.x * cos - self.y * sin
        y2 = self.x * sin + self.y * cos
        return Vector(x2, y2)
