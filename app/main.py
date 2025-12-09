from __future__ import annotations

import math
from typing import Union
from math import sqrt


class Vector:
    def __init__(
        self,
        x: Union[int, float],  # noqa: VNE001
        y: Union[int, float],  # noqa: VNE001
    ) -> None:
        self.x = round(x, 2)
        self.y = round(y, 2)

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(
        self, other: Union[Vector, int, float]
    ) -> Union[Vector, int, float]:
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)

        if isinstance(other, Vector):
            return self.x * other.x + self.y * other.y

        raise TypeError

    @classmethod
    def create_vector_by_two_points(
        cls, point1: tuple, point2: tuple
    ) -> Vector:
        x, y = point2[0] - point1[0], point2[1] - point1[1]
        return cls(x, y)

    def get_length(self) -> float:
        return sqrt(self.x**2 + self.y**2)

    def get_normalized(self) -> Vector:
        x = round(self.x / self.get_length(), 2)  # noqa: VNE001
        y = round(self.y / self.get_length(), 2)  # noqa: VNE001
        return Vector(x, y)

    def angle_between(self, other: Vector) -> int:
        len1, len2 = self.get_length(), other.get_length()
        dot = self.x * other.x + self.y * other.y
        cos_a = dot / (len1 * len2)
        angle = math.degrees(math.acos(cos_a))
        return math.ceil(angle)

    def get_angle(self) -> int:
        length = self.get_length()
        cos_a = self.y / length
        angle = math.degrees(math.acos(cos_a))
        return round(angle)

    def rotate(self, degrees: int) -> Vector:
        rad = math.radians(degrees)
        cos_a = math.cos(rad)
        sin_a = math.sin(rad)

        x_new = self.x * cos_a - self.y * sin_a
        y_new = self.x * sin_a + self.y * cos_a

        return Vector(x_new, y_new)
